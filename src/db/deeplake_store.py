from deeplake.core.vectorstore.deeplake_vectorstore import VectorStore
from src.models.embedding_model import embedding_function

class DeeplakeStore:
    def __init__(self, vector_store_path: str):
        self.vector_store = VectorStore(vector_store_path)

    def add_texts(self, texts, source_text: str):
        self.vector_store.add(
            text=texts,
            embedding_function=embedding_function,
            embedding_data=texts,
            metadata=[{"source": source_text}] * len(texts)
        )
        print(f"Added {len(texts)} texts to the vector store from {source_text}")

    def search(self, query: str, top_k: int = 3):
        results = self.vector_store.search(
            embedding_data=query,
            embedding_function=embedding_function
        )
        return results