import streamlit as st

st.markdown('<style>' + open('styles.css').read() + '</style>', unsafe_allow_html=True)

st.title("Custom CSS on Streamlit")
st.button(label = "Test Button")