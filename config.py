import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("")
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
SIMILARITY_THRESHOLD = 0.90
VERIFIER_THRESHOLD = 0.75