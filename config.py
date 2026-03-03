import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("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")
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
SIMILARITY_THRESHOLD = 0.90
VERIFIER_THRESHOLD = 0.75
