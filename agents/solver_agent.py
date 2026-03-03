from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def solve(problem_text, context):
    prompt = f"""
Use the context below to solve step-by-step.

Context:
{context}

Problem:
{problem_text}
"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content