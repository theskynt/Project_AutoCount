import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

st.markdown("<h1 style='text-align: center; color: white;'>สินค้า 🛒</h1>", unsafe_allow_html=True)

data = pd.DataFrame({
    "Name": ["Apple", "Banana", "Orange", "Mango"],
    "Price": [10, 20, 30, 40]
})

option = st.selectbox("select", data["Name"])

col1, col2, _, __ = st.columns([1, 1, 1, 1])
with col1:
    st.markdown(
        "<div style='border: 1px solid white; padding: 10px; text-align: center;'>ราคาเดิม</div>",
        unsafe_allow_html=True
    )

with col2:
    price = data[data['Name'] == option]['Price'].values[0]
    st.markdown(
        f"<div style='border: 1px solid white; padding: 10px; text-align: center;'>Price: {price}</div>",
        unsafe_allow_html=True
    )

col1.write(" ")

with col1:
    st.markdown(
        "<div style='border: 1px solid white; padding: 10px; text-align: center;'>ราคาใหม่</div>",
        unsafe_allow_html=True
    )

with col2:
    new_price = st.text_input("", placeholder="กรอกราคาใหม่")

col1.write(new_price)