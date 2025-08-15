from typing import List, Dict, Any
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pinecone import Pinecone
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("PINECONE_API_KEY")
if not api_key:
    raise ValueError("PINECONE_API_KEY not found in environment variables.")

pc = Pinecone(api_key=api_key)
index_name = "news"

def process_url(urls):
    if isinstance(urls, str):
        urls = [urls]
    elif isinstance(urls, list):
        # Remove duplicates and ensure proper URL format
        urls = list(set(urls))  # Remove duplicates
        urls = [url for url in urls if url.strip()]  # Remove empty strings
        urls = [url if url.startswith(('http://', 'https://')) else 'https://' + url for url in urls]
    else:
        raise ValueError("URLs must be a string or list of strings")
        
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=300,
        chunk_overlap=50
    )

    docs = text_splitter.split_documents(data)
    embeddings = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")
    texts = [doc.page_content for doc in docs]
    vectors = embeddings.embed_documents(texts)
    
    index = pc.Index(index_name)
    
    to_upsert = []
    for i, (vector, text) in enumerate(zip(vectors, texts)):
        to_upsert.append({
            "id": f"chunk-{i}",
            "values": vector,
            "metadata": {
                "text": text,
                "url": urls[0]  # Use the first URL since we're processing one at a time
            }
        })
    
    batch_size = 100
    for i in range(0, len(to_upsert), batch_size):
        batch = to_upsert[i:i + batch_size]
        index.upsert(vectors=batch)

def predict(query:str):
    embeddings = HuggingFaceEmbeddings(model_name="all-mpnet-base-v2")
    query_vector = embeddings.embed_query(query)
    
    index = pc.Index(index_name)
    results: Any = index.query(
        vector=query_vector,
        top_k=3,
        include_metadata=True
    )
    
    answer = ""
    sources = []
    
    if results and results.matches:
        answer = " ".join([match.metadata.get("text", "") for match in results.matches])
        sources = [match.metadata.get("url", "") for match in results.matches]
    
    return {
        "answer": answer,
        "sources": sources
    }

if __name__=="__main__":
    process_url("https://en.wikipedia.org/wiki/Suzuki_Grand_Vitara_(2022)")
    result = predict("What is Grand Vitara?")
    print("\nAnswer:")
    print(result)
    