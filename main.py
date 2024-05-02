import streamlit as st

from utils import Page


class App(Page):
    def write(self):
        self.page_links()
        st.header("Introduction")

if __name__ == "__main__":
    app = App()
    app.write()