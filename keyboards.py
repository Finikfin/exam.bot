from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_kb_builder = InlineKeyboardBuilder()

for x in range(20):
    inline_kb_builder.button(text=str(x+1), callback_data=f"btn{x+1}")

inline_kb_builder.adjust(4, repeat=True)
inline_kb_full = InlineKeyboardMarkup(inline_keyboard=inline_kb_builder.export())