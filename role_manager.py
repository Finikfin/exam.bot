import logging
from aiogram import types
from config import TEACHER_IDS, TICKET_IMAGES
from models import exam_ticket
from aiogram.utils import markdown as md
from datetime import datetime
from aiogram.types import FSInputFile
from models import ExamTicket
from views import start_command_student, get_ticket_command_student, consultation_command_student, ready_command_student
async def start_command(message: types.Message):
    if message.from_user.id in TEACHER_IDS:
        await start_command_student(message)
    else:
        await start_command_student(message)

async def get_ticket_command(message: types.Message):
    if message.from_user.id in TEACHER_IDS:
        await get_ticket_command_student(message)
    else:
        await get_ticket_command_student(message)

        
async def consultation_command(message: types.Message):
    if message.from_user.id in TEACHER_IDS:
        await consultation_command_student(message)
    else:
        await consultation_command_student(message)

async def ready_command(message: types.Message):
    if message.from_user.id in TEACHER_IDS:
        await ready_command_student(message)
    else:
        await ready_command_student(message)