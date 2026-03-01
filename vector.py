from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv(r"C:\\Users\\Admin\\Desktop\\RAG Project\\Local AI Agent\\realistic_restaurant_reviews.csv") #Make sure to update the path to your CSV file
embeddings = OllamaEmbeddings(model = "mxbai-embed-large")

# Check if the Chroma database already exists to avoid adding documents multiple times
db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

# Create the Chroma vector store and add documents if the database does not already exist
if add_documents :
    documents = []
    ids = []
    for i, row in df.iterrows():
        document = Document(
            page_content = row['Title'] + " " + row['Review'],
            metadata = {"rating" : row['Rating'], "date": row['Date']},
            id=str(1)
        )
        ids.append(str(i))
        documents.append(document)

# Initialize the Chroma vector store with the specified collection name, persistence directory, and embedding function
vector_store = Chroma(collection_name = 'reviews', 
                      persist_directory = db_location,
                      embedding_function = embeddings
                    )

# Add documents to the vector store only if they have not been added before
if add_documents:
    vector_store.add_documents(documents, ids = ids)
    
# Create a retriever from the vector store with specified search parameters (e.g., number of results to return)
retriver = vector_store.as_retriever(
    search_kwargs = {"k": 5}
)