import random
from datetime import datetime
TICKET_IMAGES_COPY = [
    "билеты/Билет№1.png",
    "билеты/Билет№2.png",
    "билеты/Билет№3.png",
    "билеты/Билет№4.png",
    "билеты/Билет№5.png",
    "билеты/Билет№6.png",
    "билеты/Билет№7.png",
    "билеты/Билет№8.png",
    "билеты/Билет№9.png",
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