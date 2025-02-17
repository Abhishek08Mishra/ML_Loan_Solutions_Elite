import joblib
import numpy as np
import streamlit as st

@st.cache_data
def load_model():
    """
    Loading pre-trained model (Random_Forest_model.pkl, scaler_model.pkl and TfidfVectorizer_model.pkl) .
    """
    try:
        model = joblib.load("Random_Forest_model.pkl")
        scaler = joblib.load("scaler_model.pkl")
        vectorizer = joblib.load("TfidfVectorizer_model.pkl")
        return model , scaler, vectorizer
    except Exception as e:
        print(f"Error loading model, scaler, or vectorizer: {e}")
        return None, None, None

def preprocess_input(input_data, scaler, vectorizer):

    user_text = input_data["text"]
    structured_features = input_data["structured"]
    X_text = vectorizer.transform([user_text]).toarray()
    scaled_structured = scaler.transform([structured_features])
    combined_features = np.hstack((X_text[0], scaled_structured[0]))
    return combined_features

def predict_loan_approval(model, input_data):
    return model.predict([input_data])[0]