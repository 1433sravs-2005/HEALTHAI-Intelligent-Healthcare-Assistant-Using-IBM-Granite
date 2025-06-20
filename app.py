import os
import streamlit as st
from transformers import pipeline
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv

# Set cache and environment config
os.environ["HF_HOME"] = "D:/HF_CACHE"
os.environ["TRANSFORMERS_NO_TF"] = "1"
load_dotenv()

# Streamlit page config
st.set_page_config(page_title="HealthAI Assistant", page_icon="🩺", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #eef2f3, #8e9eab);
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton>button {
        background-color: #2b4162;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
        transition: 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #1a2738;
    }
    .stTextArea textarea, .stTextInput input {
        border: 2px solid #2b4162;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("<h2 style='text-align: center; color: #2b4162;'>🧠 HealthAI: Intelligent Healthcare Assistant</h2>", unsafe_allow_html=True)

# Sidebar navigation
menu = ["🩺 Disease Finder", "💬 Private Chat", "💊 Medication Suggestions", "📋 Treatment Plans", "📊 Health Analytics"]
choice = st.sidebar.selectbox("🔍 Choose a Feature", menu)

# Load stable working model
@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        tokenizer="google/flan-t5-base",
        max_new_tokens=200
    )

generator = load_model()

# Function to remove repeated lines and repeated words
import re
def clean_response(text):
    lines = text.split('\n')
    seen = set()
    cleaned = []
    for line in lines:
        line = line.strip()
        line = re.sub(r'\b(\w+)( \1\b)+', r'\1', line)  # remove repeated words
        if line and line not in seen:
            cleaned.append(line)
            seen.add(line)
    return '\n'.join(cleaned)

# === Disease Finder ===
if choice == "🩺 Disease Finder":
    st.subheader("📝 Enter Symptoms")
    user_input = st.text_area("Describe your symptoms (e.g. headache, fever, fatigue):")

    if st.button("🔍 Predict Disease"):
        if user_input.strip():
            with st.spinner("🧠 Analyzing symptoms..."):
                prompt = f"You are a medical expert. Given the symptoms: {user_input}, list the most likely disease in one line."
                result = generator(prompt)[0]['generated_text']
                st.success("✅ Disease Prediction")
                st.markdown(f"**Prediction:** {clean_response(result.strip())}")
        else:
            st.warning("⚠️ Please enter your symptoms.")

# === Private Chat ===
elif choice == "💬 Private Chat":
    st.subheader("💬 Ask Your Health Question")
    question = st.text_area("Type your question below:")

    if st.button("💡 Get Answer"):
        if question.strip():
            with st.spinner("🤖 Thinking..."):
                prompt = f"Answer the following medical question accurately and simply: {question}"
                response = generator(prompt)[0]['generated_text']
                st.success("✅ Response:")
                st.markdown(clean_response(response.strip()))
        else:
            st.warning("⚠️ Please enter a valid question.")

# === Medication Suggestions ===
elif choice == "💊 Medication Suggestions":
    st.subheader("💊 Get Medication Suggestions")
    condition = st.text_input("Enter your disease or condition:")

    if st.button("🧾 Suggest Medications"):
        if condition.strip():
            with st.spinner("🔬 Finding medications..."):
                prompt = f"List exactly 3 different generic medications used to treat {condition}. Do not repeat or explain."
                response = generator(prompt)[0]['generated_text']
                st.success("✅ Medication Suggestions:")
                st.markdown(clean_response(response.strip()))
        else:
            st.warning("⚠️ Please enter a condition.")

# === Treatment Plans ===
elif choice == "📋 Treatment Plans":
    st.subheader("📋 Generate Treatment Plan")
    condition = st.text_input("Enter your diagnosed condition:")

    if st.button("📝 Get Plan"):
        if condition.strip():
            with st.spinner("⚕️ Generating treatment plan..."):
                prompt = f"You are a doctor. Write a structured treatment plan for {condition}. Include: 1) Medications, 2) Lifestyle tips, 3) Required tests. Keep it short and avoid repetition."
                response = generator(prompt)[0]['generated_text']
                st.success("✅ Treatment Plan:")
                st.markdown(clean_response(response.strip()))
        else:
            st.warning("⚠️ Please enter a condition.")

# === Health Analytics ===
elif choice == "📊 Health Analytics":
    st.subheader("📊 Weekly Health Stats")
    df = pd.DataFrame({
        "Date": pd.date_range(start="2024-01-01", periods=7),
        "Heart Rate": [72, 76, 80, 75, 78, 82, 77],
        "Blood Pressure": [120, 118, 119, 121, 117, 116, 122],
        "Blood Sugar": [90, 92, 89, 88, 94, 91, 87],
    })
    st.dataframe(df)
    st.markdown("### 📈 Health Summary")
    avg_hr = df["Heart Rate"].mean()
    avg_bp = df["Blood Pressure"].mean()
    avg_sugar = df["Blood Sugar"].mean()
    st.info(f"**Average Heart Rate:** {avg_hr:.1f} bpm\n\n**Average Blood Pressure:** {avg_bp:.1f} mmHg\n\n**Average Blood Sugar:** {avg_sugar:.1f} mg/dL")
    st.plotly_chart(px.line(df, x="Date", y="Heart Rate", title="Heart Rate Over Time"))
    st.plotly_chart(px.line(df, x="Date", y="Blood Pressure", title="Blood Pressure Over Time"))
    st.plotly_chart(px.line(df, x="Date", y="Blood Sugar", title="Blood Sugar Over Time"))
