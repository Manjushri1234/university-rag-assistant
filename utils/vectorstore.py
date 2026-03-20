from langchain_community.vectorstores import FAISS
from utils.loaders import load_all_documents
from models.embeddings import get_embeddings


def create_vectorstore():
    documents = load_all_documents("data")
    embeddings = get_embeddings()

    vectorstore = FAISS.from_documents(documents, embeddings)

    # Save locally
    vectorstore.save_local("faiss_index")

    return vectorstore


def load_vectorstore():
    embeddings = get_embeddings()
    return FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
