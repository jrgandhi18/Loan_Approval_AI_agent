import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from groq import Groq

# 1. Setup Groq
load_dotenv("api_key_groq.env")
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# Page Config
st.set_page_config(page_title="AI Loan Predictor", layout="centered")

st.title("🏦 Real-Time AI Loan Predictor")
st.markdown("Apni details bhariye aur AI se instant approval check kijiye.")

# --- INPUT FORM ---
with st.form("loan_form"):
    st.subheader("📝 Applicant Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        loan_id = st.text_input("Loan ID", value="LP001")
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        income = st.number_input("Applicant Monthly Income ($)", min_value=0, value=5000)

    with col2:
        co_income = st.number_input("Co-applicant Income ($)", min_value=0, value=0)
        loan_amt = st.number_input("Loan Amount (in thousands)", min_value=0, value=150)
        term = st.number_input("Loan Term (Days)", min_value=0, value=360)
        credit_history = st.selectbox("Credit History", [1, 0], help="1 for Good, 0 for Bad")
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

    submit_button = st.form_submit_button(label="Analyze Loan Approval 🚀")

# --- AI LOGIC ---
if submit_button:
    total_income = income + co_income
    
    # AI Prompt
    prompt = f"""
    Analyze this loan application and give a FINAL decision:
    - Loan ID: {loan_id}
    - Total Income: {total_income}
    - Loan Amount: {loan_amt}
    - Credit History: {credit_history}
    - Education: {education}
    - Property Area: {property_area}
    
    Format:
    [Decision: Approved/Rejected]
    Reason: 1 clear sentence.
    """
    
    with st.spinner('AI analysis kar raha hai...'):
        try:
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )
            result = completion.choices[0].message.content
            
            st.divider()
            st.subheader("🤖 AI Decision")
            
            # Styling based on approval
            if "Approved" in result:
                st.success(result)
            else:
                st.error(result)
                
        except Exception as e:
            st.error(f"Error: {e}")

# Footer
st.info("Note: This is an AI-generated decision based on provided parameters.")