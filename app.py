import os
import streamlit as st
import requests
from utils.visualization import visualize_input_importance


# Define the base URI of the API
#   - Potential sources are in `.streamlit/secrets.toml` or in the Secrets section
#     on Streamlit Cloud
#   - The source selected is based on the shell variable passend when launching streamlit
#     (shortcuts are included in Makefile). By default it takes the cloud API url
if "API_URI" in os.environ:
    BASE_URI = "https://sentiscope-811189409150.europe-west1.run.app/"
else:
    BASE_URI = st.secrets["cloud_api_uri"]
# Add a '/' at the end if it's not there
BASE_URI = BASE_URI if BASE_URI.endswith("/") else BASE_URI + "/"
# Define the url to be used by requests.get to get a prediction (adapt if needed)
url = BASE_URI + "predict"

# TODO: Add some titles, introduction, ...
st.title("SentiScope: Review Analysis")
st.subheader("Predicting the sentiment of customer reviews")

# TODO: Request user input
user_input = st.text_input("Enter a customer review below and click the button to analyze its sentiment:")
params = {"review": user_input}

# TODO: Call the API using the user's input
#   - url is already defined above
#   - create a params dict based on the user's input
#   - finally call your API using the requests package


# TODO: retrieve the results
#   - add a little check if you got an ok response (status code 200) or something else
#   - retrieve the prediction from the JSON



if st.button("Analyze sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a review before clicking the button.")
    else:
        response = None
        try:
            response = requests.get(url, params=params)
        except Exception as e:
            st.error(f"Error contacting the API: {e}")

        prediction = None
        contrib_dict = {}
        top_positive = []
        top_negative = []

        if response:
            if response.status_code == 200:
                data = response.json()
                prediction = data["Sentiment"]
                contrib_dict = data.get("contributions", {})
                top_positive = data.get("top_positive", [])
                top_negative = data.get("top_negative", [])
            else:
                st.error(f"API request failed with status code {response.status_code}.")

# TODO: display the prediction in some fancy way to the user
        st.success(f"**Predicted sentiment:** `{prediction}`")
        if contrib_dict:
            st.markdown("#### 🔍 Word Importance Visualization")
            html_vis = visualize_input_importance(user_input, contrib_dict, top_positive, top_negative)
            st.markdown(html_vis, unsafe_allow_html=True)
        else:
            st.info("No word-level contribution data available for this input.")

# TODO: [OPTIONAL] maybe you can add some other pages?
#   - some statistical data you collected in graphs
#   - description of your product
#   - a 'Who are we?'-page
