import streamlit as st
import base64
import os


def get_logo_path():
    return os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "assets",
        "logoo.png"
    )


def header_home():
    logo_path = get_logo_path()

    with open(logo_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <div style="display:flex; flex-direction:column; align-items:center;
                    justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src="data:image/png;base64,{encoded_image}"
                 style="height:100px;" />
            <h1 style="text-align:center; color:#E0E3FF">
                SMART<br/>CLASS
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )


def header_dashboard():
    logo_path = get_logo_path()

    with open(logo_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src="data:image/png;base64,{encoded_image}"
                 style="height:85px;" />

            <div style="
                text-align:left;
                color:#5865F2;
                font-family:'Climate Crisis', sans-serif;
                font-size:2rem;
                line-height:0.9;
                font-weight:bold;
            ">
                SMART<br/>CLASS
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )