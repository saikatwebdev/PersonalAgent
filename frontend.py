import streamlit as st
import requests

st.set_page_config(
    page_title="Saikat-Agent",
    layout="wide"
)

st.title("Personal AI Assistant")

API_URL = "http://127.0.0.1:9999/chat"


# SIDEBAR


with st.sidebar:

    provider = st.selectbox(
        "Provider",
        ["Groq", "Google"]
    )

    if provider == "Groq":

        model = st.selectbox(
            "Model",
            [
                "llama-3.3-70b-versatile"
            ]
        )

    else:

        model = st.selectbox(
            "Model",
            ["gemini-2.5-flash"]
        )

    allow_search = st.checkbox(
        "Enable Web Search"
    )

    thread_id = st.text_input(
        "Thread ID",
        value="1"
    )


# CHAT HISTORY


if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# USER INPUT


if prompt := st.chat_input(
    "Ask me anything..."
):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    payload = {

        "model_name": model,
        "model_provider": provider,
        "message": prompt,
        "allow_search": allow_search,
        "thread_id": thread_id
    }

    response = requests.post(
        API_URL,
        json=payload
    )

    result = response.json()

    assistant_reply = result["response"]

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )