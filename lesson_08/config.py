import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("YOUGILE_API_KEY")
COMPANY_ID = os.getenv("YOUGILE_COMPANY_ID")
BASE_URL = "https://yougile.com"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
