import keyboards as kb
from aiogram import types
from config import TICKET_IMAGES, BIND_TICKET_IMAGES, dir


async def start_command_teacher(message: types.Message):
    await message.answer(
        "👋Привет, учитель! Я бот, который выдает билеты на экзамен. Напиши /get_ticket, чтобы получить информацию о билете."
    )


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
            all_tic.append(
                f"▪️{i.replace('.png', '').replace(dir, '')} - пока никто не взял этот билет"
            )
    for key in BIND_TICKET_IMAGES:

        tic = str(
            f"▪️{key.replace('.png', '').replace(dir, '')} - @{BIND_TICKET_IMAGES[key]}"
        )
        all_tic.append(tic)
    all_tic_s = sorted(all_tic)
    responce = "\n".join(all_tic_s)
    await message.answer(
        f"❕Вот список всех билетов с привязкой к ученикам: \n{responce}"
    )
    await message.reply("🤞Выберите билет", reply_markup=kb.inline_kb_full)
