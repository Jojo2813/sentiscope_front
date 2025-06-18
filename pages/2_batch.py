import os
import streamlit as st
import requests
import pandas as pd
import time


def highlight_sentiment(val):
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

# Adjust endpoint to logistic route
url = BASE_URI + "text_ml"

uploaded_file = st.file_uploader("Upload a CSV file with reviews", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, index_col=0)

    st.write("Preview of uploaded data:")
    st.dataframe(df.head())

    if st.button("Predict Sentiments"):
        results = []
        with st.spinner("Sending review to API..."):
            for review in df["text"]:
                response = requests.post(url, json={"text": review})
                data = response.json()
                sentiment = data['Sentiment']
                results.append(sentiment)

        df["predicted_sentiment"] = results

        # Farbliche Hervorhebung der Spalte
        styled_df = df.style.applymap(highlight_sentiment, subset=["predicted_sentiment"])

        st.write("Sentiment Predictions:")
        st.dataframe(styled_df)

        # Optional: Download link
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download Results as CSV", csv, "predictions.csv", "text/csv")
