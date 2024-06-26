import rembg as rb
from PIL import Image
import streamlit as st

# Displaying instructions using Markdown
st.sidebar.markdown("""
    # Instructions for Using the Application
    Welcome to our application! Here are the steps to get started:

    1. **Step One**: Upload your data file using the file uploader on the sidebar.
    2. **Step Two**: Select the options you want to apply to your data.


    Feel free to explore the different features and options available in the application.

    For any questions or issues, please contact adityakhopade2003@gmail.com.
""")

side_image1 = st.file_uploader("Upload Left Side Image", type=["jpg", "jpeg", "png"])
side_image2 = st.file_uploader("Upload Right Side Image", type=["jpg", "jpeg", "png"])

col1, col2=st.columns(2)
if side_image1 and side_image2:
    side_image1 = Image.open(side_image1)
    side_image2 = Image.open(side_image2)
    side_image2=side_image2.transpose(Image.FLIP_LEFT_RIGHT)
    output = rb.remove(side_image1)
    output2 = (rb.remove(side_image2))
    with col1:
        st.image(output)
    with col2:
        st.image(output2)