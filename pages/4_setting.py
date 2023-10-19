import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container
import pandas as pd
import os
import json

st.markdown("<h1 style='text-align: center; color: white;'>สินค้า 🛒</h1>", unsafe_allow_html=True)

# ดึงข้อมูลจากไฟล์ JSON
with open("data.json", "r") as json_file:
    data = json.load(json_file)

with open("temp_data.json", "r") as json_file:
    temp_data = json.load(json_file)

st.write(temp_data)

option = st.selectbox("Select", list(data["pice"].keys()))

col1, col2, _, __ = st.columns([1, 1, 1, 1])

with col1:
    st.write("ราคาเดิม")
    st.write(" ")
    st.write(" ")
    st.write("ราคาใหม่")

with col2:
    price = data["pice"][option]
    st.write(f"{price} บาท")
    new_price = st.text_input("", placeholder="กรอกราคาใหม่")

    if new_price != "":
        if new_price.isdigit():
            if st.button("Update"):
                temp_data["pice"][option] = int(new_price)
                with open("temp_data.json", "w") as json_file:
                    json.dump(temp_data, json_file)
                st.success("บันทึกสำเร็จ")
        else:
            st.error("กรอกเฉพาะตัวเลขเท่านั้น")

st.markdown("<h1 style='text-align: center; color: white;'> </h1>", unsafe_allow_html=True)
st.write("เปลี่ยน QR Code")
uploaded_file = st.file_uploader("Choose a file" , type=['png', 'jpeg', 'jpg'])
if uploaded_file is not None:
    file_path = f"./qr/{uploaded_file.name}"
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.getvalue())
        temp_data["qr"] = uploaded_file.name
        with open("temp_data.json", "w") as json_file:
            json.dump(temp_data, json_file)
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")

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
            data = temp_data
            with open("data.json", "w") as json_file:
                json.dump(data, json_file)
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