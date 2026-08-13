import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout, style_background_home
from src.components.footer import footer_home
def home_screen():
    
    header_home()
    style_background_home()
    style_base_layout()

    st.markdown("""
    <style>
        div[data-testid="stHorizontalBlock"] {
            transform: translateY(-80px) !important;
        }
    </style>
""", unsafe_allow_html=True)


    col1,col2=st.columns(2, gap="large")

    with col1:
        st.header("I'm Student")
        st.image(r"C:\Users\Sanskriti\Desktop\ai-attendance-system\assets\student logo.png", width=180)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='student'
            st.rerun()

    with col2:
        st.header("I'm Teacher")
        st.image(r"C:\Users\Sanskriti\Desktop\ai-attendance-system\assets\teacher logo.webp",width=150)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type']='teacher'
            st.rerun()

    footer_home()