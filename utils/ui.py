from abc import ABC, abstractmethod

import streamlit as st


class Page(ABC):
    def page_links(self):
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
        
    @abstractmethod
    def write(self):
        pass