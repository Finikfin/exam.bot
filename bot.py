import logging
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.filters import Command
from aiogram.types import FSInputFile
from config import TOKEN, BIND_TICKET_IMAGES
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
    code = callback_query.data
    code = code[3:]
    if len(str(code)) == 1:
        code = f'0{code}'
    caption_text = f'Вот ваш билет №{code}! '
    file = FSInputFile(f"билеты/Билет№{code}.png")
    await bot.send_photo(chat_id=callback_query.from_user.id, photo=file, caption=caption_text)
    if f"билеты/Билет№{code}.png" in BIND_TICKET_IMAGES:
        await bot.send_message(chat_id=callback_query.from_user.id, text=f'Этот билет взял @{BIND_TICKET_IMAGES[f"билеты/Билет№{code}.png"]}')
    else:
        await bot.send_message(chat_id=callback_query.from_user.id, text='Этот билет пока никто не взял')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())