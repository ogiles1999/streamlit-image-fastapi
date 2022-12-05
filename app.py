import streamlit as st
import requests

uploaded_image = st.file_uploader("Image", type=["jpg"])

if uploaded_image is not None:
    print(uploaded_image)
    response = requests.post("http://127.0.0.1:8000/image",files={"file":uploaded_image.getvalue()})
    st.write(response.status_code)
    st.write(type(response.json()))
    st.write(response.json())
