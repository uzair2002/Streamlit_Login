import streamlit as st




if "authentication_status" in st.session_state:
    if st.session_state["authentication_status"]:
        st.header("page 2")

    else:
        st.write("please login")