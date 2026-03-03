import sqlite3

conn = sqlite3.connect("memory.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS problems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    input TEXT,
    parsed TEXT,
    solution TEXT,
    confidence REAL,
    feedback TEXT
)
""")
conn.commit()

def save_memory(input_text, parsed, solution, confidence, feedback=""):
    cursor.execute(
        "INSERT INTO problems (input, parsed, solution, confidence, feedback) VALUES (?, ?, ?, ?, ?)",
        (input_text, parsed, solution, confidence, feedback),
    )
    conn.commit()

def fetch_all():
    cursor.execute("SELECT input, solution FROM problems")
    return cursor.fetchall()