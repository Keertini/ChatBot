import streamlit as st
from PyPDF2 import PdfReader
import openai

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Chat function using OpenAI API (updated for openai>=1.0.0)
def chat_with_openai(api_key, context, user_question):
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Choose the appropriate model
            messages=[
                {"role": "system", "content": "You are an assistant that answers questions based on a PDF."},
                {"role": "user", "content": f"Context of the document: {context}"},
                {"role": "user", "content": user_question},
            ]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"

# Streamlit app layout
st.title("PDF Q&A Chatbot")
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

st.subheader("Upload a PDF File")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    st.subheader("Extracted PDF Content")
    pdf_text = extract_text_from_pdf(uploaded_file)
    st.text_area("Document Content", pdf_text, height=200)

    if api_key:
        st.subheader("Ask Questions About the PDF")
        user_question = st.text_input("Your question:")
        if st.button("Ask"):
            with st.spinner("Fetching answer..."):
                answer = chat_with_openai(api_key, pdf_text, user_question)
                st.success("Answer:")
                st.write(answer)
    else:
        st.warning("Please enter your OpenAI API key in the sidebar.")
