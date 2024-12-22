import logging
from aiogram import types
from config import TEACHER_IDS, TICKET_IMAGES
from models import exam_ticket
from aiogram.utils import markdown as md

async def start_command(message: types.Message):
    await message.answer("Привет! Я бот, который выдает билеты на экзамен. Напиши 'билет', чтобы получить билет.")

async def get_ticket_command(message: types.Message):
    current_time = datetime.utcnow()
    if current_time < datetime(2024, 12, 27, 10, 30):
        await message.answer("Билеты будут доступны не ранее 10:30 27.12.")
        return

    ticket = exam_ticket.get_random_ticket()
    await message.answer_photo(photo=open(ticket, 'rb'), caption="Ваш билет.")
    
    # Уведомление преподавателей
    for teacher_id in TEACHER_IDS:
        await message.bot.send_message(teacher_id, md.text(
            "Студент ", message.from_user.id, " запросил билет: ", ticket
        ))
        
async def consultation_command(message: types.Message):
    ticket = exam_ticket.get_random_ticket()
    for teacher_id in TEACHER_IDS:
        await message.bot.send_message(teacher_id, md.text(
            "Студент ", message.from_user.id, " запросил консультацию по билету: ", ticket
        ))