from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from keyboards.inline.callback_data import menu_callback

students_main_menu = InlineKeyboardMarkup(row_width=1)
add_student_button = InlineKeyboardButton(text="Добавить домашку",
                                       callback_data=menu_callback.new(
                                           item_name="add_student"
                                       ))

back_btn = InlineKeyboardButton(text="🔙 Вернуться в главное меню",
                                       callback_data=menu_callback.new(
                                           item_name="start"
                                       ))
students_main_menu.add(add_student_button,back_btn)

aftermath_menu = InlineKeyboardMarkup(row_width=1)
add__another_student_button = InlineKeyboardButton(text="Добавить еще домашку",
                                       callback_data=menu_callback.new(
                                           item_name="add_student"
                                       ))

aftermath_menu.add(add_student_button,back_btn)
