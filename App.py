import numpy as np
import streamlit as st
import requests
import json

# API Configuration
API_BASE_URL = "https://f-api-production.up.railway.app"
PREDICT_ENDPOINT = f"{API_BASE_URL}/predict"

# Set Page Configuration
st.set_page_config(
    page_title="Medical Insurance Premium Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark Mode Colors Only
bg_color, text_color, primary_color, secondary_color, accent_color, success_color, error_color = (
    "#0f172a", "#f8fafc", "#3b82f6", "#60a5fa", "#93c5fd", "#10b981", "#ef4444"
)
input_bg = "#1e293b"
border_color = "#475569"

# Apply Custom Styling for Modern Medical Insurance Theme
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, {bg_color} 0%, {secondary_color}15 100%);
        color: {text_color};
    }}
    
    /* Header Styling */
    .main-header {{
        background: linear-gradient(90deg, {primary_color}, {accent_color});
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }}
    
    /* Card Styling */
    .stCard {{
        background: {bg_color};
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border: 1px solid {secondary_color}30;
    }}
    
    /* Input Styling */
    .stSelectbox > div > div {{
        background: {input_bg};
        border: 2px solid {border_color};
        border-radius: 10px;
        color: {text_color} !important;
    }}
    
    .stSelectbox > div > div > div {{
        color: {text_color} !important;
    }}
    
    /* Selectbox dropdown styling */
    .stSelectbox [data-baseweb="select"] {{
        background: {input_bg} !important;
        color: {text_color} !important;
    }}
    
    .stSelectbox [data-baseweb="select"]:hover {{
        border-color: {primary_color} !important;
    }}
    
    .stSlider > div[data-baseweb="slider"] > div > div {{
        background: {primary_color};
        border-radius: 10px;
    }}
    
    .stSlider > div[data-baseweb="slider"] > div > div > div {{
        background: {accent_color};
        border: 3px solid {primary_color};
    }}
    
    /* Text input styling */
    .stTextInput > div > div > input {{
        color: {text_color} !important;
        background: {input_bg} !important;
        border: 2px solid {border_color} !important;
    }}
    
    /* Label styling */
    .stSelectbox label, .stSlider label {{
        color: {text_color} !important;
        font-weight: 600;
    }}
    
    /* Dropdown options */
    .stSelectbox [data-baseweb="select"] {{
        color: {text_color} !important;
    }}
    
    /* Ensure proper contrast for all text elements */
    .stMarkdown, .stText, p, h1, h2, h3, h4, h5, h6 {{
        color: {text_color} !important;
    }}
    
    /* Additional Streamlit element styling for light mode */
    .stSelectbox [data-baseweb="select"] > div {{
        background: {input_bg} !important;
        color: {text_color} !important;
    }}
    
    .stSelectbox [data-baseweb="select"] > div > div {{
        color: {text_color} !important;
    }}
    
    /* Slider value display */
    .stSlider [data-baseweb="slider"] + div {{
        color: {text_color} !important;
    }}
    
    /* Help text styling */
    .stSelectbox [data-testid="stMarkdown"] {{
        color: {text_color} !important;
    }}
    
    /* Button Styling */
    .stButton > button {{
        background: linear-gradient(90deg, {primary_color}, {accent_color});
        color: white;
        border-radius: 25px;
        border: none;
        font-size: 16px;
        font-weight: 600;
        padding: 12px 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }}
    
    /* Prediction Box Styling */
    .prediction-box {{
        background: linear-gradient(135deg, {success_color}, {success_color}dd);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        font-size: 20px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        border: 2px solid {success_color}40;
        margin: 1rem 0;
    }}
    
    .error-box {{
        background: linear-gradient(135deg, {error_color}, {error_color}dd);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        font-size: 16px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        border: 2px solid {error_color}40;
    }}
    
    /* Info Box Styling */
    .info-box {{
        background: linear-gradient(135deg, {secondary_color}20, {primary_color}20);
        border: 1px solid {secondary_color}40;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
    }}
    
    /* Footer Styling */
    .footer {{
        background: linear-gradient(90deg, {primary_color}, {accent_color});
        color: white;
        text-align: center;
        padding: 1rem;
        border-radius: 10px;
        margin-top: 2rem;
        box-shadow: 0 -4px 15px rgba(0,0,0,0.1);
    }}
    
    /* Hide default footer */
    footer {{visibility: hidden;}}
    
    /* Responsive Design */
    @media (max-width: 768px) {{
        .main-header {{
            padding: 1rem;
            font-size: 1.5rem;
        }}
    }}
    </style>
""", unsafe_allow_html=True)

# Main Header with Medical Insurance Theme
st.markdown(f"""
    <div class="main-header">
        <h1 style="margin: 0; font-size: 2.5rem; font-weight: 700;">
            🏥 Medical Insurance Premium Predictor
        </h1>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.1rem; opacity: 0.9;">
            AI-Powered Premium Estimation for Health Insurance
        </p>
    </div>
