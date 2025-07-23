import openai

def embedding_function(texts, model="text-embedding-3-small"):
    if isinstance(texts, str):
        texts = [texts]
    texts = [text.replace("\n", " ") for text in texts]

    response = openai.embeddings.create(
        input=texts,
        model=model
    )

    return [data.embedding for data in response.data]
