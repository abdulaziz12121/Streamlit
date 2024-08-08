import streamlit as st

import pandas as pd
import numpy as np
st.write("good")
st.image("labstr.png", caption="Sunrise by the mountains")

option = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
