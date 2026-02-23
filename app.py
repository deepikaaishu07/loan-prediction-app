import streamlit as st
import joblib
import numpy as np

model = joblib.load("loan_model.pkl")

st.title("Loan Amount Prediction App")

# Inputs
dependents = st.number_input("Number of Dependents", 0, 10)
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_emp = st.selectbox("Self Employed", ["Yes", "No"])
income = st.number_input("Annual Income")
cibil = st.number_input("CIBIL Score", 300, 900)
res_asset = st.number_input("Residential Asset Value")
com_asset = st.number_input("Commercial Asset Value")
lux_asset = st.number_input("Luxury Asset Value")
bank_asset = st.number_input("Bank Asset Value")
loan_term = st.number_input("Loan Term (years)", 1, 30)

# Convert categorical to numbers
education = 1 if education == "Graduate" else 0
self_emp = 1 if self_emp == "Yes" else 0

# Prediction
if st.button("Predict Loan Amount"):
    data = np.array([[dependents, education, self_emp, income, cibil,
                      res_asset, com_asset, lux_asset, bank_asset,  loan_term]])
    
    prediction = model.predict(data)
    st.success(f"Predicted Loan Amount: ₹ {int(prediction[0])}")