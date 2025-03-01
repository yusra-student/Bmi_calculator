import streamlit as st

# Set page config
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

# Custom styles for better UI
st.markdown(
    """
    <style>
    .stApp { background-color: #f8f9fa; }
    .big-font { font-size:22px !important; font-weight:bold; }
    .success { color: green; font-weight: bold; }
    .warning { color: orange; font-weight: bold; }
    .danger { color: red; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True
)

# Title with an icon
st.title("⚖️ BMI Calculator")

# Weight input
weight = st.slider("Select your weight (in kgs)", min_value=20, max_value=200, value=70)

# Height format selection
status = st.radio("Select your height format:", ("Centimeters", "Meters", "Feet"))

# Height input with unit conversion
height = 0.0
if status == "Centimeters":
    height = st.slider("Enter height in cm", min_value=50, max_value=250, value=170) / 100  # Convert to meters
elif status == "Meters":
    height = st.slider("Enter height in meters", min_value=0.5, max_value=2.5, value=1.7)
elif status == "Feet":
    height = st.slider("Enter height in feet", min_value=1.0, max_value=8.0, value=5.6) / 3.28  # Convert to meters

# Calculate BMI
if height > 0:
    bmi = round(weight / (height ** 2), 2)
else:
    bmi = 0

# BMI Interpretation with Emoji Badges
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
st.markdown(f'<p class="{color} big-font">{emoji} {status_text}</p>', unsafe_allow_html=True)

# BMI Progress Bar
bmi_progress = min(bmi / 40, 1)  # Normalize BMI to fit in 0-1 range
st.progress(bmi_progress)

# Additional Health Tips
st.subheader("💡 Health Tips")
if bmi < 18.5:
    st.info("Eat more nutritious food and maintain a healthy diet 🍚🥗.")
elif bmi >= 25:
    st.info("Try exercising regularly and balancing your diet 🏃‍♂️🍎.")
else:
    st.success("Great job! Keep up your balanced lifestyle! 💪")
