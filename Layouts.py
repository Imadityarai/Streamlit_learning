import streamlit as st
st.sidebar.title("This is the sidebar")
st.sidebar.write("You can place elements like slidebars,buttons,and text here")
sidebar_input=st.sidebar.text_input("Enter something in the sidebar")

#Tabs Layout
tab1,tab2,tab3=st.tabs(["tab 1","Tab 2","Tab 3"])

with tab1:
    st.write("You are in tab 1")
with tab2:
    st.write("You are in Tab 2")
with tab3:
    st.write("You are in Tab 3")

#Columns Layout
col1,col2=st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Content for column 1")
with col2:
    st.header("Column 2")
    st.write("Content for column 2")
#container examples
with st.container(border=True):
    st.write("this is inside the container")
    st.write("You can think of container as a grouping for elements")
    st.write("Containers help manage sections of page")

#Empty Placeholder
placeholder=st.empty()
placeholder.write("this is an empty placeholder,useful for dyanmic content")

if st.button("Update Placeholder"):
    placeholder.write("The content if this placeholder has been updated")

#Expander
with st.expander("Expand for more details"):
    st.write("this is additional information that is hidden by default")
    st.write("You can use expanders to keep your interface clean")

    #Popover(ToolTip)
st.write("Hover over this button for a tooltip")
st.button("Button with tooltip",help="this is a tooltip or popover on hover")

#sidebar input handling
if sidebar_input:
    st.write(f"you entered in the sidebar:{sidebar_input}")