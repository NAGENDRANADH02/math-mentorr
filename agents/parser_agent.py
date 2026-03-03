from groq import Groq
from config import GROQ_API_KEY
import json

client = Groq(api_key=GROQ_API_KEY)

def parse_problem(raw_text):
    prompt = f"""
Return STRICT JSON only:

{{
  "problem_text": "...",
  "topic": "algebra | calculus | probability | linear_algebra",
  "variables": [],
  "constraints": [],
  "needs_clarification": false,
  "clarification_question": ""
}}

Problem:
{raw_text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
    )

    try:
        return json.loads(response.choices[0].message.content)
    except:
        return {
            "problem_text": raw_text,
            "topic": "algebra",
            "variables": [],
            "constraints": [],
            "needs_clarification": False,
            "clarification_question": ""
        }