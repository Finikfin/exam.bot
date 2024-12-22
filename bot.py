import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
from aiogram import Router
from config import TOKEN
from views import start_command, get_ticket_command


logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher()


router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await start_command(message)

@router.message(F.text == "билет")
async def cmd_ticket(message: types.Message):
    await get_ticket_command(message)


dp.include_router(router)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())