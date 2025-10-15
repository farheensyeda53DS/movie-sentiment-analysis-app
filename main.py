import streamlit as st
from resume_page import resume_page
from sentiment_analysis_page import sentiment_analysis_page
from general_projects_page import general_projects_page
from biography_page import biography_page

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a Tab", 
    ["Biography", "DTSC 691 Project", "Resume", "General Projects"]
)

# Routing logic code 
if page == "Biography":
    biography_page()
elif page == "DTSC 691 Project":
    sentiment_analysis_page()
elif page == "Resume":
    resume_page()
elif page == "General Projects":
    general_projects_page()
