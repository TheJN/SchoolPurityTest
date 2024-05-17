import streamlit as st
from functions import *
import plotly.graph_objects as go


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://julienigou33:1bKqg3D0jDoTifwq@cluster0.txqupb2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


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


def display_bar_chart(data):
    
    # Extracting values and indices
    values = list(int(val) for val in data.values())
    indices = list(data.keys())
    text = list(str(int(val))+'%' for val in data.values())

    # Define colors for each bar
    colors = ['blue', 'green', 'red','purple','yellow']

    # Creating the bar plot
    fig = go.Figure(data=[go.Bar(x=indices, y=values, text=text, textposition='auto', marker_color=colors)])

    # Updating layout
    fig.update_layout(title='Répartition des résultats par catégorie',
                    xaxis_title='Catégorie',
                    yaxis_title='Pourcentage',
                    xaxis=dict(tickvals=list(range(len(indices))), ticktext=indices))

    # Display plot using Streamlit
    st.plotly_chart(fig, use_container_width=True)



import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	


def pageConclusion():
    st.markdown("""
    <style>
    .conclusion-font {
        font-size:50px !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f'<p class="conclusion-font">Résultat du test : </p>', unsafe_allow_html=True)

    data_survey = st.session_state

    score_by_cat = calculate_category_scores(data_survey)
    max_score = calculate_max_scores(survey_categories)

    pourcentage_score = convert_keys_to_categories(calculate_percentage(score_by_cat, max_score))

    global_score = '0%' if calculate_average_percentage(pourcentage_score) <0 else str(int(calculate_average_percentage(pourcentage_score)))+'%'

    

    st.markdown("""
    <style>
    .big-font {
        font-size:150px !important;
        color: lightblue !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f'<p class="big-font">{global_score}</p>', unsafe_allow_html=True)

    context = f"I'm a student at the Elisa Aerospace school of aeronautical engineering. I just took a purity test at my school and got {global_score} overall, with {pourcentage_score} for each category. Can you tell me what kind of student I am? Use the tone of humor and respond in french with two sentences please. "

    output = query({
	"inputs":f"I'm a student at the Elisa Aerospace school of aeronautical engineering. I just took a purity test at my school and got {global_score} overall, with {pourcentage_score} for each category. Can you tell me what kind of student I am? Use the tone of humor and respond in french with two sentences please. ",
    })

    generated_text = output[0]["generated_text"][len(context):]

    st.subheader(body='Quel étudiant es tu ?')
    st.write(generated_text)
    
    display_bar_chart(pourcentage_score)

    items = get_data()

    database_score_per_cat = convert_keys_to_categories(combine_data(*[calculate_percentage(calculate_category_scores(item['scores']),max_score) for item in items]))        

    fig = go.Figure()

    # Create scatter plots for each category
    for category, values in database_score_per_cat.items():
        fig.add_trace(go.Scatter(x=[category]*len(values), y=values, mode='markers', name=f"{category}"))
    
    # Add the single point
    for category, value in pourcentage_score.items():
        fig.add_trace(go.Scatter(x=[category], y=[value], mode='markers', name="Mes réponses", marker=dict(color="yellow")))


    fig.update_layout(title="Comparaison de mes réponses avec les réponses des autres étudiants",
                    xaxis_title="Catégorie",
                    yaxis_title="Valeur")
    st.plotly_chart(fig, use_container_width=True)



pageConclusion()