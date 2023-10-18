import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container


col1, col2, _ = st.columns([1, 1, 1])
# ดึงค่า total_price จาก st.session_state
total_price = st.session_state.total_price

col2.markdown("<h1 style='text-align: center; color: white;'>Payment QR</h1>", unsafe_allow_html=True)

with col2:
    with stylable_container(
        key="qr_image",
        css_styles="""
        img {
            border-radius: 2em;
        }
        """,
    ):
        st.image("./assets/IMG_0840.JPG")


col2.markdown(f"<h1 style='text-align: center; color: white;'>Price : {total_price}</h1>", unsafe_allow_html=True)

with col2:
    with stylable_container(
        key="green_button",
        css_styles="""
            button {
                justify-content: center;
                background-color: green;
                color: white;
                width: 220px; 
            }
            """,
    ):
        if st.button("Pay"):
            st.session_state.total_price = total_price
            switch_page("success")

    with stylable_container(
        key="red_button",
        css_styles="""
            button {
                justify-content: center;
                background-color: red;
                color: white;
                width: 220px; 
            }
            """,
    ):
        if st.button("Cancel"):
            switch_page("payment")
