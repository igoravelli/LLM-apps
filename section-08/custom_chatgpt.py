from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import streamlit as st
from streamlit_chat import message


import sys
sys.path.append("../packages")
from functions import instantiate_llm, set_env_variables

set_env_variables()



st.set_page_config(
    page_title="Your custom Assistant", 
    page_icon=":robot:"
)
st.subheader("ChatGPT style!")

chat = ChatOpenAI(model_name = 'gpt-3.5-turbo', temperature=0.5)
if 'messages' not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    system_message = st.text_input(label='System Role')
    user_prompt = st.text_input(label='Send a message')

    if system_message:
        if not any(isinstance(m, SystemMessage) for m in st.session_state.messages):
            st.session_state.messages.append(
                SystemMessage(content=system_message)
            )

    if user_prompt:
        st.session_state.messages.append(
            HumanMessage(content=user_prompt)
        )
    
        with st.spinner('Generating response..'):
            response = chat(st.session_state.messages)
        
        st.session_state.messages.append(AIMessage(content=response.content))

st.session_state.messages