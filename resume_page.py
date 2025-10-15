import streamlit as st

def resume_page():
    st.title("My Resume")
    st.write("Below is a detailed overview of my experience, education, and skills.")

    # Image code
    image_path = "project pic.jpeg"  
    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(image_path, use_container_width=True)  # Fixed parameter

    with col2:
        # Experience Section
        st.header("Experience")
        st.write("""
        **Freelancer – Upwork**  
        - Currently working on various data science and machine learning projects.  

        **ICCBS**  
        _Research Intern – Karachi, Pakistan_  
        Jan 2020 – Aug 2020  
        - Processed and analyzed large datasets for biological research projects.  
        - Used Python scripts to clean and transform raw data.  
        - Enhanced database structure for efficient data retrieval.  
        """)

        # Education Section
        st.header("Education")
        st.write("""
        **MS in Data Science**  
        _Eastern University – Saint Davids, PA_  
        May 2023 – Present  
        - Relevant Coursework: Data Engineering, Cloud Computing, Machine Learning  

        **BS in Bioinformatics**  
        _Sir Syed University of Engineering and Technology – Karachi, Pakistan_  
        2018 – 2022  
        - Relevant Coursework: Database Systems, Data Structures, Algorithms, Python Programming  
        """)

        # Technical Skills Section
        st.header("Technical Skills")
        st.write("""
        - **Programming Languages:** Python, SQL, R, C, C++  
        - **Data Engineering Tools:** Pandas, NumPy, PySpark, Apache Hadoop (Basics)  
        - **Databases:** MySQL, PostgreSQL, MongoDB  
        - **Data Visualization Tools:** Power BI, Tableau  
        - **Cloud Platforms:** Microsoft Azure (Basics)  
        """)

        # Projects Section
        st.header("Projects")
        st.write("""
        **Translating Egyptian Hieroglyphs Using Deep Learning**  
        - A deep learning project focused on deciphering and translating ancient Egyptian hieroglyphs.  

        **Student Performance Prediction System**  
        - Developed a predictive model to assess and forecast student academic performance based on historical data and behavioral patterns.  
        """)

        # Certifications Section
        st.header("Certifications")
        st.write("""
        - Google Data Analytics (Ongoing)  
        - IBM Data Science (Ongoing)  
        - Complete SQL Bootcamp (Udemy)  
        """)
