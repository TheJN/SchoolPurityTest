import streamlit as st
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    initial_sidebar_state="collapsed"
)
from functions import *


no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
        div[data-testid="stButton"] {display: flex; justify-content: center; align-items: center;}
        div[data-testid="element-container"] {display: flex; justify-content: center; align-items: center;text-align: center;}
        
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)


uri = "mongodb+srv://julienigou33:1bKqg3D0jDoTifwq@cluster0.txqupb2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()



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



# Pull data from the collection.
    # Uses st.cache_data to only rerun when the query changes or after 10 min.
def get_data():
    db = client.Survey_streamlit
    items = db.Survey.find()
    items = list(items)  # make hashable for st.cache_data
    return items



no_sidebar_style = """
    <style>

    .element-container .st-emotion-cache-1aege4m .e1f1d6gn4 p { font-size: 104px; }

    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)




#********************** PAGE *****************
def pageHome():

    # Instantiate session state variables
    instantiate_session_state_variables()
    st.session_state.setdefault('firstname', '')
    st.session_state.setdefault('lastname', '')
    st.session_state.setdefault('promo', '')
    st.session_state.setdefault('user_exist', False)

    items = get_data()

    st.header("Quel type d'étudiant es-tu ? ")

    st.write('Test toi afin de savoir si tu es considéré(e) comme un bon élève à ELISA Aerospace ')

    firstname = st.text_input("Prénom")
    lastname = st.text_input("Nom")

    option_promo = st.selectbox(
    "Quelle est ta promotion ?",
    ("Bachelor 1", "Bachelor 2", "Bachelor 3","Elisa 1 ","Elisa 2","Elisa 3","ELisa 4","Elisa 5","Alumni"))


    if firstname:
        st.session_state['firstname'] = firstname
        st.session_state['user_exist'] = False
    if lastname:
        st.session_state['lastname'] = lastname
        st.session_state['user_exist'] = False
        context = f"You are the game master of a purity test of the aerospace engeenering school. {firstname} {lastname} is about to play. Please Welcome the student with a funny quote in french."

        output = query({
            "inputs": context,
        })
        # Extract only the generated text from the response
        generated_text = output[0]["generated_text"][len(context):]

        st.write(generated_text)

    if option_promo:
        st.session_state['promo'] = option_promo

    for item in items:
        if st.session_state.firstname == item['firstname'] and st.session_state.lastname == item['lastname'] and st.session_state.promo == item['promo']:
            st.session_state['user_exist'] = True

        
    

    if st.button("Commencer le test"):
        if st.session_state['user_exist'] == True:
            st.subheader(':red[*------- Nom et prénom existant, changez -------*]')
        elif st.session_state['lastname'] and st.session_state['firstname']:
            st.switch_page("pages/1_Question.py")
        else:
           st.subheader(':red[*------- Vous devez remplir vos informations -------*]')

        

    

    # st.write("#### Le mur des réponses ")

    # cs_body()

pageHome()


