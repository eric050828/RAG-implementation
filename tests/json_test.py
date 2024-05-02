import json

import streamlit as st


st.write(st.session_state)
# st.session_state["message"] = []
if st.button("load"):
    # st.session_state.clear()
    with open(".config\\session.json", "r") as f:
        st.session_state.update(json.loads(f.read()))
if st.button("save"):
    with open(".config\\session.json", "w") as f:
        f.write(json.dumps(st.session_state.to_dict()))
#     for key, value in st.session_state:
