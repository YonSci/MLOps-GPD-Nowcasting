import streamlit as st

page_icon = "images\logo4.jpg"

st.set_page_config(
    page_title="Main Page",
    page_icon=page_icon,
    layout="centered"  # wide, centered
    )

# Function to create session state

   
from app.Landing_Page import Landing_Page
from app.GT_Data_Downloader_Module import GT_Data_Downloader_Module
from app.GDP_Preprocessing_Module import GDP_Preprocessing_Module 
from app.GT_Preprocessing_Module import GT_Preprocessing_Module 
from app.Feature_Engineering import Feature_Engineering
from app.Model_Development_Evaluation import Model_Development_Evaluation
from app.Visualization_Interpretation import Visualization_Interpretation

def main():
    st.sidebar.title("Navigation Bar")
    
    pages = {
        "Landing Page": Landing_Page,
        "Google Trend Data Downloader Module": GT_Data_Downloader_Module,
        "GDP Preprocessing Module": GDP_Preprocessing_Module, 
        "GT Preprocessing Module": GT_Preprocessing_Module,
        "Feature Engineering": Feature_Engineering,
        "Model Development Evaluation": Model_Development_Evaluation, 
        "Visualization Interpretation": Visualization_Interpretation, 
    }
    
    choice = st.sidebar.selectbox("Go to", list(pages.keys()))
    

    # Instantiate the chosen class
    selected_page = pages[choice]()
    
    
if __name__ == "__main__":
    main()
