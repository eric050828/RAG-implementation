from time import sleep

import streamlit as st


def stream_test(prompt):
    for s in f"(stream) you said: {prompt}":
        sleep(0.1)
        yield s

with st.sidebar:
    st.title("Chat with Docs")

    st.page_link(page="pages/1_chat.py", label="聊天室")
    st.page_link(page="pages/2_files.py", label="文件")


st.header("Chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    
    st.chat_message("user").markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"you said: {prompt}"
    stream_response = stream_test(prompt)
    with st.chat_message("assistant"):
        st.write(response)
        st.write_stream(stream_response)
        
    st.session_state.messages.append({"role": "assistant", "content": "".join(response)})
