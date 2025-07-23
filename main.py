from src.data.data_prep import extract_text_from_pdf
from src.config.settings import PDF_PATH, OUTPUT_PATH, VECTOR_STORE_PATH
from src.db.deeplake_store import DeeplakeStore
from src.pipeline.rag_pipeline import RAGPipeline
from src.utils.response_formatter import formatted_response

def chunk_text(text: str, chunk_size: int = 1000) -> list:
    """Splits the text into chunks of specified size."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

if __name__ == "__main__":
    pipeline = RAGPipeline(vector_store_path=VECTOR_STORE_PATH)
    user_prompt = input("Enter your query: ")
    gpt_response = pipeline.query(user_prompt)
    print(gpt_response)
