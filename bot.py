import logging
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters import Command
from aiogram.handlers import CallbackQueryHandler
from config import TOKEN
from role_manager import start_command, get_ticket_command, consultation_command, ready_command, get_tickets_command



logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher()


router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await start_command(message)

@router.message(Command("ticket"))
async def cmd_ticket(message: types.Message):
    await get_ticket_command(message)

@router.message(Command("consultation"))
async def cmd_consultation(message: types.Message):
    await consultation_command(message)

@router.message((Command("ready")))
async def cmd_ready(message: types.Message):
    await ready_command(message)

@router.message((Command("get_ticket")))
async def cmd_ready(message: types.Message):
    await get_tickets_command(message)
dp.include_router(router)

@router.callback_query(F.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    await bot.send_message(callback_query.from_user.id, f'Вот ваш билет! code={code}')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())