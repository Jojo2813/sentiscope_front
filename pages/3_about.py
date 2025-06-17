import streamlit as st
import pandas as pd

st.title("About the models")

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("The logistic regression model")

st.markdown("""The first **Gridsearch** was done on 1% of the training data,
            so 36000 observations:""")

df = pd.read_csv("./assets/grid_search_ml.csv", index_col=0)
small_df = df[['params','mean_test_score',\
    'std_test_score','rank_test_score']]

st.write("CV results:")
st.dataframe(small_df)

st.write("Whole gridsearch data:")
st.dataframe(df)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""The second **Gridsearch** was done on around 30% of the training
            data, so over 1 million observations:""")

df_large = pd.read_csv("./assets/cv_results_1m.csv")

df_large_small = df_large[['params','mean_test_score',\
    'std_test_score','rank_test_score']]

st.write("CV results:")
st.dataframe(df_large_small)


st.write("Whole gridsearch data:")
st.dataframe(df_large)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""With increasing training data, a bigger C led to an improvement
            of the model's accuracy. To make sure the model was not overfitting,
            we created a learning curve for a model trained on 1.5 million
            rows:""")

st.markdown("<br>", unsafe_allow_html=True)

st.image("./assets/learning_curve_1mil.png", width=1250)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""The final model was then trained with a parameter C = 10 on all
            3.6 million training observations.
            When tested on the dedicated test data of 400.000 unseen reviews,
            the model got an accuracy score of 92,14275%""")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("The BERT model")
