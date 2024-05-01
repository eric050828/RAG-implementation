import streamlit as st


# Sidebar content
with st.sidebar:
    st.title("Chat with Docs")

    st.page_link(page="pages/1_chat.py", label="聊天室")
    st.page_link(page="pages/2_files.py", label="文件")
    st.page_link(page="pages/3_web.py", label="網頁")
    st.divider()
    

url = st.text_input("網址")
submit = st.button("預覽")
if submit:
    st.markdown(f'<iframe src="{url}" width="100%" height="500" allowfullscreen></iframe>', unsafe_allow_html=True)