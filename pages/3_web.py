import streamlit as st

from utils import Page

    
class WebPage(Page):
    def write(self):
        self.page_links()
        url = st.text_input("網址")
        submit_btn = st.button("預覽")
        if submit_btn:
            st.markdown(
                f'<iframe src="{url}" width="100%" height="500" allowfullscreen></iframe>', 
                unsafe_allow_html=True
            )


if __name__ == "__main__":
    web_page = WebPage()
    web_page.write()