print("Importing PyPDFLoader...")
from langchain_community.document_loaders import PyPDFLoader

print("Importing DirectoryLoader...")
from langchain_community.document_loaders import DirectoryLoader

print("Importing RecursiveCharacterTextSplitter...")
from langchain_text_splitters import RecursiveCharacterTextSplitter

print("Importing OpenAIEmbeddings...")
from langchain_openai import OpenAIEmbeddings

print("All imports succeeded.")

# Extract data from PDF

def load_pdf(data):
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    return documents


# Chunking the data
def chunk_data(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
        length_function=len
    )
    chunks = text_splitter.split_documents(documents)

    return chunks


# Create the embeddings model instance
def instantiate_embeddings():
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",
        dimensions=384
    )

    return embeddings