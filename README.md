# 🛠️ Oil Filter Condition Predictor — ML Powered Preventive Maintenance

A fully-featured **Machine Learning + Streamlit** application that predicts the condition of a vehicle’s oil filter using engine parameters, driving behavior, road conditions, and sensor readings.

This project includes:

- 🚗 Oil filter life prediction (classification)
- 🧠 Machine learning model (Random Forest)
- 🎨 Aesthetic dark-mode UI
- 📊 Dashboard & analytics pages
- 📈 Sensor visualization
- 🤖 Model insights & interpretability
- 🚀 One-file Streamlit app ready for Render deployment

---

## 🌟 Features

### 🔮 **Oil Filter Prediction**
Predicts one of the following filter health classes:

- 🟢 **Green** — Excellent  
- 🟢 **Light-Green** — Good  
- 🟡 **Yellow** — Inspect soon  
- 🟠 **Orange** — Service recommended  
- 🟠 **Dark-Orange** — Critical  
- 🔴 **Red** — Replace immediately  

### 📁 **Multi-Page App (Inside One File)**
- **Predictor**
- **Dashboard**
- **Sensor Analytics**
- **Model Insights**
- **About Project**

All handled via a **left sidebar navigation menu**.

### 🎨 **Aesthetic Premium UI**
- Clean dark theme  
- Glass-effect cards  
- Elegant typography  
- Smooth spacing & alignment  

---

## 🧠 Machine Learning Model

The ML pipeline uses:

- **Random Forest Classifier**
- Automatic preprocessing with:
  - StandardScaler
  - OneHotEncoder
- 2000-row synthetic dataset
- 1600 training / 400 testing split

Model file included:  
oil_filter_model.pkl


---

## 🚀 Deployment Guide (Render)

### 1️⃣ **Push these files to GitHub:**

app.py
oil_filter_model.pkl
requirements.txt
Dockerfile
environment.yml
.streamlit/config.toml

---

📊 Included Dashboard Pages
📈 Sensor Analytics

Visualizes oil temperature variation, viscosity trends, or RPM correlation.

📊 Maintenance Dashboard

High-level overview:

Total predictions

Avg filter age

Critical alerts count

Condition distribution chart

🤖 Model Insights

View feature importance

ML architecture transparency