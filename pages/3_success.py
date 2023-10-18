import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container


col1, col2, _ = st.columns([1, 1, 1])

with col2:
    with stylable_container(
        key="qr_image",
        css_styles="""
        img {
            border-radius: 2em;
        }
        """,
    ):
        st.image("./assets/Check_green_icon.svg.png")

    col2.markdown(f"<h1 style='text-align: center; color: white;'>Success</h1>", unsafe_allow_html=True)

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
        if st.button("OK"):
            switch_page("main")
