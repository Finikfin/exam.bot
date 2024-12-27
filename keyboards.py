from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import config as c

inline_kb_builder = InlineKeyboardBuilder()

for x in range(len(c.TICKET_IMAGES)):
    inline_kb_builder.button(text=str(x + 1), callback_data=f"btn{x+1}")

inline_kb_builder.adjust(4, repeat=True)
inline_kb_full = InlineKeyboardMarkup(inline_keyboard=inline_kb_builder.export())
