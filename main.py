import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from authenticator import set_page_background_image,read_configuration,create_authenticator,initialize_session_state,render_content, update_configuration
from sidebar import hide_sidebar_and_deploy_button,Sidebar_Title
# Set page configuration
def set_page_configuration():
    st.set_page_config(layout="wide", initial_sidebar_state="collapsed")


def main():
    set_page_configuration()
    Sidebar_Title()
    hide_sidebar_and_deploy_button()
    set_page_background_image()
    config = read_configuration()
    authenticator = create_authenticator(config)
    initialize_session_state()
    render_content(config, authenticator)
    if "authentication_status" in st.session_state:
        if st.session_state["authentication_status"]:
            st.write("heloooooo")
    update_configuration(config)

if __name__ == "__main__":
    main()
