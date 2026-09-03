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

/* Default text color for readability on light background */
.stApp p,
.stApp span,
.stApp label,
.stMarkdown,
.stCaption,
div[data-testid="stCaptionContainer"] {
    color: #111 !important;
}

/* Main headings */
h1 {
    font-family: 'Climate Crisis', sans-serif !important;
    font-size: 2.5rem !important;
    line-height: 1.1 !important;
    margin-bottom: 0rem !important;
}

/* Secondary headings */
h2 {
    font-family: 'Climate Crisis', sans-serif !important;
    font-size: 2rem !important;
    line-height: 1 !important;
    margin-bottom: 0rem !important;
    color: black !important;
}

/* Normal text */
h3,
h4,
p {
    font-family: 'Outfit', sans-serif !important;
}

/* Text inputs & password fields */
.stTextInput input,
.stTextInput > div > div,
div[data-testid="stTextInputRootElement"] {
    background-color: #FFFFFF !important;
    color: black !important;
    border-radius: 0.8rem !important;
    border: 1px solid #ccc !important;
}

.stTextInput input::placeholder {
    color: #888 !important;
}

/* Selectbox / dropdown */
.stSelectbox > div > div,
div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    color: black !important;
    border-radius: 0.8rem !important;
    border: 1px solid #ccc !important;
}

.stSelectbox span,
.stSelectbox div[data-baseweb="select"] span,
div[data-baseweb="select"] div[title] {
    color: black !important;
}

div[data-baseweb="popover"],
ul[data-baseweb="menu"] {
    background-color: #FFFFFF !important;
}

div[data-baseweb="popover"] li,
div[data-baseweb="popover"] li span {
    background-color: #FFFFFF !important;
    color: black !important;
}

div[data-baseweb="popover"] li:hover {
    background-color: #E0E3FF !important;
}

/* Dialog / modal box - broad selector for all st.dialog variants */
div[data-testid="stDialog"],
div[data-testid="stDialog"] > div,
div[role="dialog"],
div[aria-modal="true"] {
    background-color: #FFFFFF !important;
}

div[data-testid="stDialog"] *,
div[role="dialog"] *,
div[aria-modal="true"] * {
    color: black !important;
}

div[data-testid="stDialog"] button,
div[data-testid="stDialog"] button *,
div[role="dialog"] button,
div[role="dialog"] button *,
div[aria-modal="true"] button,
div[aria-modal="true"] button * {
    color: white !important;
}

/* Table / DataFrame */
[data-testid="stTable"],
[data-testid="stDataFrame"] {
    background-color: #FFFFFF !important;
}

[data-testid="stTable"] table,
[data-testid="stTable"] th,
[data-testid="stTable"] td,
[data-testid="stDataFrame"] div {
    color: black !important;
    background-color: #FFFFFF !important;
}

/* Audio / Camera input widgets */
[data-testid="stAudioInput"],
[data-testid="stCameraInput"] {
    background-color: #FFFFFF !important;
    border-radius: 0.8rem !important;
}

/* Buttons — keep white text regardless of the rules above */
.stApp button,
.stApp button * {
    color: white !important;
}

button {
    border-radius: 1.5rem !important;
    background-color: #5865F2 !important;
    color: white !important;
    padding: 10px 20px !important;
    border: none !important;
    transition: transform 0.25s ease-in-out !important;
}

/* Secondary buttons */
button[kind="secondary"] {
    border-radius: 1.5rem !important;
    background-color: #EB459E !important;
    color: white !important;
    padding: 10px 20px !important;
    border: none !important;
}

/* Tertiary buttons */
button[kind="tertiary"] {
    border-radius: 1.5rem !important;
    background-color: black !important;
    color: white !important;
    padding: 10px 20px !important;
    border: none !important;
}

/* Button hover */
button:hover {
    transform: scale(1.05) !important;
}

</style>
        """,
        unsafe_allow_html=True
    )