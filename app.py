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
    BASE_URI = st.secrets[os.environ.get("API_URI")]
else:
    BASE_URI = st.secrets["cloud_api_uri"]
# Add a '/' at the end if it's not there
BASE_URI = BASE_URI if BASE_URI.endswith("/") else BASE_URI + "/"
# Define the url to be used by requests.get to get a prediction (adapt if needed)
url = BASE_URI + "predict"

# TODO: Add some titles, introduction, ...
st.markdown("#SentiScope: Review Analysis")
st.markdown("##Predicting the sentiment of customer reviews")
st.write("Enter a customer review below and click the button to analyze its sentiment.")

# TODO: Request user input
user_input = st.text_input("Enter a review:")

# TODO: Call the API using the user's input
#   - url is already defined above
#   - create a params dict based on the user's input
#   - finally call your API using the requests package
params = {"text": user_input}
response = None
if user_input.strip():
    try:
        response = requests.get(url, params=params)
    except Exception as e:
        st.error(f"Error contacting the API: {e}")

# TODO: retrieve the results
#   - add a little check if you got an ok response (status code 200) or something else
#   - retrieve the prediction from the JSON
prediction = None
contrib_dict = {}
top_positive = []
top_negative = []

if response:
    if response.status_code == 200:
        data = response.json()
        prediction = data.get("prediction", "No prediction returned.")
        #contrib_dict = data.get("contributions", {})
        #top_positive = data.get("top_positive", [])
        #top_negative = data.get("top_negative", [])
    else:
        st.error(f"API request failed with status code {response.status_code}.")

# TODO: display the prediction in some fancy way to the user
if st.button("Analyze sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a review before clicking the button.")
    elif prediction:
        st.success(f"**Predicted sentiment:** `{prediction}`")
        #if contrib_dict:
            #st.markdown("#### 🔍 Word Importance Visualization")
            #html_vis = visualize_input_importance(user_input, contrib_dict, top_positive, top_negative)
            #st.markdown(html_vis, unsafe_allow_html=True)
        #else:
            #st.info("No word-level contribution data available for this input.")

# TODO: [OPTIONAL] maybe you can add some other pages?
#   - some statistical data you collected in graphs
#   - description of your product
#   - a 'Who are we?'-page
