import logging
from aiogram import types
from config import TEACHER_IDS, TICKET_IMAGES, BIND_TICKET_IMAGES
from models import exam_ticket
from aiogram.utils import markdown as md
from datetime import datetime
from aiogram.types import FSInputFile
from models import ExamTicket, TICKET_IMAGES_COPY
async def start_command_student(message: types.Message):
    await message.answer("👋Привет, ученик! Я бот, который выдает билеты на экзамен. Напиши /ticket, чтобы получить билет.")

async def get_ticket_command_student(message: types.Message):
    if message.from_user.username not in list(BIND_TICKET_IMAGES.values()):
        exam_ticket = ExamTicket()
        random_ticket = exam_ticket.get_random_ticket()
        file = FSInputFile(random_ticket)
        current_time = datetime.now()
        # if current_time < datetime(2024, 12, 27, 10, 30):
        #     await message.answer("Билеты будут доступны не ранее 10:30 27.12.")
        #     return

        ticket = random_ticket
        await message.answer_photo(photo=file, caption="❕Ваш билет. Чтобы запросить консультацию, напиши /consultation, если ты готов сдавать, напиши /ready. Удачи!")
        
        # Уведомление преподавателей
        for teacher_id in TEACHER_IDS:
            caption_text = f"❕@{message.from_user.username} запросил билет: {ticket}."
            await message.bot.send_photo(chat_id=teacher_id, photo=file, caption=caption_text)
        BIND_TICKET_IMAGES[ticket] = message.from_user.username
        TICKET_IMAGES_COPY.remove(ticket)
    else:
        await message.answer('⛔️Ты уже взял билет⛔️')

        
async def consultation_command_student(message: types.Message):
    ticket = exam_ticket.get_random_ticket()
    for teacher_id in TEACHER_IDS:
        await message.bot.send_message(teacher_id, md.text(
            f"❕@{message.from_user.username} запросил консультацию по билету: {ticket}"
        ))
    await message.answer("🕐В скором времени с вами свяжется один из преподавателей")

async def ready_command_student(message: types.Message):
    ticket = exam_ticket.get_random_ticket()
    for teacher_id in TEACHER_IDS:
        await message.bot.send_message(teacher_id, md.text(
            f"❕@{message.from_user.username} готов сдавать билет: {ticket}"
        ))
    await message.answer("🕐В скором времени с вами свяжется один из преподавателей")

async def get_tickets_command_student(message: types.Message):
    pass