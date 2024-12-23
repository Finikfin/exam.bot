import logging
import keyboards as kb
from aiogram import types
from config import TEACHER_IDS, TICKET_IMAGES, BIND_TICKET_IMAGES
from models import exam_ticket
from aiogram.utils import markdown as md
from datetime import datetime
from aiogram.types import FSInputFile
from models import ExamTicket

async def start_command_teacher(message: types.Message):
    await message.answer("Привет, учитель! Я бот, который выдает билеты на экзамен. Напиши /get_ticket, чтобы получить информацию о билете.")

async def get_ticket_command_teacher(message: types.Message):
    pass
        
async def consultation_command_teacher(message: types.Message):
    pass

async def ready_command_teacher(message: types.Message):
    pass

async def get_tickets_command_teacher(message: types.Message):
    tic_keys = BIND_TICKET_IMAGES.keys()
    all_tic = []
    for i in TICKET_IMAGES:
        if i not in tic_keys:
            all_tic.append(f'{i[7:15]} - пока никто не взял этот билет')
    for key in BIND_TICKET_IMAGES:

        tic = str(f"{key[7:15]} - @{BIND_TICKET_IMAGES[key]}")
        all_tic.append(tic)
    all_tic_s = sorted(all_tic)
    responce = "\n".join(all_tic_s)
    await message.answer(f"Вот список всех билетов с привязкой к ученикам: \n{responce}")
    await message.reply("Выберите билет", reply_markup=kb.inline_kb_full)