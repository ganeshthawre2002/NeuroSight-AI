from pathlib import Path
import os

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL not found in .env")

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000"
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")