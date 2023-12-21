from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from keyboards.inline.callback_data import menu_callback

menu_main = InlineKeyboardMarkup(row_width=1)
hw_btn = InlineKeyboardButton(text="📚 Домашние задания",
                                       callback_data=menu_callback.new(
                                           item_name="hw"
                                       ))
support_btn = InlineKeyboardButton(text="💬 Поддержка",
                                       callback_data=menu_callback.new(
                                           item_name="support"
                                       ))
menu_main.add(hw_btn, support_btn)

hw_menu = InlineKeyboardMarkup(row_width=1)
back_btn = InlineKeyboardButton(text="🔙 Вернуться в главное меню",
                                       callback_data=menu_callback.new(
                                           item_name="start"
                                       ))
hw_menu.add(back_btn)

support_menu = InlineKeyboardMarkup(row_width=1)
support_menu.add(back_btn)
