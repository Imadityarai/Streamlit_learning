import streamlit as st
import requests

st.title("Classification of Notes")

with st.form("Notes"):
    VWTI = st.number_input("Enter the VWTI")
    SWTI = st.number_input("Enter the SWTI")
    CWTI = st.number_input("Enter the CWTI")
    EI   = st.number_input("Enter the EI")
    submitted = st.form_submit_button("Submit")

if submitted:
    payload = {
        "VWTI": VWTI,
        "SWTI": SWTI,
        "CWTI": CWTI,
        "EI": EI
    }
    try:
        res = requests.post("https://1196-34-106-107-44.ngrok-free.app/predict", json=payload)
        print("Status Code:", res.status_code)
        print("Response Text:", res.text)
        res.raise_for_status()
        st.success(f"Prediction: {res.json()['result'][0]}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request error: {e}")
    except ValueError as e:
        st.error(f"JSON decode error: {e}\nRaw response:\n{res.text}")
    print(res.json()['result'])