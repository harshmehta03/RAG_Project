from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

# Path to your PDF
pdf_path = r"C:\Users\Admin\Desktop\RAG Project\Local AI Agent\Robotics.pdf"

# Load PDF
loader = PyPDFLoader(pdf_path)
documents = loader.load()

# Split the PDF into chunks (important for RAG)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = text_splitter.split_documents(documents)

# Initialize embeddings (Ollama local embedding model)
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Vector DB location
db_location = "./chroma_langchain_db"

# Check if DB already exists
add_documents = not os.path.exists(db_location)

# Initialize Chroma vector store
vector_store = Chroma(
    collection_name="pdf_collection",
    persist_directory=db_location,
    embedding_function=embeddings
)

# Add documents only if database is new
if add_documents:
    vector_store.add_documents(docs)

# Create retriever
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)
