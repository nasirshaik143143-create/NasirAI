import streamlit as st
import ollama
from pypdf import PdfReader
from docx import Document

st.set_page_config(
    page_title="NasirAI",
    page_icon="🤖"
)

st.title("🤖 NasirAI")

# File upload
uploaded_file = st.file_uploader(
    "Upload a file",
    type=["txt", "pdf", "docx"]
)

file_content = ""

if uploaded_file:

    if uploaded_file.type == "text/plain":
        file_content = uploaded_file.read().decode("utf-8")

    elif uploaded_file.type == "application/pdf":
        pdf = PdfReader(uploaded_file)
        for page in pdf.pages:
            file_content += page.extract_text()

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(uploaded_file)
        for para in doc.paragraphs:
            file_content += para.text


    st.success("File uploaded successfully!")

    st.text_area(
        "File content",
        file_content,
        height=200
    )


# Chat
if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


prompt = st.chat_input("Ask NasirAI about your file...")


if prompt:

    if file_content:
        prompt = f"""
        Use this file content to answer:

        {file_content}

        Question:
        {prompt}
        """

    st.session_state.messages.append(
        {"role":"user","content":prompt}
    )

    response = ollama.chat(
        model="llama3.2:latest",
        messages=st.session_state.messages
    )

    answer = response["message"]["content"]

    st.session_state.messages.append(
        {"role":"assistant","content":answer}
    )

    with st.chat_message("assistant"):
        st.write(answer)