import streamlit as st
from PIL import Image

camera_image = st.camera_input('Camera')

if camera_image:
    img = Image.open(camera_image)
    gray_image = img.convert('L')
    st.image(gray_image)