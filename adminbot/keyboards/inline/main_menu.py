from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from keyboards.inline.callback_data import menu_callback

menu_main = InlineKeyboardMarkup(row_width=1)
students_btn = InlineKeyboardButton(text="Работа с учениками",
                                       callback_data=menu_callback.new(
                                           item_name="students_menu"
                                       ))


hw_menu = InlineKeyboardMarkup(row_width=1)
back_btn = InlineKeyboardButton(text="🔙 Вернуться в главное меню",
                                       callback_data=menu_callback.new(
                                           item_name="start"
                                       ))

menu_main.add(students_btn)
