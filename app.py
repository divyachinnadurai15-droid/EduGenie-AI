import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Page configuration
st.set_page_config(page_title="EduGenie - AI Study Assistant", page_icon="🎓", layout="centered")

st.title("🎓 EduGenie - AI Study Assistant")
st.write("Generate customized study notes, explanations, and practice questions instantly!")

# API Key handling (Streamlit Secrets or Environment Variable)
api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))

if not api_key:
    st.error("⚠️ GEMINI_API_KEY not found. Please add it to your Streamlit secrets or environment variables.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# User Inputs
topic = st.text_input("Enter the Topic or Subject:", placeholder="e.g., Photosynthesis, Python Loops, Newton's Laws")
level = st.selectbox("Select Difficulty / Level:", ["Beginner / School Level", "Intermediate / College Level", "Advanced"])
task = st.radio("Choose what you need:", ["Comprehensive Notes", "Key Concepts & Summary", "Practice Questions & Quiz"])

if st.button("Generate with AI"):
    if not topic.strip():
        st.warning("Please enter a topic first!")
    else:
        with st.spinner("EduGenie is thinking..."):
            prompt = f"Act as an expert tutor. Provide {task} on the topic '{topic}' suitable for {level}. Make it well-structured, clear, and easy to study."
            try:
                response = model.generate_content(prompt)
                st.success("Here are your study materials:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error generating response: {e}")
