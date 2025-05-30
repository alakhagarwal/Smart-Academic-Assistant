import streamlit as st
from PyPDF2 import PdfReader

# Function to extract text from PDFs
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Streamlit app
st.title("PDF Text Extractor")

uploaded_files = st.file_uploader("Upload PDF file(s)", type="pdf", accept_multiple_files=True)

# 👇 Only show text if files are uploaded and button is clicked
if uploaded_files and st.button("Extract Text"):
    extracted_text = get_pdf_text(uploaded_files)
    st.subheader("Extracted Text:")
    st.write(extracted_text)
