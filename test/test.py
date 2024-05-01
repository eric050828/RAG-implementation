import os

import streamlit as st


st.session_state["test"] = {
    "data": [
        {"0": 0}, 
        {"1": 1}
    ]
}

test = st.session_state.test

st.write(st.session_state)

test.update({"data": [{"2": 2}]})

st.write(st.session_state)
