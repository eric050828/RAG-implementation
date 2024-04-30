import streamlit as st


# Sidebar content
with st.sidebar:
    st.title("Chat with Docs")
    
    st.page_link(page="pages/1_chat.py", label="聊天室")
    st.page_link(page="pages/2_files.py", label="文件")
    

st.header("Introduction")