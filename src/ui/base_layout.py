import os
import streamlit as st
from src.ui.font_loader import inject_local_font


def style_background_home():
    st.markdown(
        """
        <style>
            .stApp {
                background: #5865F2 !important;
            }

            .stApp div[data-testid="stColumn"] {
                background-color: #E0E3FF !important;
                padding: 2.5rem !important;
                border-radius: 5rem !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


def style_background_dashboard():
    st.markdown(
        """
        <style>
            .stApp {
                background: #E0E3FF !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


def style_base_layout():

    base_path = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )

    climate_font = os.path.join(
        base_path,
        "assets",
        "fonts",
        "ClimateCrisis.ttf"
    )

    outfit_font = os.path.join(
        base_path,
        "assets",
        "fonts",
        "Outfit.ttf"
    )

    inject_local_font(
        climate_font,
        "Climate Crisis"
    )

    inject_local_font(
        outfit_font,
        "Outfit"
    )

    st.markdown(
        """
        <style>

            #MainMenu,
            footer,
            header {
                visibility: hidden;
            }

            .block-container {
                padding-top: 0rem !important;
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
            }

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
                color: black !important;
            }

            h3,
            h4,
            p {
                font-family: 'Outfit', sans-serif !important;
            }

            button {
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button:hover {
                transform: scale(1.05) !important;
            }

        </style>
        """,
        unsafe_allow_html=True
    )