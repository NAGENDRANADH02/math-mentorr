import streamlit as st
from rag.knowledge_loader import load_documents
from rag.embedder import Embedder
from rag.retriever import Retriever
from memory.memory_store import save_memory, fetch_all
from memory.memory_retriever import search_similar
from agents.orchestrator import run_pipeline
from utils.ocr import extract_text_from_image
from utils.asr import transcribe_audio
from utils.normalizer import normalize_math_text

st.set_page_config(page_title="Multimodal Math Mentor", layout="wide")

st.title("🧠 Reliable Multimodal Math Mentor")

# -------------------------------
# INPUT MODE
# -------------------------------

mode = st.selectbox("Select Input Mode", ["Text", "Image", "Audio"])

raw_input = ""
confidence = None

# -------------------------------
# TEXT INPUT
# -------------------------------

if mode == "Text":
    raw_input = st.text_area("Enter math problem")

# -------------------------------
# IMAGE INPUT (OCR)
# -------------------------------

elif mode == "Image":
    image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

    if image:
        with open("temp.png", "wb") as f:
            f.write(image.read())

        raw_input, confidence = extract_text_from_image("temp.png")

        st.write(f"🔍 OCR Confidence: {confidence:.2f}")

        if confidence < 0.85:
            st.warning("⚠ Low OCR confidence detected. Please review carefully.")

        raw_input = st.text_area("OCR Preview (edit if needed)", raw_input)

# -------------------------------
# AUDIO INPUT (ASR)
# -------------------------------

elif mode == "Audio":
    audio = st.file_uploader("Upload Audio", type=["wav", "mp3"])

    if audio:
        with open("temp.wav", "wb") as f:
            f.write(audio.read())

        raw_input, confidence = transcribe_audio("temp.wav")

        st.write(f"🎤 Transcription Confidence: {confidence:.2f}")

        if confidence < 0.7:
            st.warning("⚠ Low transcription confidence detected.")

        raw_input = st.text_area("Transcript Preview (edit if needed)", raw_input)

# Normalize text (important for math phrases)
if raw_input:
    raw_input = normalize_math_text(raw_input)

# -------------------------------
# SOLVE BUTTON
# -------------------------------

if st.button("🚀 Solve"):

    if not raw_input.strip():
        st.error("Please enter a valid math problem.")
        st.stop()

    # -------------------------------
    # BUILD RAG INDEX
    # -------------------------------

    docs = load_documents()
    embedder = Embedder()

    doc_embeddings = embedder.embed([d["content"] for d in docs])
    retriever = Retriever(doc_embeddings, docs)

    query_embedding = embedder.embed([raw_input])
    retrieved = retriever.search(query_embedding)

    context_text = "\n\n".join([r["content"] for r in retrieved])

    # -------------------------------
    # MEMORY SEARCH
    # -------------------------------

    past_data = fetch_all()
    memory_hit = search_similar(raw_input, past_data)

    # -------------------------------
    # RUN AGENT PIPELINE
    # -------------------------------

    result = run_pipeline(raw_input, context_text, memory_hit)

    # -------------------------------
    # HANDLE CLARIFICATION (HITL)
    # -------------------------------

    if "clarification" in result:
        st.warning("🤖 Clarification Required:")
        st.info(result["clarification"])
        st.stop()

    # -------------------------------
    # DISPLAY SOLUTION
    # -------------------------------

    st.subheader("📘 Solution")
    st.markdown(result["explanation"])

    # -------------------------------
    # CONFIDENCE
    # -------------------------------

    st.subheader("📊 Confidence Score")

    score = result["confidence"]

    if score >= 0.85:
        st.success(f"High Confidence: {score:.2f}")
    elif score >= 0.7:
        st.warning(f"Medium Confidence: {score:.2f}")
    else:
        st.error(f"Low Confidence: {score:.2f}")

    # -------------------------------
    # AGENT TRACE
    # -------------------------------

    st.subheader("🔎 Agent Trace")
    for step in result["trace"]:
        st.write("✔", step)

    # -------------------------------
    # RETRIEVED CONTEXT PANEL
    # -------------------------------

    st.subheader("📚 Retrieved Context")
    for r in retrieved:
        st.write(f"Source: {r['source']} | Score: {r['score']:.2f}")
        st.write(r["content"])
        st.markdown("---")

    # -------------------------------
    # SAVE MEMORY
    # -------------------------------

    save_memory(
        raw_input,
        str(result["parsed"]),
        result["solution"],
        result["confidence"]
    )

    # -------------------------------
    # USER FEEDBACK (HITL)
    # -------------------------------

    st.subheader("🧑‍🏫 Feedback")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Correct"):
            save_memory(
                raw_input,
                str(result["parsed"]),
                result["solution"],
                result["confidence"],
                "correct"
            )
            st.success("Feedback saved as correct.")

    with col2:
        if st.button("❌ Incorrect"):
            save_memory(
                raw_input,
                str(result["parsed"]),
                result["solution"],
                result["confidence"],
                "incorrect"
            )
            st.success("Feedback saved as incorrect.")