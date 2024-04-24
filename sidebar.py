import streamlit as st
def Sidebar_Title():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
      
            }
            [data-testid="stSidebarNav"]::before {
                content: "AI Based EDA";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;

            }
        </style>
        """,
        unsafe_allow_html=True,
    )
# Hide sidebar and deploy button
def hide_sidebar_and_deploy_button():
    hide_sidebar_css = """
    <style>
    .stDeployButton {
        visibility: hidden;
    }
    .st-emotion-cache-g0dirf.eczjsme1 {
        visibility: hidden;
    }
    #MainMenu {
        visibility: hidden;
    }
    </style>
    """
    st.markdown(hide_sidebar_css, unsafe_allow_html=True)
