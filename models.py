import random
from datetime import datetime

class ExamTicket:
    def __init__(self, ticket_list):
        self.ticket_list = ticket_list

    def get_random_ticket(self):
        return random.choice(self.ticket_list)

# Пример билетов
exam_ticket = ExamTicket(["ticket1.png", "ticket2.png", "ticket3.png"])