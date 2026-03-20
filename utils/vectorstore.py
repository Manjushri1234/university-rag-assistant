# TEMP VECTORSTORE (NO FAISS)

from .loaders import load_all_documents


def create_vectorstore():
    documents = load_all_documents("data")
    return documents


def load_vectorstore():
    return None
