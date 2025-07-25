import fitz
import re
from src.utils.logger import logger

def clean_text(text: str) -> str:
    """Cleans the input text by removing specific patterns and unnecessary whitespace.
    Args:
        text (str): The input text to be cleaned.
    Returns:
        str: The cleaned text.
    """
    text = re.sub(r'\[\d+\]', '', text)
    lines = text.splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip() != ""]
    return "\n".join(cleaned_lines)

def extract_text_from_pdf(pdf_path: str, output_path: str, start_page: int = 12, end_page: int = 20) -> None:
    """Extracts text from a PDF file and saves it to a text file.
    Args:
        pdf_path (str): The path to the PDF file.
        output_path (str): The path where the output text file will be saved.
        start_page (int): The starting page number for extraction (default is 12).
        end_page (int): The ending page number for extraction (default is 20).
    """
    doc = fitz.open(pdf_path)
    pages = [page.get_text() for page in doc]
    with open(output_path, 'w', encoding='utf-8') as file:
        for page in pages[start_page:end_page]:
            text_page = clean_text(page)
            file.write(text_page + "\n")
    logger.info(f"Text extracted from {start_page} to {end_page} pages and saved to {output_path}")
    

def chunk_text(text: str, chunk_size: int = 1000) -> list:
        """Splits the text into chunks of specified size."""
        return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]