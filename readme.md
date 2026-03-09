# RAG Project (Retrieval-Augmented Generation)

This project demonstrates a basic implementation of a Retrieval-Augmented Generation (RAG) pipeline using Python.  
It loads documents, creates vector embeddings, stores them in a vector database, and retrieves relevant context to answer user queries using an LLM.

---

## 📂 Project Structure
RAG_Project/
│
├── chroma_langchain_db/ # Vector database storage
├── venv/ # Python virtual environment (not pushed to GitHub)
├── main.py # Main application logic
├── vector.py # Vector creation and retrieval logic
├── realistic_restaurant_reviews.xlsx # Sample dataset
├── requirements.txt # Project dependencies
└── README.md # Project documentation


---

## 🚀 Features

- Loads documents from a dataset (Excel/PDF/text)
- Converts documents into embeddings
- Stores embeddings in a vector database (Chroma/FAISS)
- Retrieves relevant context for user queries
- Integrates with LLM for question answering

---

## 🛠️ Tech Stack

- Python
- LangChain
- Chroma / FAISS
- OpenAI / HuggingFace embeddings
- Pandas
- Vector Database

---

## ⚙️ Installation

1. Clone the repository:
git clone https://github.com/harshmehta03/RAG_Project.git


2. Create and activate virtual environment:
python -m venv venv
venv\Scripts\activate


3. Install dependencies:
pip install -r requirements.txt

---

## ▶️ How to Run
Add you manual/document to the WD.
Change The directory in the vector.py to your document.
Run python main.py in terminal.

---

## 📌 Use Case

- Question answering on custom documents
- AI chatbot with knowledge base
- Semantic search over datasets

---

## 📜 License

This project is for learning and experimentation purposes.
