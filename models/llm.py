import streamlit as st
from groq import Groq


def get_llm():
    # Get API key from Streamlit Secrets
    api_key = st.secrets["GROQ_API_KEY"]

    client = Groq(api_key=api_key)

    def generate_response(prompt):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI-powered university assistant. "
                        "Answer questions clearly, in a structured format with bullet points or numbering. "
                        "Keep answers concise but informative. "
                        "If applicable, explain step-by-step. "
                        "Focus on admissions, courses, eligibility, fees, exams, and academic topics."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    return generate_response
