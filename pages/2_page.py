import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import sys
sys.path.append('..')
from authenticator import check_login 

# if st.button("Go Home"):
#     st.switch_page("main.py")

st.set_page_config(layout="wide",initial_sidebar_state="expanded")


if "authentication_status" in st.session_state:
    if st.session_state["authentication_status"]:
        check_login()
        st.write("page 2")
       

    else:
        st.write("Please [Log in](main) to get started!!")