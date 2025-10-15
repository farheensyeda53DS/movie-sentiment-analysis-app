import streamlit as st

def biography_page():
    st.title("Biography")
    st.write("Learn more about me, my academic journey, and career aspirations!")

    # Introduction Section
    st.header("Introduction")
    st.write("""
    Hello! My name is Farheen Ali, and thank you for visiting my Streamlit page.
    I am currently pursuing my Master’s in Data Engineering at Eastern University, Saint Davids, PA.
    With a passion for building scalable and efficient data systems, I am deeply invested in the field of Data Engineering.
    I love tackling challenges related to data for analysis and machine learning applications.
    
    When I’m not immersed in coding or designing data workflows, I enjoy exploring innovative projects and staying updated on the latest trends in big data and cloud technologies.
    I also love to travel, try new foods from different countries, and spend quality time with my family, which enriches my perspective and creativity.
    """)

    # Academic Background Section
    st.header("Academic Background")
    st.write("""
    After completing my Bachelor’s in Bioinformatics from Sir Syed University of Engineering and Technology, Karachi,
    I developed a strong foundation in database systems, programming, and data structures.
    My undergraduate thesis on machine learning applications introduced me to the transformative power of data, inspiring me to specialize further in Data Engineering.

    Currently, as a Master’s student, I am expanding my expertise in ETL pipelines, big data processing, and cloud platforms.
    My academic and professional journey has given me a holistic understanding of the data lifecycle management and its critical role in driving business decisions.
    """)

    # Professional Interests Section
    st.header("Professional Interests and Career Aspirations")
    st.write("""
    I am particularly drawn to the field of Data Engineering, where I aspire to design and implement high-performance data pipelines and data warehouse solutions that enable seamless data accessibility.
    My interests include working with big data technologies, optimizing cloud-based data architectures, and creating robust data workflows to support machine learning and analytics platforms.
    """)
