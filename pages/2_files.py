import os
import base64
import tempfile
from pathlib import Path

import streamlit as st

from utils import (list_files, open_pdf, save_pdf)


def show_pdf(filename):
    bytes_pdf = open_pdf(filename)
    base64_pdf = base64.b64encode(bytes_pdf).decode("utf-8")
    st.write(
        f"""<embed src='data:application/pdf;base64,{base64_pdf}' 
        width='700' height='1000' 
        type='application/pdf'>""", 
        unsafe_allow_html=True
    )


# Sidebar content
with st.sidebar:
    st.title("Chat with Docs")
    
    st.page_link(page="pages/1_chat.py", label="聊天室")
    st.page_link(page="pages/2_files.py", label="文件")
    st.divider()

st.header("Files")

uploadfiles = st.file_uploader(
    "上傳檔案", 
    type=["txt", "pdf"], 
    accept_multiple_files=True,
)
if uploadfiles:
    save_paths = save_pdf(uploadfiles)
    st.success(save_paths)


files = list_files("/data")

if preview_pdf:=st.selectbox("預覽文件", [None]+files, placeholder="選擇要預覽的文件"):
    show_pdf(preview_pdf)
