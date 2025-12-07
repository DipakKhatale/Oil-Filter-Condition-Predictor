import streamlit as st
import pandas as pd
import joblib
import datetime

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(page_title="Oil Filter Predictor", page_icon="🛠️", layout="wide")

# ---------------------------------------------------------
# Aesthetic Premium Dark CSS
# ---------------------------------------------------------
st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #0e0f12 !important;
    color: #e8e8e8 !important;
    font-family: 'Segoe UI', sans-serif;
}

/* HEADER */
.header {
    background: linear-gradient(90deg, #1a1c20, #24272c);
    padding: 20px;
    border-radius: 14px;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.4);
}

.header h1 {
    margin: 0;
    font-size: 32px;
    font-weight: 700;
}

.header p {
    margin-top: 6px;
    font-size: 15px;
    color: #9ca3af;
}

/* CARD */
.main-card {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255,255,255,0.12);
    padding: 28px;
    border-radius: 18px;
    box-shadow: 0px 6px 35px rgba(0,0,0,0.45);
    backdrop-filter: blur(14px);
}

/* RESULT BOX */
.result-box {
    padding: 22px;
    border-radius: 16px;
    font-size: 22px;
    font-weight: 600;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.15);
    margin-top: 25px;
}

/* SIDEBAR */
.sidebar-title {
    font-size: 24px;
    font-weight: 700;
    padding-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Load Model
# ---------------------------------------------------------
model = joblib.load("oil_filter_model.pkl")

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
st.sidebar.markdown("<p class='sidebar-title'>📁 Navigation</p>", unsafe_allow_html=True)

PAGES = [
    "Predictor",
    "Dashboard",
    "Sensor Analytics",
    "Model Insights",
    "About"
]

selected_page = st.sidebar.radio("Go to:", PAGES)

# ---------------------------------------------------------
# Header (Appears on All Pages)
# ---------------------------------------------------------
st.markdown("""
<div class="header">
    <h1>🛠️ Oil Filter Condition Predictor</h1>
    <p>Aesthetic Multi-Page Dashboard · ML-Powered Analytics</p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# PAGE 1 — PREDICTOR
# =========================================================
if selected_page == "Predictor":

    st.markdown("<div class='main-card'>", unsafe_allow_html=True)

    st.subheader("Enter Vehicle & Sensor Inputs")

    vehicle_type = st.selectbox("Vehicle Type", ["SUV", "Sedan", "Hatchback", "LCV", "Truck", "Bus"])
    engine_capacity_cc = st.number_input("Engine Capacity (cc)", 800, 8000, value=2000)

    oil_filter_change_date = st.date_input("Oil Filter Change Date")
    current_date = datetime.date.today()
    oil_filter_age_days = (current_date - oil_filter_change_date).days
    st.write(f"📅 **Oil Filter Age:** {oil_filter_age_days} days")

    km_after_change = st.number_input("Kilometers Driven After Filter Change", 0, 300000, value=5000)

    road_type = st.selectbox("Road Type", ["city", "highway", "offroad", "mixed"])
    load_type = st.selectbox("Load Type", ["light", "medium", "heavy"])

    avg_oil_temperature = st.slider("Avg Oil Temperature (°C)", 60, 140, 90)
    oil_viscosity_index = st.slider("Oil Viscosity Index", 0, 100, 70)

    engine_rpm_avg = st.slider("Average Engine RPM", 600, 5000, 2200)
    idling_percentage = st.slider("Idling Percentage (%)", 0, 100, 10)
    ambient_temperature = st.slider("Ambient Temperature (°C)", -5, 60, 30)

    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    driving_style = st.selectbox("Driving Style", ["calm", "normal", "aggressive"])

    st.markdown("</div>", unsafe_allow_html=True)

    # Prepare Input for Model
    input_df = pd.DataFrame([{
        "vehicle_type": vehicle_type,
        "engine_capacity_cc": engine_capacity_cc,
        "oil_filter_age_days": oil_filter_age_days,
        "km_after_change": km_after_change,
        "road_type": road_type,
        "load_type": load_type,
        "avg_oil_temperature": avg_oil_temperature,
        "oil_viscosity_index": oil_viscosity_index,
        "engine_rpm_avg": engine_rpm_avg,
        "idling_percentage": idling_percentage,
        "ambient_temperature": ambient_temperature,
        "fuel_type": fuel_type,
        "driving_style": driving_style
    }])

    if st.button("Predict Filter Condition"):

        prediction = model.predict(input_df)[0]

        colors = {
            "Green": ("🟢", "#1f8a3a", "Excellent — Filter is fresh"),
            "Light-Green": ("🟢", "#3fbf5c", "Good — Recently changed"),
            "Yellow": ("🟡", "#bfa21f", "Moderate — Inspect soon"),
            "Orange": ("🟠", "#d48233", "Ageing — Service recommended"),
            "Dark-Orange": ("🟠", "#a85f23", "Critical — Replace soon"),
            "Red": ("🔴", "#b33636", "Replace Immediately")
        }

        icon, color, message = colors[prediction]

        st.markdown(
            f"""
            <div class='result-box' style='background-color:{color}22; color:{color};'>
                {icon} <br> {message}
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# PAGE 2 — DASHBOARD
# =========================================================
elif selected_page == "Dashboard":
    st.subheader("📊 Overall Maintenance Dashboard")

    st.metric("Total Predictions Made", 128)
    st.metric("Average Filter Age", "142 days")
    st.metric("Critical Alerts (Red)", 12)

    sample = pd.DataFrame({
        "Condition": ["Green", "Light-Green", "Yellow", "Orange", "Dark-Orange", "Red"],
        "Count": [40, 22, 33, 20, 8, 5]
    })

    st.bar_chart(sample.set_index("Condition"))


# =========================================================
# PAGE 3 — SENSOR ANALYTICS
# =========================================================
elif selected_page == "Sensor Analytics":
    st.subheader("📈 Sensor Analytics")

    df = pd.DataFrame({
        "Day": list(range(1, 11)),
        "Oil Temp": [80, 83, 86, 89, 92, 95, 98, 101, 103, 105]
    })

    st.line_chart(df, x="Day", y="Oil Temp")

    st.info("Higher oil temperatures accelerate filter degradation.")


# =========================================================
# PAGE 4 — MODEL INSIGHTS
# =========================================================
elif selected_page == "Model Insights":
    st.subheader("🤖 Model Insights")

    st.write("Model Type: ", type(model).__name__)

    try:
        features = model.named_steps["classifier"].feature_importances_
        st.bar_chart(features)
    except:
        st.warning("Feature importance not available for this model.")


# =========================================================
# PAGE 5 — ABOUT
# =========================================================
elif selected_page == "About":
    st.subheader("ℹ️ About This Project")
    st.write("""
### Overview
This application predicts **oil filter condition** using ML models trained on synthetic vehicle & sensor data.

### Technologies Used
- Python  
- Streamlit  
- Scikit-Learn  
- Random Forest  
- Custom UI & Analytics Dashboard  
""")
