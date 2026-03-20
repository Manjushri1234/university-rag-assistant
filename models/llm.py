import os
from groq import Groq


def get_llm():
    api_key = os.getenv("GROQ_API_KEY")

    print("DEBUG KEY:", api_key)  # 👈 ADD THIS

    if not api_key:
        raise ValueError("GROQ_API_KEY not found!")

    client = Groq(api_key=api_key)

    def generate_response(prompt):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful university assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content

    return generate_response
