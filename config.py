import os

dir = "./tickets/"

TOKEN = "7691139246:AAGVxWa_2QPiOPUoNjiqjgYRFe_l2QnBQFk"
TEACHER_IDS = [
    245851335,  # Александр Афанасьев
    405521598,  # Михаил Хромов
    154599813,  # Сергей Смаглюк
    363004163,  # Дмитрий Смирнов
]
STUDENT_IDS = [
    1648778328,  # Леша Писаненко
    847867090,  # Тимофей Яковлев
    1266213854,  # Артем Четокин
    114314156,  # Артем Абрамов
    1751823515,  # Степа Бармин
    5064226866,  # Лева Керский
    1309198139,  # Вета Полякова
    1254389035,  # Маша Захарова
    1817878343,  # Илья Гречин
    6269496850,  # Даня Петров
    6063850010,  # Матвей Мерзликин
    1827810009,  # Макар Удалов
    1362703815,  # Федя Воробьев
    6170560152,  # Вова Никитин
    1150266474,  # Дима Чураков
]

TICKET_IMAGES = []
for x in os.listdir(dir):
    TICKET_IMAGES.append(f"{dir}{x}")

TICKET_IMAGES_COPY = list(TICKET_IMAGES)
BIND_TICKET_IMAGES = {}
