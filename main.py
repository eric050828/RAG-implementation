import streamlit as st

from utils import Page


class App(Page):
    def write(self):
        self.page_links()
        with open("README.md", "r", encoding="utf-8") as f:
            st.markdown(f.read())

if __name__ == "__main__":
    app = App()
    app.write()