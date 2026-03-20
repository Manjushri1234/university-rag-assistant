import streamlit as st
from groq import Groq


def get_llm():
    api_key = st.secrets["GROQ_API_KEY"]   # ✅ correct

    client = Groq(api_key=api_key)

    def generate_response(prompt):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    return generate_response
