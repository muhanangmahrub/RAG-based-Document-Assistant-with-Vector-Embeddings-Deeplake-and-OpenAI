from src.data.data_prep import extract_text_from_pdf
from src.config.settings import PDF_PATH, OUTPUT_PATH

if __name__ == "__main__":
    extract_text_from_pdf(
        pdf_path=PDF_PATH,
        output_path=OUTPUT_PATH,
        start_page=12,
        end_page=79
    )