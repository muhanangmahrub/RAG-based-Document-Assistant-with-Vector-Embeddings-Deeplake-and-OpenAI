import gradio as gr
from src.pipeline.rag_pipeline import RAGPipeline
from src.utils.logger import logger
from src.utils.response_formatter import formatted_response
from src.config.settings import VECTOR_STORE_PATH


VECTOR_STORE_PATH = VECTOR_STORE_PATH
pipeline = RAGPipeline(vector_store_path=VECTOR_STORE_PATH)

def rag_chat_interface(user_input, history):
    """Handles user input and returns the response from the RAG pipeline."""
    logger.info(f"User input: {user_input}")
    response_stream = pipeline.query(user_prompt=user_input)
    full_response = ""
    for token in response_stream:
        full_response += token
        yield full_response

def create_gradio_interface():
    """Creates and launches the Gradio interface for the RAG pipeline."""
    with gr.Blocks() as demo:
        gr.Markdown("# RAG-based Document Assistant")
        gr.Markdown("This application uses a Retrieval-Augmented Generation (RAG) pipeline to assist with document queries.")
        gr.ChatInterface(
            rag_chat_interface,
            title="RAG Document Assistant",
            description="Ask questions about the document, and the system will provide answers based on the content.",
            chatbot=gr.Chatbot(label="Chat History"),
            # inputs=gr.Textbox(label="Your Question", placeholder="Type your question here..."),
            # outputs=gr.Textbox(label="Response", placeholder="The assistant's response will appear here..."),
            theme="default"
        )
        demo.launch()

if __name__ == "__main__":
    logger.info("Starting Gradio interface for RAG-based Document Assistant")
    create_gradio_interface()
    logger.info("Gradio interface launched successfully")