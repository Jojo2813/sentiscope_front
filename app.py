import streamlit as st
from PIL import Image

st.set_page_config(page_title="SentiScope", layout="centered")
col1, col2 = st.columns([1, 4])

with col1:
    st.image("assets/logo.png", width=150)

with col2:
    st.markdown("## SentiScope\n*Visual Sentiment Analysis for Reviews*")

st.subheader("Welcome to the Sentiment Analysis App")
st.write("Use the sidebar to navigate between the **Logistic Regression** and **BERT** sentiment classifiers.")
st.write("You can **input a review** and view **prediction explanations** powered by model interpretability.")
