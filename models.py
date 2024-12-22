import random

class ExamTicket:
    def __init__(self, ticket_list):
        self.ticket_list = ticket_list

    def get_random_ticket(self):
        return random.choice(self.ticket_list)


tickets = [
    "Билет 1:",
    "Билет 2:",
    "Билет 3:",
    "Билет 4:",
    "Билет 5:"
]

exam_ticket = ExamTicket(tickets)