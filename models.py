import random
import config as c
from datetime import datetime
from config import TICKET_IMAGES_COPY

class ExamTicket:
    def __init__(self):
        self.ticket_list = TICKET_IMAGES_COPY

    def get_random_ticket(self):
        return random.choice(self.ticket_list)

# Пример билетов
exam_ticket = ExamTicket()