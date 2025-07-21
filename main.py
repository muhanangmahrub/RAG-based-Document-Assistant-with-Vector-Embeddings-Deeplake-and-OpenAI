from src.data.data_prep import extract_text_from_pdf
from src.config.settings import PDF_PATH, OUTPUT_PATH, VECTOR_STORE_PATH
from src.db.deeplake_store import DeeplakeStore

def chunk_text(text: str, chunk_size: int = 1000) -> list:
    """Splits the text into chunks of specified size."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

if __name__ == "__main__":
    extract_text_from_pdf(
        pdf_path=PDF_PATH,
        output_path=OUTPUT_PATH,
        start_page=12,
        end_page=79
    )

    source_text = OUTPUT_PATH
    with open(source_text, 'r', encoding='utf-8') as file:
        text = file.read()
    chunks = chunk_text(text)

    vector_store_path = VECTOR_STORE_PATH
    store = DeeplakeStore(vector_store_path)
    store.add_texts(chunks, source_text)

    user_prompt = input("Enter your search query: ")
    results = store.search(user_prompt, top_k=3)
    print("Search Results: ", results)