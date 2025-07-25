import openai
from src.utils.logger import logger

def embedding_function(texts, model="text-embedding-3-small"):
    """Generates embeddings for the provided texts using the specified model."""
    logger.info("Generating embeddings for texts")
    if isinstance(texts, str):
        texts = [texts]
    texts = [text.replace("\n", " ") for text in texts]

    response = openai.embeddings.create(
        input=texts,
        model=model
    )

    return [data.embedding for data in response.data]
