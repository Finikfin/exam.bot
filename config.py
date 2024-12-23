import os
dir = "./билеты"

TOKEN = "7691139246:AAGVxWa_2QPiOPUoNjiqjgYRFe_l2QnBQFk"
TEACHER_IDS = [6170560152, 245851335, 1362703815]  # Замените на реальные ID преподавателей
TICKET_IMAGES = []
for x in os.listdir(dir):
    TICKET_IMAGES.append(f'билеты/{x}')

TICKET_IMAGES_COPY = list(TICKET_IMAGES)
BIND_TICKET_IMAGES = {}