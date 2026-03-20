import streamlit as st
from utils.vectorstore import load_vectorstore
from models.llm import get_llm
import os

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="AI-Powered Jain University Information Chatbot",
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
        "This chatbot answers questions from university documents."
    )

    st.markdown("### 💡 Sample Questions")
    st.write("- What is MCA eligibility?")
    st.write("- What are MCA specializations?")
    st.write("- What is the fee structure?")
    st.write("- Who teaches AI subject?")
    st.write("- What are exam rules?")

    # 🔥 NEW: RESPONSE MODE
    st.markdown("### 🧠 Response Mode")

    mode = st.radio(
        "Choose how you want answers:",
        ["Concise ⚡", "Detailed 📘"],
        index=1
    )

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -------------------------------
# 🔥 SHOW CURRENT MODE (TOP)
# -------------------------------
st.markdown(
    f"""
    <div style='text-align:center; margin-bottom:10px;'>
        <span style='background-color:#4CAF50; color:white; padding:6px 12px; border-radius:12px;'>
        Mode: {mode}
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Load Vectorstore (SAFE MODE)
# -------------------------------
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = load_vectorstore()

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

    # 🔥 NEW: MODE-BASED PROMPT
    if "Concise" in mode:
        final_query = "Give a short, crisp answer in 3-4 points: " + query
    else:
        final_query = "Give a detailed answer with headings, bullet points, and explanation: " + query

    # ✅ LLM call
    answer = st.session_state.llm(final_query)

    st.chat_message("assistant").write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
