import streamlit as st
import os #also used for joining file paths
import numpy as np
import pandas as pd#used for working with dataframe
import matplotlib.pyplot as plt
st.title("Streamlit Tutorials")
st.header("this is header")
st.subheader("this is subheader")
st.markdown("This is _markdown_")
st.caption("small text")
st.write("hello world")
#" 3+4 will be written as 7 on app"
"hello world" if 2>3 else "bye" 
#it will print bye just simple if else condn
pressed=st.button("Press me")
print(pressed)#here if we press button it save as true else false
#how to show code in any language
code_example="""
def print():
 print("hello")"""
st.code(code_example,language="python")
st.divider()#a divider line
#how to add image
st.image(os.path.join(os.getcwd(),"static","100_days.png"),width=50)
#showing dataframe on app
data={
    'age':[12,1,3,43],
    'color':['b','w','br','b']
}
df=pd.DataFrame(data)
st.dataframe(df)
#data editor Section (Editable Dataframe)
st.subheader("Static table")
editable_df=st.data_editor(df)
print(editable_df)
#working with json
st.json(data)
#working with charts
chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C']
)
#Chart Section
st.area_chart(chart_data)
st.bar_chart(chart_data)
st.line_chart(chart_data)
#scatter data section
scatter_data=pd.DataFrame({
    'x':np.random.randn(100),
    'y':np.random.randn(100)
})
st.scatter_chart(scatter_data)
#Map Section 
map_data=pd.DataFrame(
    np.random.randn(100,2)/[50,50]+[37.76,-122.4],
    columns=['lat','lon']
)
st.map(map_data)