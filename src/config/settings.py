import os
from dotenv import load_dotenv

load_dotenv(override=True)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ACTIVELOOP_TOKEN = os.getenv("ACTIVELOOP_TOKEN")
VECTOR_STORE_PATH = os.getenv("VECTOR_STORE_PATH")
LOG_PATH = os.getenv("LOG_PATH")
PDF_PATH = os.getenv("PDF_PATH")
OUTPUT_PATH = os.getenv("OUTPUT_PATH")