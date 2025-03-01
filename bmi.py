import streamlit as st

# Set page config
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="wide")

# Custom styles for better UI
st.markdown(
    """
    <style>
    .stApp { background-color: #f8f9fa; overflow-x: hidden; }
    .big-font { font-size:18px !important; font-weight:bold; }
    .success, .warning, .danger { font-weight: bold; }
    </style>
    """, unsafe_allow_html=True
)

# Title with an icon
st.title("⚖️ BMI Calculator")

# Weight input
weight = st.slider("Select your weight (kg)", 20, 200, 70, help="Slide to select your weight")

# Height format selection
status = st.radio("Select your height format:", ("Centimeters", "Meters", "Feet"))

# Height input with unit conversion
if status == "Centimeters":
    height = st.slider("Enter height in cm", 50, 250, 170, help="Slide to select your height") / 100
elif status == "Meters":
    height = st.slider("Enter height in meters", 0.5, 2.5, 1.7)
elif status == "Feet":
    height = st.slider("Enter height in feet", 1.0, 8.0, 5.6) / 3.28

# Calculate BMI
bmi = round(weight / (height ** 2), 2) if height > 0 else 0

# BMI Interpretation
if bmi < 16:
    status_text, color, emoji = "Extremely Underweight", "danger", "⚠️"
elif bmi < 18.5:
    status_text, color, emoji = "Underweight", "warning", "🥗"
elif bmi < 25:
    status_text, color, emoji = "Healthy", "success", "✅"
elif bmi < 30:
    status_text, color, emoji = "Overweight", "warning", "🍔"
else:
    status_text, color, emoji = "Extremely Overweight", "danger", "⚠️"

# Display results
st.metric(label="Your BMI", value=f"{bmi}")

# Display status with color coding
st.write(f"### {emoji} {status_text}")

# BMI Progress Bar (Mobile-Friendly)
col1, col2 = st.columns([3, 1])
col1.progress(min(bmi / 40, 1))
col2.write(f"**{bmi}** BMI")

# Additional Health Tips
st.subheader("💡 Health Tips")
if bmi < 18.5:
    st.info("Eat more nutritious food and maintain a healthy diet 🍚🥗.")
elif bmi >= 25:
    st.info("Try exercising regularly and balancing your diet 🏃‍♂️🍎.")
else:
    st.success("Great job! Keep up your balanced lifestyle! 💪")
