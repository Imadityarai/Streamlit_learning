import streamlit as st
import requests
import json,os
import plotly.express as px
url = "https://leetcode-api-faisalshohag.vercel.app/Imadityarai"
res = requests.get(url).json()
print(res)
st.set_page_config(page_title="Aditya's codefolio",layout="wide")
st.image(os.path.join(os.getcwd(),"static","100_days.png"),width=50)
st.sidebar.title("Aditya Rai")
st.sidebar.markdown("CS Undergrad|DSA & ML Enthusiast")
st.sidebar.write("https/github.com/adityarai")
st.sidebar.write("adityarai20051978@gmail.com")

#Tabs
tabs=st.tabs(["Home","DSA Profiles","Analysis"])
with tabs[0]:
    st.title("👋 Welcome to my Codefolio")
    st.write("""
    I'm Aditya Rai, a Computer Science student and DSA enthusiast.  
    I love solving problems on LeetCode and GFG and building cool Python projects.
    """)
    st.subheader("🛠 Tech Stack")
    st.markdown("Python | Pandas | NumPy | Streamlit | Scikit-learn")
with tabs[1]:
    st.title("DSA Profiles")
    st.metric("Total Solved", res['totalSolved'])
    st.metric("Easy", res['easySolved'])
    st.metric("Medium", res['mediumSolved'])
    st.metric("Hard", res['hardSolved'])
    st.metric("ranking",res['ranking'])
    st.metric("contrinution_points",res['contributionPoint'])
    st.metric("reputation",res['reputation'])
    fig = px.pie(
            names=["Easy", "Medium", "Hard"],
            values=[res['easySolved'], res['mediumSolved'], res['hardSolved']],
            title="LeetCode Problem Distribution"
        )
    st.plotly_chart(fig)
    
    with st.form(key="compare"):
        id=st.text_input(label="enter your id to compare")
        btn=st.form_submit_button(label="compare it now")
        if btn:
            url1=f"https://leetcode-api-faisalshohag.vercel.app/{id}"
            res1 = requests.get(url1).json()
            st.metric("Total Solved", res1['totalSolved'])
            st.metric("Easy", res1['easySolved'])
            st.metric("Medium", res1['mediumSolved'])
            st.metric("Hard", res1['hardSolved'])
            st.metric("ranking",res1['ranking'])
            st.metric("contrinution_points",res1['contributionPoint'])
            st.metric("reputation",res1['reputation'])
            fig1 = px.pie(
                names=["Easy", "Medium", "Hard"],
                values=[res1['easySolved'], res1['mediumSolved'], res1['hardSolved']],
                title="LeetCode Problem Distribution"
            )
            st.plotly_chart(fig1)
    
       