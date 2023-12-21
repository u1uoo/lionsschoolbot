import logging


from messages.main import MESSAGES
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from keyboards.inline.main_menu import menu_main
from keyboards.inline.students_menu import students_main_menu
from keyboards.default.main import start_menu
from keyboards.inline.callback_data import menu_callback
from states.main import MainStates
from states.students import StudentsStates
from loader import dp
from utils.dbworkflow import get_homeworks

logger = logging.getLogger(__name__)

@dp.callback_query_handler(menu_callback.filter(item_name="start"),
                           state="*")
async def start(call: CallbackQuery, state: FSMContext):
    try:
        logger.info(
            f'User @{call.from_user.username} {call.from_user.full_name} (id: {call.from_user.id}) opened '
            f'/start')
        await call.message.delete()
        await call.bot.send_message(call.from_user.id,
                                       MESSAGES["start"],
                                       reply_markup=menu_main)
    except Exception as err:
        msg = f'Error in show_menu: {err}'
        logger.error(msg)
    finally:
        await MainStates.initial.set()


@dp.message_handler(text="Меню", state="*")
@dp.message_handler(Command("start"), state="*")
async def start(message: Message):
    try:
        logger.info(
            f'User @{message.chat.username} {message.chat.full_name} (id: {message.chat.id}) opened '
            f'/start')
        await message.delete()
        await message.bot.send_message(message.chat.id,
                                       MESSAGES["start"],
                                       reply_markup=menu_main)
    except Exception as err:
        msg = f'Error in show_menu: {err}'
        logger.error(msg)
    finally:
        await MainStates.initial.set()

