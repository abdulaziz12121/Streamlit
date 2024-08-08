import streamlit as st

import pandas as pd
import numpy as np
st.write("good")
st.image("labstr.png", caption="Sunrise by the mountains")

st.image("test2.png", caption="test")
st.title("سيارات ")

st.markdown("<h1 style='text-align: center; color: red;'>سيارات</h1>", unsafe_allow_html=True)

# Using HTML and CSS to set text direction to right-to-left
st.markdown(
    """
    <div style="direction: rtl;">
        <h1>This text is written from right to left</h1>
        <p>سيارات/p>
    </div>
    """,
    unsafe_allow_html=True
)
