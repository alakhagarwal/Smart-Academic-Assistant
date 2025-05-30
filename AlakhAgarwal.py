import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from PyPDF2 import PdfReader
from langchain_community.document_loaders import PyPDFLoader
from langchain_core import load


def  get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf) #gives an reader object
        for page in pdf_reader.pages: #pdf_reader.pages is the list of all pages in a particular pdf
            text+=page.extract_text() #gets the content from each page of the selected pdf
    return text
# -------------------- Page Configuration --------------------
st.set_page_config(page_title="Smart Academic Assistant", layout="centered")

# -------------------- Title --------------------
st.title("📚 Smart Academic Assistant")
st.write("Upload your academic documents and ask questions to get structured answers.")

# -------------------- File Upload Section --------------------
uploaded_files = st.file_uploader(                 #considering the user uploads only one file
    "Upload academic documents PDF:",
    type=["pdf"],
    accept_multiple_files=True
)

# -------------------- Question Input --------------------
question = st.text_input("Enter your academic question:")

# -------------------- Submit Button --------------------
if st.button("Get Answer"):
    if not uploaded_files or not question:
        st.warning("Please upload at least one document and enter a question.")
    else:
         extracted_text = get_pdf_text(uploaded_files)  
        



        # 2. Split documents using RecursiveCharacterTextSplitter or similar
        # 3. Create embeddings and store in vector store (e.g., FAISS, Chroma)
        # 4. Retrieve relevant chunks based on the question
        # 5. Use Groq-hosted LLM via LangChain (e.g., Mixtral, Gemma, Llama3)
        # 6. Use Output Parser to format structured response

        # Example output format (replace this with actual output):
        # response = {
        #     "question": question,
        #     "answer": "Your answer here",
        #     "source_document": "Document Name",
        #     "confidence_score": "0.93"
        # }
        #
        # st.subheader("📄 Answer:")
        # st.json(response)

    st.info(extracted_text)

# -------------------- Bonus Section: Agent Tools --------------------
st.markdown("---")
st.subheader("🧠 Bonus Tools ( Optional )")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Summarize Document"):
        # TODO: Implement SummarizeDocumentTool using LangChain agent
        st.info("Summary will be shown here.")

with col2:
    if st.button("Generate MCQs"):
        # TODO: Implement GenerateMCQsTool using LangChain agent
        st.info("Generated MCQs will appear here.")

with col3:
    if st.button("Topic-wise Explanation"):
        # TODO: Implement TopicWiseExplanationTool using LangChain agent
        st.info("Topic-wise explanation will be displayed here.")

# -------------------- Footer --------------------
st.markdown("---")
st.caption("Mentox Bootcamp · Final Capstone Project · Phase 1")
