from processor import VectorStore_Extractor
from processor import Compute_Response
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Web-Chat App", page_icon="custom_icon.png")
st.title("Web-Chat App")
website_url = st.text_input("Please enter a valid URL you wish to converse with:")
if website_url is None or website_url == "":
    st.info("Please enter a valid website URL to start the chat.")
else:
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hi there, I am the Web-Chat Bot. How can I help you today?"),
        ]
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = VectorStore_Extractor(website_url)
    user_query = st.chat_input("Type your message here...")
    if user_query:
        response = Compute_Response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)
footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    </style>
    <div class="footer">
        <p>Check out my GitHub portfolio: <a href="https://github.com/fouzan-akhter" target="_blank">fouzan-akhter</a></p>
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)
