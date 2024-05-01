import streamlit as st


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
    

url = st.text_input("網址")
submit_btn = st.button("預覽")
if submit_btn:
    st.markdown(
        f'<iframe src="{url}" width="100%" height="500" allowfullscreen></iframe>', 
        unsafe_allow_html=True
    )