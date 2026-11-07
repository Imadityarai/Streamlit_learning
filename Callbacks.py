#callbacks are functions which are triggered when any button 
#is pressed
import streamlit as st

# Initialize session state if not already set
if "step" not in st.session_state:
    st.session_state.step = 1
if "info" not in st.session_state:
    st.session_state.info = {}
def got_to_step1():
    st.session_state.step=1
# Callback to go to step 2
def go_to_step2(name):
    st.session_state.info["name"] = name
    st.session_state.step = 2

# Step 1: Collect user input
if st.session_state.step == 1:
    st.header("Part 1: Info")
    name = st.text_input("Name", value=st.session_state.info.get("name", ""))
    st.button("Next", on_click=go_to_step2, args=(name,))

# Step 2: Review and Submit
elif st.session_state.step == 2:
    st.header("Part 2: Review")
    st.subheader("Please review this:")
    st.write(f"**Name**: {st.session_state.info.get('name', '')}")

    if st.button("Submit"):
        st.success("Great!")
        st.balloons()
        st.session_state.info = {}
    st.button("Pre",on_click=got_to_step1)

#summary use session_state to remember session and callbacks to go from 1 session to another session