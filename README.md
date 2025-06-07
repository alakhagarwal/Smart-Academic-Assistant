# 📚 Your Study-Buddy

Your Study-Buddy is a multi-document academic Q&A assistant built with [Streamlit](https://streamlit.io/), [LangChain](https://www.langchain.com/), and [Groq LLMs](https://groq.com/). Upload academic PDFs, ask questions, generate summaries, MCQs, and topic-wise explanations—all in one place.

---

## 🚀 Features

- Upload and process multiple academic PDF documents
- Ask context-aware academic questions
- Generate:
  - 📄 Document summaries
  - 📝 Multiple Choice Questions (MCQs)
  - 📚 Topic-wise explanations
- Choose from various LLMs (LLaMA, Gemma, etc.)
- Customize temperature and max token limit

---

## 📦 Installation

1. Clone the repository

git clone https://github.com/your-username/your-study-buddy.git
cd your-study-buddy

2. Install dependencies

pip install -r requirements.txt

3 . 🔐 Environment Variables
Create a .env file in the root directory and add your API key:

GROQ_API_KEY=your_api_key_here

4. 🧠 How to Run

streamlit run main.py


## 🧰 Tech Stack

Streamlit — frontend web app framework

LangChain — chaining logic and prompt engineering

Groq LLMs — fast and powerful language models

FAISS — vector similarity search

HuggingFace Embeddings — semantic vector encoding

PyPDF2 — PDF text extraction

## 🧑‍💻 Author
Developed with 💻 by Alakh Agarwal
