import streamlit as st
import pandas as pd
data={
    'name':None,
    'Feedback':None,
    'dob':None,
    'gender':None,
    'Age':None,
}

st.title("Streamlit Form Demo")
#form to hold interactive elmenets
with st.form(key="Sample_form"):#key is not necessary but used to identify form
    #text input
    st.subheader("text Inputs")
    data['name']=st.text_input("Enter your name")
    data["Age"]=st.number_input("Enter your Age")
    data['Feedback']=st.text_area("Provide youer feedback")
    #Date and Time Inputs 
    st.subheader("Date and Time Inputs")
    data['dob']=st.date_input("Select your date of birth")
    time=st.time_input("Choose a preferred time")

    #Selectors
    st.subheader("Selectors")
    choice=st.radio("Choose an option",['Option 1','Option 2','Option 3'])
    data['gender']=st.selectbox("select your gender",['Male','Female','Other'])
    slider_value=st.select_slider("Select a range",options=[1,2,3,4])
    submit=st.form_submit_button(label="submit your form")
if submit:
    for key in data.keys():
        print(f"{key} is {data[key]}")