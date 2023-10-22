import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container

col1, col2, col3 = st.columns([1, 1, 1])
col2.markdown("<h1 style='text-align: center; color: white;'>AutoCount 💸</h1>", unsafe_allow_html=True)

with col2:
    with stylable_container(
        key="qr_image",
        css_styles="""
        img {
            border-radius: 2em;
        }
        """,
    ):
        st.image("./assets/869639.png")

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
        if st.button('Start Yolov8 Model'):
            switch_page("payment")

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
        if st.button('Start Detr Model'):
            switch_page("pay")



with col3:
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col3:
        with stylable_container(
            key="Admin_button",
            css_styles="""
                button {
                    justify-content: center;
                    background-color: transparent;
                    color: #333;
                    border: none;
                    padding: 0;
                    cursor: pointer;
                    font-size:300px;
                    width: 100px;
                    color: white;
                }
                """,
        ):
            if st.button("Setting⚙️"):
                switch_page("setting")

