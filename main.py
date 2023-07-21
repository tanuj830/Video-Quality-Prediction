import streamlit as st
import time
import numpy as np
import pickle


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
    channelTitle = form.text_input(label='Enter Channel Name')
    viewCount = form.text_input(label='Enter Total Views of Video')
    likeCount = form.text_input(label='Enter Likes')
    commentCount = form.text_input(label='Enter Number of Comments')
    definition = form.text_input(label='Enter Definition(hd or sd anything)')# hd or sd anything
    caption = form.text_input(label='Enter Your Caption(true or false)')# true of false
    subscribers = form.text_input(label='Enter Total Number of Subs')
    totalViews = form.text_input(label='Enter Total Views On Channel')
    totalVideos = form.text_input(label='Total Videos in Channel')
    pushblishYear = form.text_input(label='Enter Publish Year')
    videoDuration = form.text_input(label='Enter Duration of Video')#convert to secs
    tags = form.text_input(label='Enter Video Tags')# no of tags
    title = form.text_input(label='Enter Title')# title length
    description = form.text_input(label='Enter  Description')# length
    submit_button = form.form_submit_button(label='Submit')

if submit_button:
    print("tanujsssssssssssss")
    # print(time)
    if (len(videoDuration) <= 4):
        time = "0:" + videoDuration
        DurationSecs = sum(x * int(t) for x, t in zip([3600, 60, 1], time.split(":")))
    elif (len(videoDuration ) > 4):
        DurationSecs = sum(x * int(t) for x, t in zip([3600, 60, 1], videoDuration.split(":")))

    tagsArray = tags.split()
    tagsCount = len(tagsArray)

    titleLength = len(title)

    channelTitleLength = len(channelTitle)

    descriptionLength = len(description)


    # Loading Model
    loaded_model = pickle.load(open('E:/pythonProject/model/trained_model.sav', 'rb'))

    # input_data = (0,19,1410150,18797,76,0,1,369000,20517888,1850,0.277472727,2020,4520.0,142,76,1057)
    input_data = (1,int(channelTitleLength),int(viewCount),int(likeCount),int(commentCount),int(definition),int(caption),int(subscribers),int(totalViews),int(totalVideos),0
,int(pushblishYear), int(DurationSecs),int(tagsCount),int(titleLength),int(descriptionLength))
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the np array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]==1):
            st.toast("High Quality Video")
            st.balloons()
    else:
            st.toast('Low Video Quality')
            st.snow()


st.write("[Challenge this model by entering input(dataset is available here)](https://tanujbhatt.in)")







