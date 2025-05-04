import streamlit as st
import requests

# Set the page layout to wide mode for better spacing
st.set_page_config(page_title="Code Review Assistant", layout="wide")

# Title and introductory text
st.title("🧠 Code Review Assistant (DeepSeek-Coder)")
st.markdown("""
    Welcome to the **Code Review Assistant**!  
    Paste your code below, and our AI-powered tool will analyze it and provide feedback, suggestions, and improvements.  
    Get valuable insights into your code quality, potential bugs, and optimization tips.
""", unsafe_allow_html=True)

# Code input with an enhanced style
code_input = st.text_area(
    "🔧 Your Code",
    height=350,
    placeholder="Paste your code here...",
    help="Paste the code you want to review. The more code you paste, the better the AI review will be.",
    max_chars=5000
)

# Add a custom button with a nice style
if st.button("🚀 Get Review", help="Click to get code review"):
    if not code_input.strip():
        st.warning("Please paste your code first.")
    else:
        with st.spinner("Analyzing code... Please wait..."):
            try:
                response = requests.post("http://localhost:8000/review/", data={"code": code_input})
                response.raise_for_status()
                review = response.json().get("review", "No review returned.")
                
                # Display the review results in a beautiful layout
                st.subheader("📋 Review & Suggestions")
                st.markdown("""
                    **Here are some helpful suggestions for your code:**
                """, unsafe_allow_html=True)
                st.code(review, language="python")
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {str(e)}")

# Add footer section with some useful links or text
st.markdown("""
    ---
    <div style="text-align:center; font-size:14px;">
        Created by <b>Hardik Sankhla</b> | Code Review Assistant powered by <b>DeepSeek-Coder</b><br>
        <a href="https://github.com/yourusername/code-review-deepseek" target="_blank">Visit the GitHub Repository</a>
    </div>
""", unsafe_allow_html=True)

# Add custom CSS to style the app and make it more visually appealing
st.markdown("""
    <style>
        .stTextInput textarea {
            font-family: 'Courier New', monospace;
            font-size: 16px;
            padding: 12px;
        }
        .stButton>button {
            background-color: #4a0b8c;
            color: white;
            font-weight: bold;
            font-size: 16px;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #6a0db2;
        }
        .stMarkdown {
            font-family: 'Arial', sans-serif;
            font-size: 16px;
            line-height: 1.5;
            color: #333;
        }
        .stSpinner {
            color: #4a0b8c;
        }
        .stCode {
            background-color: #f5f5f5;
            padding: 16px;
            border-radius: 8px;
            font-size: 14px;
            font-family: 'Courier New', monospace;
        }
        .stText {
            color: #4a0b8c;
        }
    </style>
""", unsafe_allow_html=True)
