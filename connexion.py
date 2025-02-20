import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import pandas as pd

# User data in the correct format
user_data = pd.read_csv('user_data.csv')

lesDonneesDesComptes = {'usernames': {}}

for _, row in user_data.iterrows():
    lesDonneesDesComptes['usernames'][row['username']] = {
        'name': row['name'],
        'password': row['password'],
        'email': row['email'],
        'failed_login_attemps': 0,  # Managed automatically
        'logged_in': False,  # Managed automatically
        'role': row['role']
    }

# Create the authenticator instance
authenticator = Authenticate(
    lesDonneesDesComptes,  # User data
    "cookie_name",  # Cookie name
    "cookie_key",  # Cookie key
    30  # Expiry time for the cookie (in days)
)

# Login logic
def login():
    authenticator.login()

def accueil():
    # If the user is logged in
    if st.session_state.get("authentication_status"):
        user_name = st.session_state["name"]            
        
        # Sidebar for navigation options
        with st.sidebar:
            # Display a logout button
            authenticator.logout("Déconnexion")
            st.title(f"Welcome {user_name}")
            selection = option_menu(
                menu_title=None,
                options=["👾 Accueil", "💁‍♀️ Photos"])
            
        if selection == "👾 Accueil":
            st.title(f"Bienvenue sur le contenu réservé aux utilisateurs connectés, {user_name} :smile:")
            st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHB2bjNueWh0aDJ0cGV0YXR5MmR5aW1sd3V2MGcxdTNpMWsxdWFqMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Rlwz4m0aHgXH13jyrE/giphy.gif",
                 width=400)
        elif selection == "💁‍♀️ Photos":
            st.title("Ha! you've been trapped, here are some cat memes")
            col1, col2, col3 = st.columns(3, gap='large')
            with col1:
                st.image("https://i.chzbgr.com/full/9380397568/h30A8D494/what-if",
                        width=250)
            with col2:
                st.image("https://i.chzbgr.com/full/9380382976/hB72C23D9/it-must-be-friday-by-now",
                        width=250)
            with col3:
                st.image("https://i.chzbgr.com/full/9381991424/h11236647/one-hour-late",
                        width=250)
    # If the user is not logged in
    elif st.session_state.get("authentication_status") is False:
        st.error("L'username ou le password est/sont incorrect")
    
    # If the login attempt was not made
    elif st.session_state.get("authentication_status") is None:
        st.warning("Les champs username et mot de passe doivent être remplis")

# Run login function and then display the main content
login()
accueil()