""", unsafe_allow_html=True)

# Sidebar Content
with st.sidebar:
    st.markdown("### 📊 About")
    st.markdown("""
    This AI-powered application estimates your medical insurance premium based on:
    - **Demographics**: Age, Gender, Region
    - **Health Factors**: BMI, Smoking Status
    - **Family**: Number of Children
    
    The prediction uses advanced machine learning algorithms trained on comprehensive insurance data.
    """)
    
    st.markdown("---")
    st.markdown("### 🔗 API Status")
    try:
        response = requests.get(f"{API_BASE_URL}/", timeout=5)
        if response.status_code == 200:
            st.success("✅ API Connected")
        else:
            st.error("❌ API Error")
    except:
        st.warning("⚠️ API Unavailable")

# Main Content Area
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📋 Personal Information")
    
    # Input Section in a modern card layout
    with st.container():
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("#### 👤 Demographics")
            gender = st.selectbox('Gender', ['Female', 'Male'], help="Select your gender")
            age = st.slider('Age', 18, 80, value=30, step=1, help="Enter your age")
            region = st.selectbox('Region', ['SouthEast', 'SouthWest', 'NorthEast', 'NorthWest'], help="Select your region")
        
        with col_b:
            st.markdown("#### 🏥 Health Information")
            bmi = st.slider('BMI (Body Mass Index)', 15.0, 50.0, value=25.0, step=0.1, help="Enter your BMI")
            smoker = st.selectbox('Smoking Status', ['No', 'Yes'], help="Are you a smoker?")
            children = st.slider('Number of Children', 0, 10, value=1, help="Number of children in your family")

# Prediction Section
st.markdown("---")
st.markdown("### 🎯 Premium Prediction")

# Predict Button with enhanced styling
if st.button('🚀 Calculate Premium', use_container_width=True):
    try:
        # Convert inputs to API format
        sex = gender.lower()
        smoker_status = smoker.lower()
        region_lower = region.lower()
        
        # Prepare API request data
        api_data = {
            "age": age,
            "sex": sex,
            "bmi": float(bmi),
            "children": children,
            "smoker": smoker_status,
            "region": region_lower
        }
        
        # Make API request with loading animation
        with st.spinner('🔍 Analyzing your profile and calculating premium...'):
            response = requests.post(PREDICT_ENDPOINT, json=api_data, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if "predicted_premium" in result:
                predicted_prem = result["predicted_premium"]
                
                # Enhanced prediction display
                st.markdown(f"""
                    <div class="prediction-box">
                        <h2 style="margin: 0 0 1rem 0; font-size: 1.5rem;">💰 Estimated Premium</h2>
                        <h1 style="margin: 0; font-size: 3rem; font-weight: 700;">${predicted_prem:.2f}</h1>
                        <p style="margin: 0.5rem 0 0 0; font-size: 1rem; opacity: 0.9;">USD per month</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Additional information
                st.markdown(f"""
                    <div class="info-box">
                        <h4>📊 Premium Breakdown:</h4>
                        <ul>
                            <li><strong>Age Factor:</strong> {age} years old</li>
                            <li><strong>Health Status:</strong> {'Smoker' if smoker == 'Yes' else 'Non-smoker'}</li>
                            <li><strong>BMI Category:</strong> {'Underweight' if bmi < 18.5 else 'Normal' if bmi < 25 else 'Overweight' if bmi < 30 else 'Obese'}</li>
                            <li><strong>Family Size:</strong> {children} children</li>
                            <li><strong>Region:</strong> {region}</li>
                        </ul>
                    </div>
                """, unsafe_allow_html=True)
                
            else:
                st.markdown(f"""
                    <div class="error-box">
                        <h3>❌ Prediction Error</h3>
                        <p>{result.get("error", "Unknown error occurred")}</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="error-box">
                    <h3>🌐 API Connection Error</h3>
                    <p>Status {response.status_code}: {response.text}</p>
                </div>
            """, unsafe_allow_html=True)
            
    except requests.exceptions.RequestException as e:
        st.markdown(f"""
            <div class="error-box">
                <h3>🌐 Connection Error</h3>
                <p>Unable to connect to the prediction service. Please check your internet connection and try again.</p>
            </div>
        """, unsafe_allow_html=True)
        st.error(f"Technical details: {str(e)}")
    except Exception as e:
        st.markdown(f"""
            <div class="error-box">
                <h3>⚠️ Unexpected Error</h3>
                <p>Something went wrong during the prediction process. Please try again.</p>
            </div>
        """, unsafe_allow_html=True)
        st.error(f"Technical details: {str(e)}")

# Footer with enhanced styling
st.markdown(f"""
    <div class="footer">
        <p style="margin: 0; font-size: 1rem;">
            🚀 Developed with ❤️ by <strong>SWAYAM AGARWAL</strong> | 
            <a href="https://www.linkedin.com/in/swayam-agarwal/" target="_blank" style="color: white; text-decoration: underline;">LinkedIn</a> |
            <a href="https://f-api-production.up.railway.app/docs" target="_blank" style="color: white; text-decoration: underline;">API Documentation</a>
        </p>
    </div>
""", unsafe_allow_html=True)
