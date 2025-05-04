import streamlit as st
import requests

st.set_page_config(page_title="Code Review Assistant", layout="wide")
st.title("🧠 Code Review Assistant")

st.markdown("Paste your code below and get AI-generated suggestions and improvements using DeepSeek-Coder.")

code_input = st.text_area("🔧 Your Code", height=300)

if st.button("🚀 Get Review"):
    if not code_input.strip():
        st.warning("Please paste your code first.")
    else:
        with st.spinner("Analyzing code..."):
            response = requests.post("http://localhost:8000/review/", data={"code": code_input})
            review = response.json().get("review", "No review returned.")
            st.subheader("📋 Review & Suggestions")
            st.code(review, language="text")