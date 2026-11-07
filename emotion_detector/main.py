import streamlit as st
import requests
import json
import base64
from PIL import Image
import io

st.set_page_config(page_title="Emotion Detector", page_icon="😊")
st.title("Know your Current Emotion 😂😒😭")

st.markdown("Click your photo below and let the model predict your emotion.")

# Capture image
image = st.camera_input("Click your photo")

if image:
    try:
        # Read and encode image
        img_bytes = image.getvalue()
        img_b64 = base64.b64encode(img_bytes).decode("utf-8")
        payload = {"image_data": img_b64}

        # Send to FastAPI backend
        response = requests.post("https://952c697cd21a.ngrok-free.app/predict", json=payload)

        # Handle response
        if response.status_code == 200:
            result = response.json()
            st.success(f"Emotion: `{result['emotion']}`  \nConfidence: `{result['confidence']:.2f}%`")
        else:
            st.error(f"Server error: {response.status_code}")
            st.text("Response content:")
            st.text(response.text)

    except requests.exceptions.JSONDecodeError:
        st.error("😬 The response was not JSON. Possible server-side error or empty response.")
    except Exception as e:
        st.exception(f"Unexpected error: {e}")
