import logging
from aiogram import types
from config import TEACHER_IDS, TICKET_IMAGES
from models import exam_ticket
from aiogram.utils import markdown as md
from datetime import datetime
from aiogram.types import FSInputFile
from models import ExamTicket
from student_view import start_command_student, get_ticket_command_student, consultation_command_student, ready_command_student, get_tickets_command_student
from teacher_view import start_command_teacher, get_ticket_command_teacher, consultation_command_teacher, ready_command_teacher, get_tickets_command_teacher


async def start_command(message: types.Message):
    if message.from_user.id in TEACHER_IDS:
        await start_command_teacher(message)
    else:
        await start_command_student(message)

async def get_ticket_command(message: types.Message):
    if message.from_user.id in TEACHER_IDS:
        await get_ticket_command_teacher(message)
    else:
        await get_ticket_command_student(message)

        
async def consultation_command(message: types.Message):
    if message.from_user.id in TEACHER_IDS:
        await consultation_command_teacher(message)
    else:
        await consultation_command_student(message)

async def ready_command(message: types.Message):
    if message.from_user.id in TEACHER_IDS:
        await ready_command_teacher(message)
    else:
        await ready_command_student(message)

async def get_tickets_command(message: types.Message):
    if message.from_user.id in TEACHER_IDS:
        await get_tickets_command_teacher(message)
    else:
        await get_tickets_command_student(message)