import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

TOKEN = os.environ.get("TOKEN")
TEACHER_IDS = os.environ.get("TEACHER_IDS").split('\n')
STUDENT_IDS = os.environ.get("STUDENT_IDS").split('\n')
dir = "./tickets/"

TICKET_IMAGES = []
# for x in os.listdir(dir):
#     TICKET_IMAGES.append(f"{dir}{x}")

TICKET_IMAGES_COPY = list(TICKET_IMAGES)
BIND_TICKET_IMAGES = {}
