import streamlit as st


with st.sidebar:
    st.sidebar.title("Chat with Docs")
    
    st.sidebar.page_link(page="pages/1_chat.py", label="聊天室")
    st.sidebar.page_link(page="pages/2_files.py", label="文件")
    

st.header("Introduction")