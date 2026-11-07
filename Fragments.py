#Fragments are way to re run only certain portion of your UI
#and better organise or seprate out your code
import streamlit as st

@st.fragment
def toggle_and_text():
    cols=st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter the Text")
    
@st.fragment()
def filter_and_file():
    new_cols=st.columns(2)
    new_cols[0].checkbox("Filter")
    new_cols[1].file_uploader("ipload image")
    
toggle_and_text()
cols=st.columns(2)
cols[0].selectbox("Select",[1,2,3],None)
cols[1].button("Update")
filter_and_file()