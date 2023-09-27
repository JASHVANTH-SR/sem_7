import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# Function to calculate bond valuation
def bond_valuation(principal, coupon_rate, years_to_maturity, discount_rate):
    coupon_payment = principal * coupon_rate
    bond_value = 0

    for t in range(1, years_to_maturity + 1):
        bond_value += coupon_payment / ((1 + discount_rate) ** t)

    bond_value += principal / ((1 + discount_rate) ** years_to_maturity)
    return bond_value

# Function to calculate yield to maturity (YTM) using numerical methods (Newton's method)
def calculate_ytm(principal, coupon_rate, years_to_maturity, bond_price):
    guess = 0.05  # Initial guess for YTM
    max_iterations = 10000
    tolerance = 0.001

    for _ in range(max_iterations):
        bond_value = bond_valuation(principal, coupon_rate, years_to_maturity, guess)
        error = bond_value - bond_price

        if abs(error) < tolerance:
            return guess

        guess = guess - error / 1000  # Adjust the guess

    return None

# Function to calculate current yield
def current_yield(principal, coupon_rate, bond_price):
    coupon_payment = principal * coupon_rate
    return (coupon_payment / bond_price) * 100

# Function to calculate modified duration
def modified_duration(principal, coupon_rate, years_to_maturity, discount_rate):
    bond_value = bond_valuation(principal, coupon_rate, years_to_maturity, discount_rate)
    
    if bond_value == 0:
        return None  # Avoid division by zero
    
    macaulay_duration = 0

    for t in range(1, years_to_maturity + 1):
        present_value = (coupon_rate * principal / 100) / ((1 + discount_rate) ** t)
        macaulay_duration += (t * present_value)

    macaulay_duration += (years_to_maturity * (principal / ((1 + discount_rate) ** years_to_maturity)))
    return macaulay_duration / bond_value

# Streamlit app
st.title("Bond Valuation and Analytics Calculator")

# Input fields
principal = st.number_input("Principal Amount ($):", min_value=0)
coupon_rate = st.slider("Coupon Rate (%):", min_value=0.0, max_value=100.0, step=0.1)
years_to_maturity = st.number_input("Years to Maturity:", min_value=0, step=1)
discount_rate = st.slider("Discount Rate (%):", min_value=0.0, max_value=100.0, step=0.1)
bond_price = st.number_input("Current Bond Price ($):", min_value=0)

# Calculate bond value
bond_value = bond_valuation(principal, coupon_rate / 100, years_to_maturity, discount_rate / 100)

# Calculate Yield to Maturity (YTM)
ytm = calculate_ytm(principal, coupon_rate / 100, years_to_maturity, bond_price)

# Calculate Current Yield
current_yield_value = current_yield(principal, coupon_rate / 100, bond_price)

# Calculate Modified Duration
modified_duration_value = modified_duration(principal, coupon_rate / 100, years_to_maturity, discount_rate / 100)

# Display bond value, YTM, current yield, and modified duration
st.write(f"**Bond Value**: ${bond_value:.2f}")
if ytm is not None:
    st.write(f"**Yield to Maturity (YTM)**: {ytm * 100:.2f}%")
else:
    st.warning("YTM calculation did not converge. Please check inputs.")
st.write(f"**Current Yield**: {current_yield_value:.2f}%")
if modified_duration_value is not None:
    st.write(f"**Modified Duration**: {modified_duration_value:.2f} years")
else:
    st.warning("Modified duration calculation encountered an issue. Please check inputs.")

# Bond Price Sensitivity to Interest Rate
st.subheader("Bond Price Sensitivity to Interest Rate")

# Generate a range of interest rates
interest_rates = np.linspace(0, 10, 101)  # Interest rates from 0% to 10%
bond_values = [bond_valuation(principal, coupon_rate / 100, years_to_maturity, r) for r in interest_rates]

# Create a Plotly line plot
df = pd.DataFrame({'Interest Rate (%)': interest_rates, 'Bond Value ($)': bond_values})
fig = px.line(df, x='Interest Rate (%)', y='Bond Value ($)', title='Bond Price Sensitivity to Interest Rate')
st.plotly_chart(fig)

