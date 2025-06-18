import streamlit as st


#Front page
st.set_page_config(page_title="SentiScope", layout="centered")
col1, col2 = st.columns([1, 4])

#Set logo and Header
with col1:
    st.image("assets/logo.png", width=150)
with col2:
    st.markdown("## SentiScope\n*Visual Sentiment Analysis for Reviews*")

#This line is used to seperate text blocks
st.markdown("<br>", unsafe_allow_html=True)

#Create Greeting and navigation
st.subheader("Welcome to the Sentiment Analysis App")
st.markdown("""Use the [prediction page](https://sentiscope.streamlit.app/about)
            to choose between **Logistic Regression** and **BERT** sentiment
            classifiers.""")
st.markdown("""You can **input a review** and view **prediction explanations**
         powered by model interpretability.""")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""Use the [batch page](https://sentiscope.streamlit.app/batch)
            to upload  csv file containing multiple reviews and get a sentiment
            prediction on all of them at once.""")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""Use the [about page](https://sentiscope.streamlit.app/about)
            to learn about the
         models and learning""")
