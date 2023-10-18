import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container

col1, col2, _ = st.columns([1, 1, 1])

col2.markdown("<h1 style='text-align: center; color: white;'>QR Code</h1>", unsafe_allow_html=True)

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