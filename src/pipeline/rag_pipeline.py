from src.db.deeplake_store import DeeplakeStore
from src.models.openai_model import call_gpt4_with_full_text

class RAGPipeline:
    def __init__(self, vector_store_path: str):
        self.store = DeeplakeStore(vector_store_path)

    def query(self, user_prompt: str) -> str:
        search_results = self.store.search(user_prompt)
        top_score = search_results['score'][0]
        top_text = search_results['text'][0]
        top_metadata = search_results['metadata'][0]

        augmented_input = f"{user_prompt} {top_text}"
        gpt_response = call_gpt4_with_full_text(augmented_input)
        return gpt_response