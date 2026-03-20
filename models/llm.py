from langchain_groq import ChatGroq
from config.config import GROQ_API_KEY


def get_llm():
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model="llama-3.1-8b-instant",
        temperature=0.3
    )
