import random
from datetime import datetime
from config import TICKET_IMAGES
class ExamTicket:
    def __init__(self):
        self.ticket_list = TICKET_IMAGES

    def get_random_ticket(self):
        return random.choice(self.ticket_list)

# Пример билетов
exam_ticket = ExamTicket()