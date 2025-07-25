import time
from openai import OpenAI
from src.config.settings import OPENAI_API_KEY
from src.utils.logger import logger

client = OpenAI(api_key=OPENAI_API_KEY)
MODEL = "o4-mini"

def call_gpt4_with_full_text(itext: str) -> str:
    """Calls the GPT-4 model with the provided text input."""
    logger.info("Calling GPT-4 with full text input")
    text_input = '\n'.join(itext) if isinstance(itext, list) else itext
    prompt = f"Please summarize inputan dan perbaiki teks yang kurang sesuai:\n{text_input}"
    start_time = time.time()
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "Kamu adalah ahli dalam bidang kecerdasan buatan dan AI engineer"},
            {"role": "assistant", "content": "Kamu dapat membaca inputan dan memberikan jawaban secara detail. Response dalam bentuk markdown"},
            {"role": "user", "content": prompt}
        ]
    )
    logger.info(f"GPT-4 response time: {time.time() - start_time:.2f} seconds")
    return response.choices[0].message.content.strip()

