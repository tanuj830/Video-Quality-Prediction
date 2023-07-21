import streamlit as st

st.set_page_config(page_title="Video Quality Prediction", layout='wide')

st.subheader("Hey, I'm Tanuj Bhatt  :wave:")

with st.container():
        st.title("Video Quality Prediction...!")
        left_col, right_col = st.columns(2)
        with left_col:
            st.write("This Web App is used to predict the quality of the video and it is done using machine learning algorithm. For predicting video quality there are following parameters on which our algorithm works and predict the video quality.  ")
            st.write("The Video Quality Prediction project is a cutting-edge Python-based application that aims to revolutionize the way video content is consumed and delivered. Rather than focusing on video quality enhancement, this project concentrates on predicting the quality of videos before they are streamed or displayed. By leveraging the power of Artificial Intelligence (AI) and Machine Learning (ML) algorithms, the project accurately predicts video quality, enabling content providers and streaming platforms to optimize video delivery for a seamless and immersive viewing experience.")


        with right_col:
            st.video("https://player.vimeo.com/external/442381769.sd.mp4?s=f206b533b8bdb1cc1364de87074af32f4f0f2231&profile_id=164&oauth2_token_id=57447761")


with st.container():
    st.subheader("Algorithm Used ?")
    left_col2, right_col2 = st.columns(2)
    with left_col2:
        st.image("https://images.pexels.com/photos/750539/pexels-photo-750539.jpeg?auto=compress&cs=tinysrgb&w=600")
    with right_col2:
        st.write(
            "Logistic regression is a supervised machine learning algorithm mainly used for classification tasks where the goal is to predict the probability that an instance of belonging to a given class or not. It is a kind of statistical algorithm, which analyze the relationship between a set of independent variables and the dependent binary variables. It is a powerful tool for decision-making. For example email spam or not. ")

with st.container():
    st.title("Predict Video Quality: Enter Credentials")

    form = st.form(key='my_form')
    form.text_input(label='Enter ')
    form.text_input(label='Enter 2')
    form.text_input(label='Enter 3')
    form.text_input(label='Enter 4')
    form.text_input(label='Enter 5')
    form.text_input(label='Enter 6')
    form.text_input(label='Enter 7')
    form.text_input(label='Enter 8')
    form.text_input(label='Enter 9')
    form.text_input(label='Enter 10')
    form.text_input(label='Enter 11')
    form.text_input(label='Enter 12')
    form.text_input(label='Enter 13')
    form.text_input(label='Enter 14')
    form.text_input(label='Enter 15')
    submit_button = form.form_submit_button(label='Submit')

if submit_button:
        print(form)