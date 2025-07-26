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
    prompt = f"Please summarize inputan dan perbaiki teks yang kurang sesuai. Exclude inputan yang tidak sesuai dengan pertanyaan:\n{text_input}"
    start_time = time.time()
    stream = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "Kamu adalah ahli dalam bidang kecerdasan buatan dan AI engineer"},
            {"role": "assistant", "content": "Kamu dapat membaca inputan dan memberikan jawaban secara detail. Response dalam bentuk markdown"},
            {"role": "user", "content": prompt}
        ],
        stream=True,
    )
    logger.info(f"GPT-4 response time: {time.time() - start_time:.2f} seconds")
    full_response = ""
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
                token = chunk.choices[0].delta.content
                full_response += token
                yield token  

