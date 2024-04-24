import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
    
def check_login():
    #if st.session_state["authentication_status"]:

        with open('data.yaml') as file:
            config = yaml.load(file, Loader=SafeLoader)


        # Step 2: Create an authenticator object
        authenticator = stauth.Authenticate(
            config['credentials'],
            config['cookie']['name'],
            config['cookie']['key'],
            config['cookie']['expiry_days'],
            config['preauthorized']
        )

        st.sidebar.markdown("<div style='margin-bottom:600px;'></div>", unsafe_allow_html=True)
        st.sidebar.write(f'Welcome *{st.session_state["name"]}*')
        authenticator.logout("Logout", "sidebar")
        if not st.session_state["authentication_status"]:
            st.switch_page("main.py")

        