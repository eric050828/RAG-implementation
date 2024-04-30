from time import sleep

import streamlit as st
from utils import (list_files, save_session, load_session, ROOT_DIR)


st.session_state.update(load_session())

# Sidebar content
with st.sidebar:
    st.title("Chat with Docs")

    st.page_link(page="pages/1_chat.py", label="聊天室")
    st.page_link(page="pages/2_files.py", label="文件")
    st.divider()

chat_title = st.empty()
chat_path = st.empty()

selected_chat = st.sidebar.selectbox("chats", st.session_state.chats.keys())
chat_title.header(selected_chat)

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

# Select file
files = list_files("/data")
if st.session_state.chats[selected_chat]["path"] != "":
    path = st.session_state.chats[selected_chat]["path"]
else:
    if selected_pdf:=st.sidebar.selectbox("選擇文件", [None]+files, placeholder="選擇參考文件"):
        path = f"{ROOT_DIR}\\data\\{selected_pdf}"
        st.session_state.chats[selected_chat]["path"] = path
chat_path.write(path)


save_session(st.session_state.to_dict())