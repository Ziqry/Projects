import streamlit as st

# Title
st.title("🏡 Mortgage Calculator")

# User inputs
loan_amount = st.number_input("Loan Amount (RM)", min_value=1000, step=1000, value=300000)
interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.1, step=0.1, value=3.5)
loan_years = st.number_input("Loan Term (years)", min_value=1, step=1, value=30)

# Calculate mortgage
monthly_rate = (interest_rate / 100) / 12
num_payments = loan_years * 12

if monthly_rate > 0:
    monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
else:
    monthly_payment = loan_amount / num_payments

# Show results
st.subheader("📊 Results")
st.write(f"**Monthly Payment:** RM {monthly_payment:,.2f}")
st.write(f"**Total Payment:** RM {monthly_payment * num_payments:,.2f}")
st.write(f"**Total Interest:** RM {(monthly_payment * num_payments) - loan_amount:,.2f}")




