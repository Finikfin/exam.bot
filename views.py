from aiogram import types
from models import exam_ticket

async def start_command(message: types.Message):
    await message.answer("Привет! Я бот, который выдаёт билеты на экзамен. Напиши 'билет', чтобы получить билет.")

async def get_ticket_command(message: types.Message):
    ticket = exam_ticket.get_random_ticket()
    await message.answer(f"Ваш билет: {ticket}")