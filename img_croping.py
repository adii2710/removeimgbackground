# pip install rembg pillow
import streamlit as st
from rembg import remove
from PIL import Image

# input_path = "images/car10.jpg"
# output_path = "out.png"

# input = Image.open(input_path)
# output = remove(input)
# output.save(output_path)
side_image1 = st.file_uploader("Upload Right Side Image", type=["jpg", "jpeg", "png"])

if side_image1:
    side_image1 = Image.open(side_image1)
    output = remove(side_image1)
    st.image(output)