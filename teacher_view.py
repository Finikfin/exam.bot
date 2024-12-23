import logging
from aiogram import types
from config import TEACHER_IDS, TICKET_IMAGES
from models import exam_ticket
from aiogram.utils import markdown as md
from datetime import datetime
from aiogram.types import FSInputFile
from models import ExamTicket
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_kb_full = InlineKeyboardMarkup()
bl_1 = InlineKeyboardButton('билет 1', callback_data='btn1')
bl_2 = InlineKeyboardButton('билет 2', callback_data='btn2')
bl_3 = InlineKeyboardButton('билет 3', callback_data='btn3')
inline_kb_full.add(bl_1, bl_2, bl_3)



async def start_command_teacher(message: types.Message):
    await message.answer("Привет! Я бот, который выдает билеты на экзамен. Напиши /get_ticket, чтобы получить информацию о билете.")

async def get_ticket_command_teacher(message: types.Message):
    pass
        
async def consultation_command_teacher(message: types.Message):
    pass

async def ready_command_teacher(message: types.Message):
    pass

async def get_tickets_command_teacher(message: types.Message):
    await message.reply("Выберите билет", reply_markup=kb.inline_kb1)

@dp.callback_query_handler(func=lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    await bot.send_message(callback_query.from_user.id, f'Вот ваш билет! code={code}')