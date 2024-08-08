import streamlit as st

import pandas as pd
import numpy as np
st.markdown(
    """
   <div style="direction: rtl;">
    <h1 style="color: red;">العنوان</h1>
        
    </div>
    """,
    unsafe_allow_html=True
)



# Using HTML and CSS to set text direction to right-to-left
st.markdown(
    """
    <div style="direction: rtl;">
        <h2>العنوان الفرعي</h2>
        
    </div>
    """,
    unsafe_allow_html=True
)
st.image("image1.png", caption="Sunrise by the mountains")
