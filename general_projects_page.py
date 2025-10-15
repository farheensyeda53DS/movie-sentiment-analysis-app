import streamlit as st

def general_projects_page():
    st.title("General Projects")
    
    # Note Section
    st.markdown("### Note")
    st.write("""
    **** No links are provided as these projects are private.****
    """)

    # Project 1
    st.header("Project 1: Translating Egyptian Hieroglyphs Using Deep Learning")
    st.write("""
    As my final year project in my BS program, I developed a real-time object detection system using the Single Shot Detection (SSD) 
    algorithm to detect and translate Egyptian hieroglyphs. The primary goal was to provide tourists with an affordable alternative 
    to hiring local guides for understanding hieroglyphs. The application works as a pocket translator, allowing users/tourists to point their 
    camera at hieroglyphs and translate Egyptian Hieroglyphs in real-time.
    
    **Challenges and Solutions:**
    - **Dataset Creation:** Used Gardiner’s List to create a custom dataset and applied data augmentation techniques to expand the dataset size.
    - **Algorithm Selection:** Chose SSD for its balance of speed and accuracy after experimenting with RCNN and YOLO.
    - **Performance Testing:** Achieved high accuracy and effective translations through iterative training and fine-tuning.
    """)

    # Project 2
    st.header("Project 2: Student Performance Prediction System")
    st.write("""
    As part of a program focused on learning Machine Learning, I created a predictive system to analyze student performance based 
    on historical academic data. The system uses features like attendance, grades, and participation records to predict students' 
    performance in upcoming exams, enabling teachers to identify students who might need additional support.
    
    **Development Summary:**
    - Cleaned and pre-processed a sample dataset to handle missing and inconsistent data.
    - Implemented a Random Forest Classifier for its robustness and ability to handle mixed data types.
    - Created an interactive dashboard to visualize predictions and performance.
    """)
