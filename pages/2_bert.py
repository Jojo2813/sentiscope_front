import os
import streamlit as st
import requests
from utils.visualization import visualize_input_importance

st.title("📈 BERT")
st.title("Sentiment Analysis")

# Load API URI from secrets or environment
if "API_URI" in os.environ:
    BASE_URI = "https://sentiscope-811189409150.europe-west1.run.app/"
else:
    BASE_URI = st.secrets["cloud_api_uri"]
BASE_URI = BASE_URI if BASE_URI.endswith("/") else BASE_URI + "/"

# Adjust endpoint to logistic route
url = BASE_URI + "text_dl"

# Create user input box
user_input = st.text_input("Enter a review:")
params = {"text": user_input}

# Display result
if st.button("Analyze sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a review.")
    else:
        try:
            response = requests.post(url, json=params)
            if response.status_code == 200:
                data = response.json()
                prediction = data["sentiment"]
                contrib_dict = data.get("contributions", {})
                top_positive = data.get("top_positive", [])
                top_negative = data.get("top_negative", [])

                st.success(f"**Predicted sentiment:** `{prediction}`")

                if contrib_dict:
                    st.markdown("#### 🔍 Word Importance Visualization")
                    html_vis = visualize_input_importance(user_input, contrib_dict, top_positive, top_negative)
                    st.markdown(html_vis, unsafe_allow_html=True)
                else:
                    st.info("No word-level contribution data available.")
            else:
                st.error(f"API request failed with status code {response.status_code}")
        except Exception as e:
            st.error(f"Error contacting the API: {e}")
