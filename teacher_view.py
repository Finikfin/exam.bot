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
async def start_command_teacher(message: types.Message):
    await message.answer("Привет! Я бот, который выдает билеты на экзамен. Напиши /get_ticket, чтобы получить информацию о билете.")

async def get_ticket_command_teacher(message: types.Message):
    pass
        
async def consultation_command_teacher(message: types.Message):
    pass

async def ready_command_teacher(message: types.Message):
    pass

async def get_tickets_command_teacher(message: types.Message):
    pass
