# Math Mentor  
An end-to-end AI system designed to solve JEE-style math problems reliably using:

- Retrieval-Augmented Generation (RAG)
- Multi-Agent Orchestration
- Multimodal Input (Text / Image / Audio)
- Human-in-the-Loop (HITL)
- Persistent Memory & Self-Learning

---
Live Link: https://math-mentorr-klshptokqbmtzvjjxpdn4k.streamlit.app/

# 🎯 Objective

Build a reliable AI application capable of:

- Solving JEE-level math problems
- Explaining solutions step-by-step
- Handling image, text, and audio input
- Reducing hallucination using RAG
- Improving over time using feedback memory
- Providing confidence scoring

---

# 🏗️ System Architecture

## High-Level Flow

User Input (Text / Image / Audio)  
↓  
Input Processing (OCR / ASR)  
↓  
Parser Agent  
↓  
Intent Router  
↓  
RAG Retrieval  
↓  
Solver Agent  
↓  
Verifier Agent  
↓  
Explainer Agent  
↓  
Memory Storage  
↓  
UI Output + Feedback  

---

# 🧩 Core Components

---

## 1️⃣ Multimodal Input Layer

The system supports:

### ✅ Text Input
User directly types math problem.

### ✅ Image Input
- OCR using EasyOCR
- Extracted text preview shown
- OCR confidence displayed
- Low confidence triggers HITL warning

### ✅ Audio Input
- Whisper speech-to-text
- Transcript preview shown
- Confidence indicator displayed
- Low transcription triggers warning

This ensures reliability before solving.

---

## 2️⃣ Parser Agent

The Parser Agent:

- Cleans OCR/ASR noise
- Identifies topic (Algebra / Calculus / Probability / Linear Algebra)
- Extracts variables
- Detects ambiguity
- Outputs structured JSON

Example output:

{
  "problem_text": "...",
  "topic": "algebra",
  "variables": ["x"],
  "constraints": [],
  "needs_clarification": false
}

If ambiguity is detected → HITL trigger.

---

## 3️⃣ RAG Pipeline

To reduce hallucination, the system uses Retrieval-Augmented Generation.

### Knowledge Base
Located in `/kb`:

- algebra.md
- calculus.md
- probability.md
- linear_algebra.md

### RAG Steps

1. Documents are chunked
2. Embedded using Sentence Transformers
3. Stored in FAISS vector store
4. Top-K relevant chunks retrieved per query
5. Retrieved context passed to Solver

Retrieved sources are shown in UI for transparency.

---

## 4️⃣ Multi-Agent System

The system uses 5 agents:

### 🔹 Parser Agent
Converts raw input into structured format.

### 🔹 Router Agent
Determines problem type and workflow.

### 🔹 Solver Agent
Generates solution using:
- Retrieved context
- LLM reasoning

### 🔹 Verifier Agent
Evaluates:
- Logical consistency
- Basic symbolic structure
- Assigns confidence score

### 🔹 Explainer Agent
Produces student-friendly step-by-step explanation.

### 🔹 Orchestrator
Controls full agent workflow and branching logic.

---

# 🔁 Human-in-the-Loop (HITL)

HITL is triggered when:

- OCR confidence is low
- ASR confidence is low
- Parser detects ambiguity
- Verifier confidence is low
- User marks answer incorrect

This ensures reliability and transparency.

---

# 🧠 Memory & Self-Learning

The system stores:

- Original problem
- Parsed structure
- Retrieved context
- Final solution
- Confidence score
- User feedback

Stored in SQLite (`memory.db`).

### Runtime Memory Usage

Before solving a new problem:

- System searches for similar past problems
- If similarity exceeds threshold:
  - Reuses solution pattern
  - Improves confidence estimation

This enables pattern reuse without model retraining.

---

# 📊 Confidence Scoring

Confidence is determined based on:

- Verifier score
- Retrieval quality
- Memory similarity reuse

Displayed as:

🟢 High Confidence  
🟡 Medium Confidence  
🔴 Low Confidence  

---

# 🖥️ UI Features

Built using Streamlit.

Includes:

- Input mode selector (Text / Image / Audio)
- OCR / ASR preview editor
- Agent trace panel
- Retrieved context panel
- Step-by-step solution display
- Confidence score display
- Feedback buttons (Correct / Incorrect)

---

# 📂 Project Structure

math-mentor/

├── app.py  
├── config.py  
├── requirements.txt  
├── .env.example  

├── agents/  
├── rag/  
├── memory/  
├── utils/  
├── kb/  

---

# 🚀 Installation & Setup

## 1️⃣ Clone Repository

git clone <your-repo-url>  
cd math-mentor  

## 2️⃣ Create Virtual Environment

python -m venv venv  
venv\Scripts\activate  

## 3️⃣ Install Dependencies

pip install -r requirements.txt  

## 4️⃣ Add Environment Variable

Create `.env` file:

GROQ_API_KEY=your_api_key_here  

## 5️⃣ Run Application

streamlit run app.py  

---

# 🌍 Deployment

The application can be deployed on:

- Streamlit Cloud
- HuggingFace Spaces
- Render
- Railway

Deployment requires:

- requirements.txt
- .env configuration
- Public GitHub repository

---

# ⚠ Limitations

- Symbolic reasoning relies primarily on LLM-based reasoning
- Very advanced Olympiad-level problems may require deterministic symbolic tools
- OCR accuracy depends on image clarity

Future improvements:

- Integrate SymPy-based deterministic math engine
- Advanced verification logic
- Enhanced combinatorics solver
- Stronger mathematical validation layer

---

# 🏆 Evaluation Summary

This system demonstrates:

- RAG-based grounding
- Multi-agent orchestration
- HITL integration
- Memory-based improvement
- Confidence-aware reasoning
- Transparent agent trace

It balances flexibility of LLM reasoning with structured reliability layers.

---

 
