import streamlit as st

def footer_home():
    st.markdown("""
        <div style="
            margin-top:-5rem;
            display:flex;
            justify-content:center;
            align-items:center;
        ">
            <p style="font-weight:bold; color:white;">
                Created by Sanskriti Mittal
            </p>
        </div>
    """, unsafe_allow_html=True)