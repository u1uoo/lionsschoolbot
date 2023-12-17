import logging

from messages.main import MESSAGES
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from keyboards.inline.main_menu import menu_main, hw_menu, support_menu
from keyboards.default.main import start_menu
from keyboards.inline.callback_data import menu_callback
from states.main import MainStates
from loader import dp, cursor, connection

logger = logging.getLogger(__name__)

@dp.callback_query_handler(menu_callback.filter(item_name="start"),
                           state="*")
async def start(call: CallbackQuery, state: FSMContext):
    try:
        logger.info(
            f'User @{call.from_user.username} {call.from_user.full_name} (id: {call.from_user.id}) opened '
            f'/start')
        async with state.proxy() as data:
            if 'hw_messages' in data:
                for msg in data['hw_messages']:
                    await msg.delete()
                    data.pop('hw_messages', None)
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


@dp.callback_query_handler(menu_callback.filter(item_name="hw"),
                           state="*")
async def hw(call: CallbackQuery, state: FSMContext):
    try:
        logger.info(
            f'User @{call.from_user.username} {call.from_user.full_name} (id: {call.from_user.id}) opened '
            f'/hw')
        connection.commit()
        cursor.execute('SELECT date, time, hometask FROM Users WHERE username = ?', (call.from_user.username,))
        results = cursor.fetchall()
        await call.message.delete()
        hw_messages = []
        if results:
            for i in range(len(results)-1):
                hw_messages.append(await call.bot.send_message(call.from_user.id, 
                                            "Домашнее задание на {date} число, {hours}:{minutes}: {hometask}".format(
                                                    date = results[i][0],hours = results[i][1][:2],
                                                    minutes = results[i][1][2:],hometask = results[i][2])))
            await call.bot.send_message(call.from_user.id, 
                                        "Домашнее задание на {date} число, {hours}:{minutes}: {hometask}".format(
                                                date = results[-1][0],hours = results[-1][1][:2],
                                                minutes = results[-1][1][2:],hometask = results[-1][2]), reply_markup=hw_menu)
            async with state.proxy() as data:
                data['hw_messages'] = hw_messages
        else:
            await call.bot.send_message(call.from_user.id,
                                        MESSAGES["no_hw"],
                                        reply_markup=hw_menu)
    except Exception as err:
        msg = f'Error in /hw: {err}'
        logger.error(msg)



    except Exception as err:
        msg = f'Error in /support: {err}'
        logger.error(msg)

@dp.callback_query_handler(menu_callback.filter(item_name="support"),
                           state="*")
async def start(call: CallbackQuery, state: FSMContext):
    try:
        logger.info(
            f'User @{call.from_user.username} {call.from_user.full_name} (id: {call.from_user.id}) opened '
            f'/start')
        await call.message.delete()
        await call.bot.send_message(call.from_user.id,
                                       MESSAGES["support"],
                                       reply_markup=support_menu)
    except Exception as err:
        msg = f'Error in show_menu: {err}'
        logger.error(msg)