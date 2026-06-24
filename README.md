#  LangGraph AI Assistant

An AI-powered chatbot built using **LangGraph**, **LangChain**, **FastAPI**, and **Streamlit** with support for:

* Multiple LLM Providers (Groq & Google Gemini)
* Tool Calling
* Web Search using Tavily
* Conversational Memory
* FastAPI Backend
* Streamlit Frontend
* Thread-based Chat Sessions

---

##  Features

###  LangGraph Workflow

* Built using LangGraph's Graph API
* State-based architecture
* Tool routing with conditional edges
* Persistent conversation memory using MemorySaver

###  Multiple LLM Providers

Supported providers:

* Groq

  * llama-3.3-70b-versatile
* Google Gemini

  * gemini-2.5-flash
  * gemini-2.5-pro

### 🔍 Web Search

* Optional real-time web search using Tavily
* Tool calling handled automatically by LangGraph

###  Memory Support

* Uses LangGraph MemorySaver
* Maintains conversation history using Thread IDs

###  FastAPI Backend

* REST API endpoint for chat interactions
* Dynamic model selection

###  Streamlit Frontend

* User-friendly chat interface
* Provider selection
* Model selection
* Search toggle
* Thread ID support

---

##  Project Architecture

```text
User
 │
 ▼
Streamlit Frontend
 │
 ▼
FastAPI Backend
 │
 ▼
LangGraph
 │
 ├── Chatbot Node
 │
 ├── Tool Node
 │       │
 │       ▼
 │    Tavily Search
 │
 ▼
LLM (Groq / Gemini)
```

---

## 📂 Project Structure

```text
langgraph-chatbot/
│
├── ai_agent.py
├── backend.py
├── frontend.py
│
├── .env
├── .gitignore
│
├── pyproject.toml
├── uv.lock
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd langgraph-chatbot
```

---

### 2. Create Virtual Environment

Using UV:

```bash
uv venv
```

Activate Environment:

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
uv sync
```

or

```bash
uv add langgraph langchain langchain-core langchain-community langchain-groq langchain-google-genai tavily-python python-dotenv fastapi uvicorn streamlit typing-extensions
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

GOOGLE_API_KEY=your_google_api_key

TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Running the Application

### Start Backend

```bash
uv run python backend.py
```

Backend runs on:

```text
http://127.0.0.1:9999
```

Swagger Documentation:

```text
http://127.0.0.1:9999/docs
```

---

### Start Frontend

Open a new terminal:

```bash
uv run streamlit run frontend.py
```

Streamlit App:

```text
http://localhost:8501
```

---

## 🔄 LangGraph Workflow

```text
START
  │
  ▼
Chatbot Node
  │
  ▼
Need Tool?
  │
 ┌┴──────────┐
 │           │
Yes         No
 │           │
 ▼           ▼
Tool Node   END
 │
 ▼
Chatbot Node
 │
 ▼
END
```

---

##  Memory

This project uses:

```python
MemorySaver()
```

to persist conversation history.

Each conversation is identified by:

```python
thread_id
```

Example:

```text
Thread ID: 1
```

The chatbot remembers previous messages within the same thread.

---

##  API Usage

### POST /chat

Request:

```json
{
  "model_name": "llama-3.3-70b-versatile",
  "model_provider": "Groq",
  "message": "What is LangGraph?",
  "allow_search": true,
  "thread_id": "1"
}
```

Response:

```json
{
  "response": "LangGraph is a framework..."
}
```

---

## 🛠️ Technologies Used

### Backend

* FastAPI
* LangGraph
* LangChain

### LLMs

* Groq
* Google Gemini

### Tools

* Tavily Search

### Frontend

* Streamlit

### Environment

* UV Package Manager
* Python 3.11+

---

## 📚 Learning Objectives

This project demonstrates:

* LangGraph State Management
* Nodes & Edges
* Conditional Routing
* Tool Calling
* Memory Management
* FastAPI Integration
* Streamlit Integration
* Multi-LLM Support

---

##  Future Improvements

* Streaming Responses
* PDF Chat (RAG)
* Vector Database Integration
* Chat History Storage
* Multi-Agent Workflows
* Authentication
* Deployment on Render
* Docker Support

---

##  Author

**Saikat Tunga**

B.Tech Artificial Intelligence Student

Built as a hands-on project to learn:

* LangGraph
* LangChain
* FastAPI
* Streamlit
* Agentic AI Systems

```
```
