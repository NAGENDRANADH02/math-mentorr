import os

def load_documents():
    docs = []
    kb_path = "kb"
    for file in os.listdir(kb_path):
        if file.endswith(".md"):
            with open(os.path.join(kb_path, file), "r", encoding="utf-8") as f:
                docs.append({"source": file, "content": f.read()})
    return docs