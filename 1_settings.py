import streamlit as st



import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

if "authentication_status" in st.session_state:
    if st.session_state["authentication_status"]:
        
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.title('Some content')
        st.header("page 1")
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

        st.sidebar.markdown("<div style='margin-bottom:800px;'></div>", unsafe_allow_html=True)
        st.sidebar.write(f'Welcome *{st.session_state["name"]}*')
        authenticator.logout("Logout", "sidebar")

        # Step 5: Create a reset password widget
    
        try:
            if authenticator.reset_password(st.session_state.get("username", "")):
                st.success('Password modified successfully')
        except Exception as e:
            st.error(e)

        # Step 9: Create an update user details widget
        # if "authentication_status" in st.session_state:
        #     if st.session_state["authentication_status"]:
        try:
            if authenticator.update_user_details(st.session_state.get("username", "")):
                st.success('Entries updated successfully')
        except Exception as e:
            st.error(e)



        # Step 10: Update the configuration file
        with open('data.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)



    else:
        st.write("please login")