import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# st.write("# AutoCount 👋")

st.markdown("<h1 style='text-align: center; color: white;'>AutoCount 👋</h1>", unsafe_allow_html=True)

st.markdown("----", unsafe_allow_html=True)
columns = st.columns((2, 1, 2))
button_pressed = columns[1].button('Pay Here')
if button_pressed:
    switch_page("payment")
st.markdown("----", unsafe_allow_html=True)