import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
from aiogram import Router
from config import TOKEN
from views import start_command, get_ticket_command, consultation_command, ready_command


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

@router.message((Command("consultation")))
async def cmd_consultation(message: types.Message):
    await consultation_command(message)

@router.message((Command("ready")))
async def cmd_ready(message: types.Message):
    await ready_command(message)

dp.include_router(router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())