from time import sleep

import streamlit as st
from utils import save_session, load_session


st.session_state.update(load_session())

with st.sidebar:
    st.title("Chat with Docs")

    st.page_link(page="pages/1_chat.py", label="聊天室")
    st.page_link(page="pages/2_files.py", label="文件")
    st.divider()

st.header("Chat")

selected_chat = st.sidebar.selectbox("chats", st.session_state.chats.keys())

for message in st.session_state.chats[selected_chat]["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    
    st.chat_message("user").markdown(prompt)
    
    st.session_state.chats[selected_chat]["messages"].append({"role": "user", "content": prompt})

    response = f"you said: {prompt}"
    with st.chat_message("assistant"):
        st.write(response)
        
    st.session_state.chats[selected_chat]["messages"].append({"role": "assistant", "content": "".join(response)})

save_session(st.session_state.to_dict())