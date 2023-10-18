import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd

camera = st.camera_input("Take a photo")

col1, col2 = st.columns([1, 1])

# สร้าง DataFrame
data = pd.DataFrame({
    "Name": ["Apple", "Banana", "Orange", "Mango"],
    "Price": [10, 20, 30, 40]
})

# แสดงตารางจาก DataFrame
col1.dataframe(data)

total_price = data["Price"].sum()

col1.write(
    f'<div style="font-size: 20px;">Total Price: {total_price}</div>',
    unsafe_allow_html=True
)

# กำหนด CSS เพื่อปรับขนาดและสีพื้นหลังของปุ่ม
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: green; /* สีเขียวสำหรับปุ่ม "Pay" */
    width: 150px; /* กำหนดความกว้าง */
    margin: 0 auto; /* จัดกลางแนวนอน */
}
div.stButton > button:last-child {
    background-color: red; /* สีแดงสำหรับปุ่ม "Cancel" */
    width: 150px; /* กำหนดความกว้าง */
    margin: 0 auto; /* จัดกลางแนวนอน */
}
</style>
""", unsafe_allow_html=True)

if col2.button("Pay"):
    switch_page("b")

if col2.button("Cancel"):
    switch_page("main")
