import streamlit as st
from utils import (empty_chat, list_files, save_session, load_session, ROOT_DIR)


st.session_state.update(load_session())

# Sidebar content
with st.sidebar:
    st.title("Chat with Docs")

    st.page_link(page="pages/1_chat.py", label="聊天室")
    st.page_link(page="pages/2_files.py", label="文件")
    st.page_link(page="pages/3_web.py", label="網頁")
    st.divider()

# Chat
chat_title = st.empty()
chat_path = st.empty()
chats = st.session_state.chats.keys()

# New chat
if st.sidebar.button("New chat", use_container_width=True):
    new_chat_title = f"Chat {len(chats) + 1}"
    new_chat = empty_chat(new_chat_title)
    st.session_state.chats.update(new_chat)

# Select chat
col1, col2 = st.sidebar.columns([3, 1])
selected_chat = col1.selectbox("chats", chats)
chat_title.header(selected_chat)

# Chat Delete
if col2.button("Delete", type="primary"):
    del st.session_state.chats[selected_chat]
    if not st.session_state.chats.keys():
        st.session_state.chats.update(empty_chat("Chat1"))
    selected_chat = list(st.session_state.chats.keys())[0]
    
# Chat rename
col1, col2 = st.sidebar.columns([3, 1])
new_chat_name = col1.text_input("new name")
if col2.button("Rename") and new_chat_name is not None:
    st.session_state.chats[new_chat_name] = st.session_state.chats[selected_chat]
    del st.session_state.chats[selected_chat]
    selected_chat = new_chat_name
    

st.sidebar.divider()

# Chat history
for message in st.session_state.chats[selected_chat]["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Select file
path = ""
if st.session_state.chats[selected_chat]["path"] != "":
    path = st.session_state.chats[selected_chat]["path"]

files = list_files("/data")
col1, col2 = st.sidebar.columns([3, 1])
selected_pdf = col1.selectbox("選擇文件", files, index=None, placeholder="選擇參考文件")
submit_btn = col2.button("上傳")
if submit_btn and selected_pdf is not None:
    path = f"{ROOT_DIR}\\data\\{selected_pdf}"
    st.session_state.chats[selected_chat]["path"] = path

chat_path.write(path)

# React to user input
if prompt := st.chat_input("What is up?"):
    
    st.chat_message("user").markdown(prompt)
    
    st.session_state.chats[selected_chat]["messages"].append({"role": "user", "content": prompt})

    response = f"you said: {prompt}"
    with st.chat_message("assistant"):
        st.write(response)
        
    st.session_state.chats[selected_chat]["messages"].append({"role": "assistant", "content": "".join(response)})



save_session(st.session_state.to_dict())