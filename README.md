# 🩺 HealthAI: Intelligent Healthcare Assistant Using local models 

HealthAI is an AI-powered web app designed to offer intelligent healthcare assistance using Large Language Models (LLMs). Users can ask health-related questions, get disease predictions based on symptoms, receive treatment recommendations, and visualize health metrics.

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange?style=for-the-badge&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Under%20Development-yellow?style=for-the-badge)

---
> ⚠️ Note:
This project simulates IBM Granite integration using a local Hugging Face transformer model (`flan-t5-base`) due to lack of access to IBM API credentials.
The architecture and functionality are designed as per the IBM SmartInternz guidelines.

## 🔥 Features

- 🗣️ **Patient Chat** – Ask any health-related question and get AI-generated responses
- 🔍 **Disease Prediction** – Input symptoms and receive likely conditions
- 💊 **Treatment Plan Generator** – Get personalized treatment suggestions
- 📊 **Health Analytics Dashboard** – Visualize health data using interactive graphs

---

## 🧠 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI Model**: google/flan-t5-base
- **Data Visualization**: Plotly, Pandas

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/1433sravs-2005/HEALTH-AI-USING-LOCAL-MODEL.git
cd HEALTH-AI-USING-LOCAL-MODEL

# Install dependencies
pip install -r requirements.txt

#app.py
#add python code and ctrl+s

# Run the app
streamlit run app.py
