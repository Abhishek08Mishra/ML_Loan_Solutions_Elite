import streamlit as st

def user_input():
    st.sidebar.header("Enter Applicant Details")
    income = st.sidebar.number_input("Income ($)", min_value=0, step=1000, value=100000, help="Enter your annual income.")
    credit_score = st.sidebar.slider("Credit Score", min_value=300, max_value=850, value=700,  help="Enter your credit score.")
    loan_amount = st.sidebar.number_input("Loan Amount ($)", min_value=0, step=1000, value=50000,  help="Enter the desired loan amount.")
    dti_ratio = st.sidebar.slider("Debt-to-Income Ratio (%)", min_value=0.0, max_value=100.0, value=30.0, help="Enter your debt-to-income ratio.")
    employment_status = st.sidebar.selectbox("Employment Status", ["Employed", "Unemployed"] ,help="Select your employment status.")
    employment_status_encoded = 1 if employment_status == "Employed" else 0
    
    user_text = st.text_area("Enter additional details (e.g., purpose of loan: I need the loan to start a small business).", "", help="Provide any additional information that might help in the loan approval process." )

    if not user_text.strip():
        st.warning("Please provide additional details to proceed with the prediction.")
        return None

    input_data = {
        "text": user_text,
        "structured": [income, credit_score, loan_amount, dti_ratio, employment_status_encoded]
    }

    return input_data

def add_footer():
    st.markdown("""
    <style>
        .footer {
            text-align: center;
            color: #00FF00;
            background-color: #000;
            padding: 10px;
            border-top: 2px solid #00FF00;
            font-family: 'Courier New', monospace;
        }
    </style>
    <div class='footer'>
        <p>⚡ <b>Created by The Passionate Data Scientist</b> 💀</p>
        <p>✨ <b>©️ 2025 All rights reserved.</b> Developed by <b>Abhishek Mishra</b> 💻</p>
        <p>💾 <i>Fueled by data, algorithms, and coffee ☕</i></p>
    </div>
    """, unsafe_allow_html=True)

def add_social_media_links():
    st.markdown("""
    <style>
        @keyframes glow {
            0% { text-shadow: 0 0 5px #00FF00, 0 0 10px #00FF00, 0 0 15px #00FF00; }
            50% { text-shadow: 0 0 10px #00FF00, 0 0 20px #00FF00, 0 0 30px #00FF00; }
            100% { text-shadow: 0 0 5px #00FF00, 0 0 10px #00FF00, 0 0 15px #00FF00; }
        }
        .social {
            text-align: center;
            color: #00FF00;
            background-color: #000;
            padding: 10px;
            border-top: 2px solid #00FF00;
            font-family: 'Courier New', monospace;
        }
        .social h3 {
            animation: glow 1.5s infinite alternate;
        }
    </style>
    <div class='social'>
        <h3>💀 Connect with me to enter into the matrix of data!</h3>
        <p>
            <a href='https://x.com/Abhi__57' target='_blank' style='color: #00FF00; text-decoration: none;'>🐦 Twitter</a> |
            <a href='https://www.linkedin.com/in/abhishek-mishra08/' target='_blank' style='color: #00FF00; text-decoration: none;'>💼 LinkedIn</a> |
            <a href='https://github.com/Abhishek08Mishra' target='_blank' style='color: #00FF00; text-decoration: none;'>💀 GitHub</a>
        </p>
        <p>💀 Follow the Data, Own the Algorithm! 🚀</p>
    </div>
    """, unsafe_allow_html=True)