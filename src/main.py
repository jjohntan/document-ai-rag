from src.parser import parse_arg, extract_text_from_pdf
from src.chunking import chunk_by_char
from src.vector_store import VectorStore
from src.gen_prompt import generate_prompt
from google import genai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

st.title("Document AI RAG")


# uploaded_file = st.file_uploader("Choose a file", type=["pdf"], accept_multiple_files=False)
# if uploaded_file is not None:
#     text = extract_text_from_pdf(uploaded_file)

prompt = st.chat_input(
    "Say something and/or attach an image",
    accept_file=True,
    file_type=["pdf"],
)

if prompt and prompt["files"]:
    text = extract_text_from_pdf(prompt["files"][0])
    st.write(text)
    chunks = chunk_by_char(text)
    retriever = VectorStore(chunks)
    retriever.encode_similarity()
    
if prompt and prompt.text:
    st.markdown(prompt.text)
# result = retriever.search(prompt.text)

# def main() -> None:
#     arg = parse_arg()

#     # user_query = arg.prompt

#     text = extract_text_from_pdf(arg.pdf_path)
#     chunks = chunk_by_char(text)
#     retriever = VectorStore(chunks)
#     retriever.encode_similarity()
#     result = retriever.search(user_query)
#     # print(f'search result: {result}')
#     prompt = generate_prompt(user_query, result)
#     # print(f'prompt: {prompt}')
#     client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#     interaction = client.interactions.create(
#     model=os.getenv("MODEL"),

#     input=prompt
#     )
#     print(interaction.output_text)


# if __name__ == "__main__":
#     main()
