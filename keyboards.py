from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_kb_full = InlineKeyboardBuilder()
bl_1 = InlineKeyboardButton(text='1', callback_data='btn1')
bl_2 = InlineKeyboardButton(text='2', callback_data='btn2')
bl_3 = InlineKeyboardButton(text='3', callback_data='btn3')
inline_kb_full.add(bl_1, bl_2, bl_3)
inline_kb_full = inline_kb_full.as_markup()