from pathlib import Path
from models import ApiHostModel


# API_HOST = ApiHostModel("http://127.0.0.1:80/api")
API_HOST = ApiHostModel("https://smart-room-production.up.railway.app/api")
DEBUG = False

BASE_DIR = Path(__file__).resolve().parent
