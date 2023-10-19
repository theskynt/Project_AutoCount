import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container
import pandas as pd
import json

camera = st.camera_input("Take a photo")

col1, col2 = st.columns([1, 1])

data_in = ("Apple", "Banana", "Mango", "Apple")

with open("data.json", "r") as json_file:
    data = json.load(json_file)
    
name_list = []
price_list = []
for item in data_in:
    if item in data['pice']:
        name_list.append(item)
        price_list.append(data['pice'][item])

df = pd.DataFrame({'Name': name_list, 'Price': price_list})
col1.dataframe(df)

total_price = df['Price'].sum()

col1.write(
    f'<div style="font-size: 20px;">Total Price: {total_price}</div>',
    unsafe_allow_html=True
)


with col2:
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
        if st.button("Pay"):
            st.session_state.total_price = total_price
            switch_page("QR")

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

