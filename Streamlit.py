import streamlit as st

import pandas as pd
import numpy as np
st.write("good")
st.image("labstr.png", caption="Sunrise by the mountains")
st.markdown(
    """
    <div style="direction: rtl;">
        <h2>سيارات</h2>
        
    </div>
    """,
    unsafe_allow_html=True
)
st.image("test2.png", caption="test")
st.title("سيارات ")

st.markdown("<h1 style='text-align: center; color: red;'>سيارات</h1>", unsafe_allow_html=True)

# Using HTML and CSS to set text direction to right-to-left
st.markdown(
    """
    <div style="direction: rtl;">
        <h1>سيارات</h1>
        
    </div>
    """,
    unsafe_allow_html=True
)
st.image("image1.png", caption="Sunrise by the mountains")
