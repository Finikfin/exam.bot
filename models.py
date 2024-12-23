import random
from datetime import datetime
TICKET_IMAGES_COPY = [
    "билеты/Билет№01.png",
    "билеты/Билет№02.png",
    "билеты/Билет№03.png",
    "билеты/Билет№04.png",
    "билеты/Билет№05.png",
    "билеты/Билет№06.png",
    "билеты/Билет№07.png",
    "билеты/Билет№08.png",
    "билеты/Билет№09.png",
    "билеты/Билет№10.png",
    "билеты/Билет№11.png",
    "билеты/Билет№12.png",
    "билеты/Билет№13.png",
    "билеты/Билет№14.png",
    "билеты/Билет№15.png",
    "билеты/Билет№16.png",
    "билеты/Билет№17.png",
    "билеты/Билет№18.png",
    "билеты/Билет№19.png",
    "билеты/Билет№20.png"
]
class ExamTicket:
    def __init__(self):
        self.ticket_list = TICKET_IMAGES_COPY

    def get_random_ticket(self):
        return random.choice(self.ticket_list)

# Пример билетов
exam_ticket = ExamTicket()