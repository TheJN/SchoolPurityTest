import streamlit as st
from functions import *
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://julienigou33:1bKqg3D0jDoTifwq@cluster0.txqupb2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
        div[data-testid="stButton"] {display: flex; justify-content: center; align-items: center;}
        div[data-testid="stVerticalBlockBorderWrapper"] {display: flex; justify-content: center; align-items: center;    height: 100vh;          flex-direction: column; text-align: center; }
        div[data-testid="stRadio"]{display: flex; justify-content: center; align-items: center;}
        div[data-testid="stMarkdown"] {display: flex; justify-content: left; align-items: left;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return client

client = init_connection()

def page3():

    categories = list(survey_categories.keys())

    categories_index = 6
    selected_category = categories[categories_index-1]  # You can change this to display different categories

    display_category(category=selected_category)

        # add to database

    bool_scores = check_category_scores(categories_index,extract_scores(st.session_state))
    bool_completed_score = all(value for value in bool_scores.values())


    if st.button(label=" Voir mes résultats "):
        if bool_completed_score:

            scores = extract_scores(st.session_state)
            # {str(key): value for key, value in calculate_category_scores(st.session_state).items()}
            mydict = {'firstname':st.session_state.firstname,'lastname':st.session_state.lastname,'scores':scores}
            
            st.write(mydict)

            db = client.Survey_streamlit
            db.Survey.insert_one(mydict)
            st.switch_page("pages/Conclusion.py")
        else:
            st.subheader(':red[*------- Vous devez répondre à toute les questions -------*]')
        
        
        

        

page3()