import os
import streamlit as st
import requests
import pandas as pd
import time


def highlight_sentiment(val):
    """Function to highlight the sentiment column of our resulting dataframe
    in green (Positive) or red (Negative)"""

    if val == "Positive":
        color = '#d4edda'  # hellgrün
        text_color = '#155724'
    elif val == "Negative":
        color = '#f8d7da'  # hellrot
        text_color = '#721c24'
    else:
        color = 'white'
        text_color = 'black'
    return f'background-color: {color}; color: {text_color}'


st.title("📈 Batch analysis")

# Load API URI from secrets or environment
if "API_URI" in os.environ:
    BASE_URI = "https://sentiscope-811189409150.europe-west1.run.app/"
else:
    BASE_URI = st.secrets["cloud_api_uri"]
BASE_URI = BASE_URI if BASE_URI.endswith("/") else BASE_URI + "/"

# Adjust endpoint to batch route
url = BASE_URI + "predict_csv"

#Let the user upload a file
uploaded_file = st.file_uploader("Upload a CSV file with reviews", type="csv")

if uploaded_file:

    #Turn file to dataframe and display the head
    df = pd.read_csv(uploaded_file, index_col=0)
    st.write("Preview of uploaded data:")
    st.dataframe(df.head())

    #Once button is clicked, make API call to the batch endpoint
    if st.button("Predict Sentiments"):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")}
        with st.spinner("Sending review to API..."):
            response = requests.post(url, files=files)
            data = response.json()

        #Turn response to dataframe
        df= pd.DataFrame(data).set_index('id')

        #Highlight sentiment with colors
        styled_df = df.style.applymap(highlight_sentiment, subset=["predicted_sentiment"])

        #Display dataset with new sentiment column
        st.write("Sentiment Predictions:")
        st.dataframe(styled_df)

        #Download link
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download Results as CSV", csv, "predictions.csv", "text/csv")
