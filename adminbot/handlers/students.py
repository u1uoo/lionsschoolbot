import logging


from messages.main import MESSAGES
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from keyboards.inline.main_menu import menu_main
from keyboards.inline.students_menu import students_main_menu, aftermath_menu
from keyboards.default.main import start_menu
from keyboards.inline.callback_data import menu_callback
from states.main import MainStates
from states.students import StudentsStates
from loader import dp
from utils.dbworkflow import add_homework
from utils.string_process import isnt_command

logger = logging.getLogger(__name__)


@dp.callback_query_handler(menu_callback.filter(item_name="students_menu"),
                           state=MainStates.initial)
async def students(call: CallbackQuery, state: FSMContext):
    try:
        logger.info(
            f'User @{call.from_user.username} {call.from_user.full_name} (id: {call.from_user.id}) opened '
            f'/new_student')
        await call.message.delete()
        await call.bot.send_message(call.from_user.id,
                                       MESSAGES["students_initial"],
                                       reply_markup=students_main_menu)
    except Exception as err:
        msg = f'Error in students_menu: {err}'
        logger.error(msg)
    finally:
        await StudentsStates.initial.set()

@dp.callback_query_handler(menu_callback.filter(item_name="add_student"),
                           state=StudentsStates.initial)
async def add_student(call: CallbackQuery, state: FSMContext):
    try:
        logger.info(
            f'User @{call.from_user.username} {call.from_user.full_name} (id: {call.from_user.id}) opened '
            f'/add_student')
        await call.message.delete()
        await call.bot.send_message(call.from_user.id,
                                       MESSAGES["add_student"])
    except Exception as err:
        msg = f'Error in add_student: {err}'
        logger.error(msg)
    finally:
        await StudentsStates.enter_student_username.set()

@dp.message_handler(lambda message: isnt_command(message.text), state=StudentsStates.enter_student_username)
async def process_student_username(message: Message, state: FSMContext):
    try:
        student_login = message.text.strip()
        logger.info(
            f'User @{message.chat.username} {message.chat.full_name} (id: {message.chat.id}) entered student_login '
            f'{student_login}')
        async with state.proxy() as data:
            data['student_username'] = student_login
        await message.bot.send_message(message.chat.id,"Введите имя учителя")
    except Exception as err:
        msg = f'Error in process_student_username: {err}'
        logger.error(msg)
    finally:
        await StudentsStates.enter_teacher_name.set()


@dp.message_handler(lambda message: isnt_command(message.text), state=StudentsStates.enter_teacher_name)
async def process_teacher_name(message: Message, state: FSMContext):
    try:
        teacher_name = message.text.strip()
        logger.info(
            f'User @{message.chat.username} {message.chat.full_name} (id: {message.chat.id}) entered teacher_name '
            f'{teacher_name}')
        async with state.proxy() as data:
            data['teacher_name'] = teacher_name
        await message.bot.send_message(message.chat.id,"Введите название курса")
    except Exception as err:
        msg = f'Error in process_teacher_name: {err}'
        logger.error(msg)
    finally:
        await StudentsStates.enter_course_name.set()

@dp.message_handler(lambda message: isnt_command(message.text), state=StudentsStates.enter_course_name)
async def process_course_name(message: Message, state: FSMContext):
    try:
        course_name = message.text.strip()
        logger.info(
            f'User @{message.chat.username} {message.chat.full_name} (id: {message.chat.id}) entered course_name '
            f'{course_name}')
        async with state.proxy() as data:
            data['course_name'] = course_name
        await message.bot.send_message(message.chat.id,"Введите дату сдачи ДЗ (только день)")
    except Exception as err:
        msg = f'Error in process_course_name: {err}'
        logger.error(msg)
    finally:
        await StudentsStates.enter_date.set()

@dp.message_handler(lambda message: isnt_command(message.text), state=StudentsStates.enter_date)
async def process_date(message: Message, state: FSMContext):
    try:
        date = message.text.strip()
        logger.info(
            f'User @{message.chat.username} {message.chat.full_name} (id: {message.chat.id}) entered date '
            f'{date}')
        async with state.proxy() as data:
            data['date'] = date
        await message.bot.send_message(message.chat.id,"Введите время сдачи ДЗ в формате 'ЧЧ ММ'")
    except Exception as err:
        msg = f'Error in process_date: {err}'
        logger.error(msg)
    finally:
        await StudentsStates.enter_time.set()

@dp.message_handler(lambda message: isnt_command(message.text), state=StudentsStates.enter_time)
async def process_time(message: Message, state: FSMContext):
    try:
        time = message.text.strip()
        logger.info(
            f'User @{message.chat.username} {message.chat.full_name} (id: {message.chat.id}) entered time '
            f'{time}')
        async with state.proxy() as data:
            data['time'] = time
        await message.bot.send_message(message.chat.id,"Введите задание ученику")
    except Exception as err:
        msg = f'Error in process_time: {err}'
        logger.error(msg)
    finally:
        await StudentsStates.enter_task.set()

@dp.message_handler(lambda message: isnt_command(message.text), state=StudentsStates.enter_task)
async def process_task(message: Message, state: FSMContext):
    try:
        task = message.text.strip()
        logger.info(
            f'User @{message.chat.username} {message.chat.full_name} (id: {message.chat.id}) entered task '
            f'{task}')
        async with state.proxy() as data:
            data['task'] = task
            await add_homework(data['student_username'], data['teacher_name'], data['course_name'],
                               data['date'], data['time'], data['task'])
        await message.bot.send_message(message.chat.id,"Домашка успешно добавлена", reply_markup=aftermath_menu)
    except Exception as err:
        msg = f'Error in process_task: {err}'
        logger.error(msg)
    finally:
        await StudentsStates.enter_task.set()