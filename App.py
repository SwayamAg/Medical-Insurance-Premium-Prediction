import numpy as np
import pickle as pkl
import streamlit as st

# Load the ML model
model = pkl.load(open('Insurance_ML.pkl', 'rb'))

# Set Page Configuration
st.set_page_config(page_title="Medical Insurance Premium Predictor", page_icon="🩺", layout="centered")

# Define Theme Toggle State using Session State
if "theme_mode" not in st.session_state:
    st.session_state["theme_mode"] = "light"

def toggle_theme():
    st.session_state["theme_mode"] = "dark" if st.session_state["theme_mode"] == "light" else "light"

theme_mode = st.session_state["theme_mode"]

# Define Colors for Light and Dark Modes
if theme_mode == "light":
    bg_color, text_color, slider_color, button_color, slider_thumb, success_color = (
        "#f9f9f9", "#1f1f1f", "#c3e5cc", "#7bbcff", "#ffa07a", "#196F3D"
    )
else:
    bg_color, text_color, slider_color, button_color, slider_thumb, success_color = (
        "#1E1E1E", "#F5F5F5", "#667b83", "#f48fb1", "#ffa07a", "#28B463"
    )

# Apply Custom Styling for Dynamic Theme
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    div.stSlider > div[data-baseweb="slider"] > div > div {{
        background: {slider_color};
    }}
    div.stSlider > div[data-baseweb="slider"] > div > div > div {{
        background: {slider_thumb};
    }}
    div.stButton > button {{
        color: white;
        background-color: {button_color};
        border-radius: 5px;
        border: none;
        font-size: 16px;
        padding: 10px 15px;
    }}
    .prediction-box {{
        background-color: {success_color};
        color: white;
        padding: 15px;
        border-radius: 5px;
        font-size: 18px;
        text-align: center;
    }}
    footer {{visibility: hidden;}}
    .footer {{
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: {button_color};
        color: white;
        text-align: center;
        padding: 10px;
    }}
    </style>
""", unsafe_allow_html=True)

# Header with Theme Toggle Button
col1, col2 = st.columns([4, 1])
col1.title("Medical Insurance Premium Predictor")
col2.button("Toggle Theme", on_click=toggle_theme)

st.write("This app estimates your medical insurance premium based on your age, BMI, region, and smoking habits.")

# Input Section in Columns
col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox('Choose Gender', ['Female', 'Male'])
    smoker = st.selectbox('Are you a smoker?', ['Yes', 'No'])

with col2:
    region = st.selectbox('Choose Region', ['SouthEast', 'SouthWest', 'NorthEast', 'NorthWest'])

age = st.slider('Enter Age', 5, 80, value=30, step=1)
bmi = st.slider('Enter BMI', 5, 100, value=25, step=1)
children = st.slider('Choose Number of Children', 0, 5, value=1)

# Predict Button Logic
if st.button('Predict Premium'):
    # Convert categorical to numerical for the model
    gender = 1 if gender == 'Female' else 0
    smoker = 1 if smoker == 'Yes' else 0
    region_dict = {'NorthWest': 0, 'NorthEast': 1, 'SouthEast': 2, 'SouthWest': 3}
    region = region_dict[region]

    # Prepare input and make predictions
    input_data = (age, gender, bmi, children, smoker, region)
    input_data_array = np.asarray(input_data).reshape(1, -1)
    predicted_prem = model.predict(input_data_array)

    # Display the rounded result in two decimal places with improved color
    st.markdown(
        f'<div class="prediction-box">Your Estimated Insurance Premium is: <strong>${predicted_prem[0]:.2f} USD</strong></div>',
        unsafe_allow_html=True,
    )

# Footer Section with Credits
st.markdown(f"""
    <div class="footer">
        Developed with ❤️ by SWAYAM AGARWAL. Follow me on 
        <a href="https://www.linkedin.com/in/swayam-agarwal/" target="_blank" style="color: white;">LinkedIn</a>.
    </div>
""", unsafe_allow_html=True)
