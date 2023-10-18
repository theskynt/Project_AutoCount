import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container
import pandas as pd

st.markdown("<h1 style='text-align: center; color: white;'>สินค้า 🛒</h1>", unsafe_allow_html=True)

data = pd.DataFrame({
    "Name": ["Apple", "Banana", "Orange", "Mango"],
    "Price": [10, 20, 30, 40]
})

option = st.selectbox("Select", data["Name"])

col1, col2, _, __ = st.columns([1, 1, 1, 1])

with col1:
    st.write("ราคาเดิม")
    st.write(" ")
    st.write(" ")
    st.write("ราคาใหม่")

with col2:
    price = data[data['Name'] == option]['Price'].values[0]
    st.write(f"{price} บาท")
    new_price = st.text_input("", placeholder="กรอกราคาใหม่")

st.markdown("<h1 style='text-align: center; color: white;'> </h1>", unsafe_allow_html=True)
st.write("เปลี่ยน QR Code")
uploaded_file = st.file_uploader("Choose a file" , type=['png', 'jpeg', 'jpg'])
if uploaded_file is not None:
    st.image(uploaded_file)

_, button1, button2, __ = st.columns([1, 1, 1, 1])
with button1:
    with stylable_container(
        key="green_button",
        css_styles="""
            button {
                background-color: green;
                color: white;
                width: 150px; 
            }
            """,
    ):
        if st.button("Save"):
            switch_page("main")

with button2:
    with stylable_container(
        key="red_button",
        css_styles="""
            button {
                background-color: red;
                color: white;
                width: 150px; 
            }
            """,
    ):
        if st.button("Cancel"):
            switch_page("main")