# Explanation using LaTeX
st.subheader("Formulas:")
st.latex(r"\text{Bond Valuation Formula:}")
st.latex(r"PV = \frac{C}{(1+r)^1} + \frac{C}{(1+r)^2} + \ldots + \frac{C}{(1+r)^n} + \frac{F}{(1+r)^n}")
st.latex(r"\text{Yield to Maturity (YTM):}")
st.latex(r"\text{Current Yield:}")
st.latex(r"\text{Modified Duration:}")

st.write("Where:")
st.latex(r"PV = \text{Present Value of the Bond}")
st.latex(r"C = \text{Annual Coupon Payment}")
st.latex(r"r = \text{Discount Rate per Period}")
st.latex(r"n = \text{Number of Years to Maturity}")
st.latex(r"F = \text{Face Value of the Bond}")
st.latex(r"\text{Yield to Maturity (YTM)} = ?")  # Provide explanation for YTM formula
st.latex(r"\text{Current Yield} = \frac{C}{\text{Current Bond Price}} \times 100\%")
st.latex(r"\text{Modified Duration} = \frac{\sum_{t=1}^{n} t \left(\frac{C \cdot P}{(1+r)^t}\right) + n \left(\frac{F}{(1+r)^n}\right)}{PV}")

# Additional Information
st.subheader("Additional Information:")
st.write("- Principal Amount: The initial amount of the bond.")
st.write("- Coupon Rate (%): The annual interest rate as a percentage of the bond's face value.")
st.write("- Years to Maturity: The number of years until the bond matures.")
st.write("- Discount Rate (%): The annual interest rate used to discount future cash flows.")
st.write("- Current Bond Price: The price at which the bond is currently trading in the market.")
st.write("- Modified Duration: A measure of the bond's sensitivity to changes in interest rates.")

# Applications and Usage
st.subheader("Applications and Usage:")
st.write("Bond valuation and analytics are essential in the following financial scenarios:")
st.write("- **Investment Decisions**: Investors use bond valuation to decide whether to buy or sell bonds in the market.")
st.write("- **Portfolio Management**: Portfolio managers assess the value of bonds in their portfolios and make allocation decisions.")
st.write("- **Risk Assessment**: Bond valuation helps in evaluating the risk associated with a bond investment.")
st.write("- **Financial Planning**: Individuals use bond valuation to plan for their long-term financial goals, such as retirement.")
st.write("- **Corporate Finance**: Companies use bond valuation when issuing or repurchasing bonds.")

# Color-coded tables
st.subheader("Key Metrics Summary:")
data = {
    "Metric": ["Bond Value", "Yield to Maturity (YTM)", "Current Yield", "Modified Duration"],
    "Value": [f"${bond_value:.2f}", f"{ytm * 100:.2f}%" if ytm is not None else "N/A", f"{current_yield_value:.2f}%" if current_yield_value is not None else "N/A", f"{modified_duration_value:.2f} years" if modified_duration_value is not None else "N/A"],
    "Color": ["green" if bond_value >= bond_price else "red", "green" if ytm is not None and ytm >= (coupon_rate / 100) else "red", "green" if current_yield_value is not None and current_yield_value >= (coupon_rate * 100) else "red", "green" if modified_duration_value is not None and modified_duration_value >= 0 else "red"]
}

df = pd.DataFrame(data)
st.dataframe(df.style.applymap(lambda x: f"background-color: {'green' if x == 'green' else 'red'}", subset=["Color"]))

# Disclaimer
st.write("This calculator provides an approximate bond valuation, YTM calculation, current yield, and modified duration. It does not consider various factors that can affect bond prices in the real world.")

# References
st.subheader("References:")
st.write("- Investopedia: [Bond Valuation](https://www.investopedia.com/terms/b/bond-valuation.asp)")
st.write("- Investopedia: [Yield to Maturity (YTM)](https://www.investopedia.com/terms/y/yieldtomaturity.asp)")
st.write("- Investopedia: [Current Yield](https://www.investopedia.com/terms/c/currentyield.asp)")
st.write("- Investopedia: [Modified Duration](https://www.investopedia.com/terms/m/modifiedduration.asp)")
