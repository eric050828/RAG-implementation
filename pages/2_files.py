import os
import base64

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

    pages = [
        ("聊天室", "pages/1_chat.py"),
        ("文件", "pages/2_files.py"),
        ("網頁", "pages/3_web.py")
    ]
    for label, page in pages:
        st.page_link(page=page, label=label)
    st.divider()

st.header("Files")

uploadfiles = st.file_uploader(
    "上傳檔案", 
    type=["txt", "pdf"], 
    accept_multiple_files=True,
)
if uploadfiles:
    save_paths = save_pdf(uploadfiles)
    st.success(f"已儲存 {len(save_paths)} 個檔案。")


files = list_files("/uploads")

if preview_pdf:=st.selectbox("預覽文件", files, index=None, placeholder="選擇要預覽的文件"):
    show_pdf(preview_pdf)
