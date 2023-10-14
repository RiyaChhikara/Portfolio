import streamlit as st
from load_css import local_css


st.set_page_config(
    page_title='Machine Learning',
    page_icon="👩"
)


local_css("css/style.css")

st.title("My portfolio")


st.markdown(
    """
    **Riya Chhikara**  
    Trainer (Data Science Tools)  
    """)

st.image("img/lse_dsl_logo.png", width=200)

st.markdown("---")

cols = st.columns(3)

with cols[1]:
    st.image("img/spotify.jpeg", width=150)

st.markdown(
    """
    This website provides an introduction to my work.

    Please select a page from the sidebar menu where you can find information about:
    - my explanations to code. Educational purpose 
    - Data Science 
    - Visualisations 
    - exploring Research papers 

    """)

