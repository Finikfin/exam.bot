import random
import config as c
from datetime import datetime
TICKET_IMAGES_COPY = list(c.TICKET_IMAGES)
class ExamTicket:
    def __init__(self):
        self.ticket_list = TICKET_IMAGES_COPY

    def get_random_ticket(self):
        return random.choice(self.ticket_list)

# Пример билетов
exam_ticket = ExamTicket()