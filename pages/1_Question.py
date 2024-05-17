import streamlit as st
from functions import *


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


def page1():

    categories = list(survey_categories.keys())
    categories_index = 1
    selected_category = categories[categories_index-1]  # You can change this to display different categories
  
    display_category(selected_category)

    bool_scores = check_category_scores(1,extract_scores(st.session_state))
    bool_completed_score = all(value for value in bool_scores.values())
   

    if st.button(label="Questions suivantes"):
        if bool_completed_score:
            st.switch_page("pages/2_Question2.py")
        else:
            st.subheader(':red[*------- Vous devez répondre à toute les questions -------*]')

page1()