print("Importing load_pdf, chunk_data, instantiate_embeddings from src.helper...")
from src.helper import load_pdf, chunk_data, instantiate_embeddings
print("Successfully imported from src.helper.")

print("Importing PineconeGRPC from pinecone.grpc...")
from pinecone.grpc import PineconeGRPC as Pinecone
print("Successfully imported PineconeGRPC.")

print("Importing ServerlessSpec from pinecone...")
from pinecone import ServerlessSpec
print("Successfully imported ServerlessSpec.")

print("Importing PineconeVectorStore from langchain_pinecone...")
from langchain_pinecone import PineconeVectorStore
print("Successfully imported PineconeVectorStore.")

print("Importing os...")
import os
print("Successfully imported os.")

print("Importing load_dotenv from dotenv...")
from dotenv import load_dotenv
print("Successfully imported load_dotenv.")

print("✅ All imports completed successfully.")

load_dotenv()
print("✅ Environment variables loaded successfully.")

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
if PINECONE_API_KEY is None:
    raise ValueError("PINECONE_API_KEY not found in environment variables.")
else:
    print("✅ PINECONE_API_KEY found in environment variables.")

print("Loading PDF data...")
extract_data = load_pdf(data="Data/")
print("Data loaded successfully. Chunking...")
chunked_data = chunk_data(extract_data)
print("Data chunked successfully. Creating embeddings...")
embeddings = instantiate_embeddings()
print("✅ Data loaded and chunked successfully.")

pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
print("✅ Pinecone client initialized.")

index_name = "medibot-pinecone"

pc.create_index(
    name=index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)

# Embed each chunk from chunked_Data and store in Pinecone index
docsearch = PineconeVectorStore.from_documents(
    documents=chunked_data,
    index_name=index_name,
    embedding=embeddings,
)
