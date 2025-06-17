import streamlit as st
from PIL import Image
import os
import streamlit as st
import requests
from utils.visualization import visualize_input_importance

#Page for predictions and comparison
st.title("Sentiment Analysis")

# Create user input box
user_input = st.text_area(
    "Enter your review:",
    height=200,  # passt die Höhe an
    placeholder="Paste or type a long review here..."
)

#ML part
st.title("📈 Logistic Regression")

# Load API URI from secrets or environment
if "API_URI" in os.environ:
    BASE_URI = "https://sentiscope-811189409150.europe-west1.run.app/"
else:
    BASE_URI = st.secrets["cloud_api_uri"]
BASE_URI = BASE_URI if BASE_URI.endswith("/") else BASE_URI + "/"

# Display result if button is clicked
if st.button("Analyze sentiment with Logistic Regression"):

    #Create placeholders for sentiment and visualizing
    sentiment_placeholder = st.empty()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    header_placeholder = st.empty()
    logistic_viz_placeholder = st.empty()

    st.markdown("<br>", unsafe_allow_html=True)

    # Adjust endpoint to logistic route
    url = BASE_URI + "text_ml"

    #Prepare parameters
    params = {"text": user_input}

    #Check if input is correct
    if user_input.strip() == "":
        sentiment_placeholder.error("Please enter a review.")
    else:
        try:
            #Get the prediction from the api and display it
            response = requests.post(url, json=params)
            if response.status_code == 200:
                data = response.json()
                prediction = data["Sentiment"]
                contrib_dict = data.get("contributions", {})
                top_positive = data.get("top_positive", [])
                top_negative = data.get("top_negative", [])

                if prediction.lower() == "positive":
                    sentiment_placeholder.markdown(
                        "<div style='padding:10px; background-color:#eaffe3; \
                            color:#33c800; border-radius:10px;'>"
                        "✅ <strong>Sentiment: Positive</strong></div>",
                        unsafe_allow_html=True
                    )
                elif prediction.lower() == "negative":
                    sentiment_placeholder.markdown(
                        "<div style='padding:10px; background-color:#ffe0e0; \
                            color:#d20000; border-radius:10px;'>"
                        "❌ <strong>Sentiment: Negative</strong></div>",
                        unsafe_allow_html=True
                    )
                else:
                    sentiment_placeholder.info("Sentiment could not be determined.")

                if contrib_dict:
                    header_placeholder.markdown("#### 🔍 Word Importance Visualization")
                    html_vis = visualize_input_importance(user_input, \
                        contrib_dict, top_positive, top_negative)
                    logistic_viz_placeholder.markdown(html_vis, unsafe_allow_html=True)
                else:
                    st.info("No word-level contribution data available.")
            else:
                st.error(f"API request failed with status code {\
                    response.status_code}")
        except Exception as e:
            st.error(f"Error contacting the API: {e}")


#DL part
st.title("📈 BERT")

# Display result
if st.button("Analyze sentiment with BERT", key='bert'):

    #Prepare parameters for request
    params = {"text": user_input}

    # Adjust endpoint to logistic route
    url = BASE_URI + "text_dl"

    #Check if input is correct
    if user_input.strip() == "":
        st.error("Please enter a review.")
    else:
        try:
            #Get prediction from the api
            response = requests.post(url, json=params)
            if response.status_code == 200:
                data = response.json()
                prediction = data["sentiment"]
                contrib_dict = data.get("contributions", {})
                top_positive = data.get("top_positive", [])
                top_negative = data.get("top_negative", [])

                if prediction.lower() == "positive":
                    st.markdown(
                        "<div style='padding:10px; background-color:#eaffe3; \
                            color:#33c800; border-radius:10px;'>"
                        "✅ <strong>Sentiment: Positive</strong></div>",
                        unsafe_allow_html=True
                    )
                elif prediction.lower() == "negative":
                    st.markdown(
                        "<div style='padding:10px; background-color:#ffe0e0; \
                            color:#d20000; border-radius:10px;'>"
                        "❌ <strong>Sentiment: Negative</strong></div>",
                        unsafe_allow_html=True
                    )
                else:
                    st.info("Sentiment could not be determined.")

                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)

                if contrib_dict:
                    st.markdown("#### 🔍 Word Importance Visualization")
                    html_vis = visualize_input_importance(user_input, \
                        contrib_dict, top_positive, top_negative)
                    st.markdown(html_vis, unsafe_allow_html=True)
                else:
                    st.info("No word-level contribution data available.")
            else:
                st.error(f"API request failed with status code {\
                    response.status_code}")
        except Exception as e:
            st.error(f"Error contacting the API: {e}")
