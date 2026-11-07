import streamlit as st

# Counter without session state – resets every rerun
counter = 0
button = st.button(label="Increase counter without session state")
if button:
    counter += 1
    st.write(counter)
    # This counter will always reset to 1 because Streamlit reruns the script top to bottom on every interaction

# Correctly initializing session state
if "counter1" not in st.session_state:
    st.session_state.counter1 = 0  # ✅ Fix: check if the key exists in session_state dict (not st.session_state.counter1)

# Counter using session state – persistent across reruns
button2 = st.button(label="Increase with session state")
if button2:
    st.session_state.counter1 += 1
    st.write("Session-based counter:", st.session_state.counter1)  # better to use st.write than print
