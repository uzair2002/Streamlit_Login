import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import base64

# hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

import streamlit as st
st.set_page_config(layout="wide",initial_sidebar_state="collapsed")

hide_sidebar="""
<style>
.stDeployButton{
    visibility:hidden;
}

.st-emotion-cache-g0dirf.eczjsme1a{
    visibility:hidden;
}

#MainMenu{
    visibility:hidden;
}


</style>
"""
st.markdown(hide_sidebar,unsafe_allow_html=True)



page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://r4.wallpaperflare.com/wallpaper/998/592/1023/red-triangles-low-poly-low-poly-art-wallpaper-48661d4810307c88a01c511e9822548a.jpg");
background-size: 120%;
background-position: center;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

</style>
"""
def Signup_button():
    st.header("New Here ?")
    st.text(f"Ready to analyze your data with AI?\nSign in here to access our EDA website.")
    
    st.button("Go to Signup", on_click=switch_page)



# Step 1: Read configuration from YAML file
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

# Initialize session state variable for page number
if "page" not in st.session_state:
    st.session_state.page = "login"

# Function to switch to the next page
def switch_page():
    if st.session_state.page == "login":
        st.session_state.page = "signup"
    else:
        st.session_state.page = "login"

# Render content based on the current page
if st.session_state.page == "login":
    buff,login_columns,buff,SignupButton_column,buff=st.columns([1,5,1,2,1])
    # Step 3: Call login widget
    with login_columns: 
        authenticator.login()
        # Step 4: Authenticate users
        if "authentication_status" in st.session_state:        
            if st.session_state["authentication_status"]:
                st.sidebar.markdown("<div style='margin-bottom:750px;'></div>", unsafe_allow_html=True)
                st.sidebar.write(f'Welcome *{st.session_state["name"]}*')
                authenticator.logout("Logout", "sidebar")
                st.title('Some content')
                st.markdown("""<style>
                .st-emotion-cache-g0dirf.eczjsme1{
                visibility:visible;
                }
                 </style>
                 """,unsafe_allow_html=True)
            
            elif st.session_state["authentication_status"] is False:
                #st.markdown(page_bg_img, unsafe_allow_html=True)
                st.error('Username/password is incorrect')

            elif st.session_state["authentication_status"] is None:
                #st.markdown(page_bg_img, unsafe_allow_html=True)
                st.info('Please enter your username and password')
    with SignupButton_column:
        if st.session_state["authentication_status"] is False or st.session_state["authentication_status"] is None:
            Signup_button()

    

elif st.session_state.page == "signup":
    #st.markdown(page_bg_img, unsafe_allow_html=True)
    buff,LoginButton_column,buff,Signup_columns,buff=st.columns([1,2,1,5,1])
    with Signup_columns:
        # Step 6: Create a new user registration widget
        try:
            email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False)
            if email_of_registered_user:
                st.success('User registered successfully')
        except Exception as e:
            st.error(e)
    with LoginButton_column:
        st.header("Already have an account? ")
        st.text("Let's get started! Please log in to continue.")
        st.button("Go to Login", on_click=switch_page)




# tab1, tab2 = st.tabs(["login", "register u ser"])
# with tab1:



    # # Step 7: Create a forgot password widget
    # try:
    #     username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
    #     if username_of_forgotten_password:
    #         st.success('New password to be sent securely')
    #         # The developer should securely transfer the new password to the user.
    #     elif username_of_forgotten_password == False:
    #         st.error('Username not found')
    # except Exception as e:
    #     st.error(e)

    # # Step 8: Create a forgot username widget
    # try:
    #     username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username()
    #     if username_of_forgotten_username:
    #         st.success('Username to be sent securely')
    #         # The developer should securely transfer the username to the user.
    #     elif username_of_forgotten_username == False:
    #         st.error('Email not found')
    # except Exception as e:
    #     st.error(e)


# Step 10: Update the configuration file
with open('data.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)




