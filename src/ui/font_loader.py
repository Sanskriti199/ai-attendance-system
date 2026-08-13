import streamlit as st
import base64


def inject_local_font(font_path, font_name):
    with open(font_path, "rb") as font_file:
        font_data = base64.b64encode(font_file.read()).decode()

    st.markdown(
        f"""
        <style>
        @font-face {{
            font-family: "{font_name}";
            src: url(data:font/ttf;base64,{font_data}) format("truetype");
            font-weight: normal;
            font-style: normal;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )