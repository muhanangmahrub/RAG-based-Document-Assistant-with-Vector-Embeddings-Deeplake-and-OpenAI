import os
from src.db.deeplake_store import DeeplakeStore
from src.models.openai_model import call_gpt4_with_full_text
from src.config.settings import PDF_PATH, OUTPUT_PATH
from src.data.data_prep import extract_text_from_pdf, chunk_text
from src.utils.logger import logger

class RAGPipeline:
    def __init__(self, vector_store_path: str):
        if os.path.exists(vector_store_path):
            logger.info(f"Using existing vector store at {vector_store_path}")
            self.store = DeeplakeStore(vector_store_path)
        else:
            logger.info(f"Creating new vector store at {vector_store_path}")
            extract_text_from_pdf(PDF_PATH, output_path=OUTPUT_PATH, start_page=12, end_page=79)
            source_text = OUTPUT_PATH
            with open(source_text, 'r', encoding='utf-8') as file:
                text_data = file.read()
            chunks = chunk_text(text_data)
            self.store = DeeplakeStore(vector_store_path)
            logger.info(f"Adding chunks to vector store from {source_text}")
            self.store.add_texts(chunks, source_text=source_text)

    def query(self, user_prompt: str) -> str:
        """Handles user queries by searching the vector store and generating a response."""
        logger.info(f"User query: {user_prompt}")
        search_results = self.store.search(user_prompt)
        logger.info(f"Search results: {search_results}")
        top_score = search_results['score'][0]
        top_text = search_results['text'][0]
        top_metadata = search_results['metadata'][0]

        augmented_input = f"{user_prompt} {top_text}"
        return call_gpt4_with_full_text(augmented_input)
    