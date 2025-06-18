import streamlit as st
import pandas as pd

st.title("About the models")

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("The logistic regression model")

st.markdown("""The first **Gridsearch** was done on 1% of the training data,
            so 36.000 observations:""")

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

st.markdown("""For the Deep Learning approach, we used a pre-trained Transformer
            model called [tiny BERT](https://huggingface.co/prajjwal1/bert-tiny)
            from HuggingFace. This model is a smaller version of the BERT model,
            which is known for it's ability to work with natural language.
            For training, we used the pre-trained tiny bert Tokenizer, to get
            the data ready for the model. As the tiny model already comes with
            over 4.000.000 parameters to train, we started with a small portion
            of our data:""")

st.image("./assets/bert_train_1.png", width = 1500)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.image("./assets/bert_train_2.png", width = 1500)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""These graphs were created when training the model on 15.000 rows.
            After a couple more iterations with increasing the training data
            little by little, the model we use in the backend was trained on
            200.000 observations using 10 epochs, a batch size of 32, the adam
            optimizer and binary crossentropy as a loss function. The model got
            an accuracy of around 90,1206% on the test set.
            The training was done in google colab and was already bringing us to
            the edge of open source ressources for efficient model training.""")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""The amount of data used for this project was great to train
            models with good accuracy and generalisation, but also striked some
            difficulties when training complex models. With more computational
            power, time and memory space, especially the BERT model could have
            been optimized more.""")
