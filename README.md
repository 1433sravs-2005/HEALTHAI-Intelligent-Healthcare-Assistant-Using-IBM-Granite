# 🩺 HealthAI: Intelligent Healthcare Assistant Using IBM Granite

HealthAI is an AI-powered web app designed to offer intelligent healthcare assistance using Large Language Models (LLMs). Users can ask health-related questions, get disease predictions based on symptoms, receive treatment recommendations, and visualize health metrics.

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange?style=for-the-badge&logo=streamlit)
![IBM](https://img.shields.io/badge/Powered%20by-IBM%20Granite-blue?style=for-the-badge&logo=ibm)
![Status](https://img.shields.io/badge/Status-Under%20Development-yellow?style=for-the-badge)

---

## 🔥 Features

- 🗣️ **Patient Chat** – Ask any health-related question and get AI-generated responses
- 🔍 **Disease Prediction** – Input symptoms and receive likely conditions
- 💊 **Treatment Plan Generator** – Get personalized treatment suggestions
- 📊 **Health Analytics Dashboard** – Visualize health data using interactive graphs

---

## 🧠 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI Model**: IBM Granite 13B Instruct v2 (LLM)
- **Data Visualization**: Plotly, Pandas

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/1433sravs-2005/HEALTH-AI-USING-LOCAL-MODEL.git
cd HEALTH-AI-USING-LOCAL-MODEL

# Install dependencies
pip install -r requirements.txt

# Create a .env file with your IBM API credentials
# Example:
# API_KEY=your_ibm_api_key
# PROJECT_ID=your_ibm_project_id

# Run the app
streamlit run app.py
