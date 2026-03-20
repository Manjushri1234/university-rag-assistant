import streamlit as st
from utils.vectorstore import create_vectorstore, load_vectorstore
from models.llm import get_llm
from utils.rag_pipeline import run_rag
import os

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="University RAG Chatbot",
    page_icon="🎓",
    layout="wide"
)

# -------------------------------
# Header
# -------------------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>
    🎓 AI-Powered University Knowledge Assistant
    </h1>
    <p style='text-align: center;'>
    Ask anything about admissions, courses, fees, exams & more
    </p>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:
    st.title("📌 Menu")

    st.markdown("### 📖 About")
    st.write(
        "This chatbot uses RAG (Retrieval-Augmented Generation) "
        "to answer questions from university documents."
    )

    st.markdown("### 💡 Sample Questions")
    st.write("- What is MCA eligibility?")
    st.write("- What are MCA specializations?")
    st.write("- What is the fee structure?")
    st.write("- Who teaches AI subject?")
    st.write("- What are exam rules?")

    st.markdown("### ⚙️ Options")

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -------------------------------
# Load Vectorstore (SAFE MODE)
# -------------------------------
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = load_vectorstore()

    if st.session_state.vectorstore is None:
        st.warning("⚠️ Running in basic mode (no vector database)")

# -------------------------------
# Load LLM
# -------------------------------
if "llm" not in st.session_state:
    st.session_state.llm = get_llm()

# -------------------------------
# Chat History
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# -------------------------------
# User Input
# -------------------------------
query = st.chat_input("💬 Ask your question...")

if query:
    st.chat_message("user").write(query)
    st.session_state.messages.append({"role": "user", "content": query})

    # -------------------------------
    # SAFE RAG HANDLING
    # -------------------------------
    if st.session_state.vectorstore:
        answer = run_rag(query, st.session_state.vectorstore, st.session_state.llm)
    else:
        # fallback (no vector DB)
        response = st.session_state.llm(query)
        answer = response

    st.chat_message("assistant").write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
