import streamlit as st

st.set_page_config(page_title="SentiScope", layout="centered")
st.title("👁️ SentiScope")
st.subheader("Welcome to the Sentiment Analysis App")
st.write("Use the sidebar to navigate between the **Logistic Regression** and **BERT** sentiment classifiers.")
st.write("You can **input a review** and view **prediction explanations** powered by model interpretability.")
