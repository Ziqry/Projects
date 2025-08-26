import streamlit as st

# Title
st.title("🏡 Mortgage Calculator")

# User inputs
# --- Loan amount input with auto-formatting ---
loan_amount_str = st.text_input("Loan Amount (RM)", "200,000")

# Remove commas safely and reformat
try:
    loan_amount = float(loan_amount_str.replace(",", ""))
    # Reformat with commas
    formatted_amount = "{:,.0f}".format(loan_amount)
    if loan_amount_str != formatted_amount:
        # Update text input with formatted value
        st.session_state["loan_amount_str"] = formatted_amount
except ValueError:
    loan_amount = 0

# Re-render the input with the formatted value
loan_amount_str = st.text_input("Loan Amount (RM)", value="{:,.0f}".format(loan_amount) if loan_amount > 0 else "200,000", key="loan_amount_str")
loan_amount = float(loan_amount_str.replace(",", "")) if loan_amount_str.replace(",", "").isdigit() else 0
    
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



