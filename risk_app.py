import streamlit as st
import pandas as pd

# Function to calculate CVSS score
def calculate_cvss_score(impact, exploitability, complexity):
    # Formula for CVSS Base Score
    base_score = round(impact * exploitability * complexity, 2)
    return base_score

# Function to calculate a basic risk assessment score using a custom formula
def calculate_custom_risk_score(likelihood, impact):
    # Custom formula for risk score
    risk_score = likelihood * impact
    return risk_score

# Function to calculate Mean Time to Identify (MTTI) based on input parameters
def calculate_mtti(recovery_time, detection_probability):
    mtti = recovery_time / (1 - detection_probability)
    return mtti

# Function to calculate Mean Time to Contain (MTTC) based on input parameters
def calculate_mttc(recovery_time, containment_probability):
    mttc = recovery_time / (1 - containment_probability)
    return mttc

# Function to calculate risk using the formula Risk = Likelihood * Impact + Threat * Vulnerability
def calculate_combined_risk(likelihood, impact, threat, vulnerability):
    risk_score = likelihood * impact + threat * vulnerability
    return risk_score

# Streamlit UI
st.title("Information Security Risk Assessment")

# Description of the application
st.markdown(
    """
    It allows us to calculate risk scores 
    using various methods, including the Common Vulnerability Scoring System (CVSS), a custom risk assessment model, 
    Mean Time to Identify (MTTI), Mean Time to Contain (MTTC), and a combined risk assessment method.
    
    ## Common Vulnerability Scoring System (CVSS)
    
    CVSS is a widely used framework for assessing the severity of security vulnerabilities. It takes into account 
    three parameters:
    
    - **Impact**: The impact of a security vulnerability on your organization (0.0 - 10.0).
    - **Exploitability**: The ease with which an attacker can exploit the vulnerability (0.0 - 10.0).
    - **Complexity**: The complexity of the attack required to exploit the vulnerability (0.0 - 10.0).
    
    The CVSS Base Score is calculated using the formula:
    
    """
)
st.latex("CVSS Base Score = \\text{Impact} \\times \\text{Exploitability} \\times \\text{Complexity}")

st.markdown(
    """
    ## Custom Risk Assessment
    
    You can perform a custom risk assessment using the following parameters:
    
    - **Likelihood**: The likelihood of a security incident occurring (0.0 - 1.0).
    - **Impact**: The impact of the security incident on your organization (0.0 - 10.0).
    
    The custom risk assessment score is calculated using a simple formula:
    
    """
)
st.latex("Risk Score = \\text{Likelihood} \\times \\text{Impact}")

st.markdown(
    """
    ## Mean Time to Identify (MTTI)
    
    MTTI represents the average time it takes to identify a security incident. You can calculate it using the formula:
    
    """
)
st.latex("MTTI = \\frac{\\text{Recovery Time}}{1 - \\text{Detection Probability}}")

st.markdown(
    """
    ## Mean Time to Contain (MTTC)
    
    MTTC represents the average time it takes to contain a security incident. You can calculate it using the formula:
    
    """
)
st.latex("MTTC = \\frac{\\text{Recovery Time}}{1 - \\text{Containment Probability}}")

st.markdown(
    """
    ## Combined Risk Assessment
    
    You can calculate risk using the formula:
    
    """
)
st.latex("Risk = \\text{Likelihood} \\times \\text{Impact} + \\text{Threat} \\times \\text{Vulnerability}")

# Sidebar for user inputs
st.sidebar.header("CVSS Parameters")
impact_cvss = st.sidebar.slider("CVSS Impact (0.0 - 10.0)", 0.0, 10.0, 5.0, key="cvss_impact")
exploitability_cvss = st.sidebar.slider("Exploitability (0.0 - 10.0)", 0.0, 10.0, 5.0, key="cvss_exploit")
complexity_cvss = st.sidebar.slider("Complexity (0.0 - 10.0)", 0.0, 10.0, 5.0, key="cvss_complexity")

st.sidebar.header("Custom Risk Assessment Parameters")
likelihood_custom = st.sidebar.slider("Likelihood (0.0 - 1.0)", 0.0, 1.0, 0.5, key="custom_likelihood")
impact_custom = st.sidebar.slider("Custom Impact (0.0 - 10.0)", 0.0, 10.0, 5.0, key="custom_impact")

st.sidebar.header("MTTI Parameters")
recovery_time = st.sidebar.slider("Recovery Time (hours)", 1, 24, 12, key="mtti_recovery_time")
detection_probability = st.sidebar.slider("Detection Probability (0.0 - 1.0)", 0.0, 1.0, 0.7, key="mtti_detection_prob")

st.sidebar.header("MTTC Parameters")
containment_probability = st.sidebar.slider("Containment Probability (0.0 - 1.0)", 0.0, 1.0, 0.8, key="mttc_containment_prob")

st.sidebar.header("Combined Risk Assessment Parameters")
likelihood_combined = st.sidebar.slider("Likelihood (0.0 - 1.0)", 0.0, 1.0, 0.5, key="combined_likelihood")
impact_combined = st.sidebar.slider("Impact (0.0 - 10.0)", 0.0, 10.0, 5.0, key="combined_impact")
threat_combined = st.sidebar.slider("Threat (0.0 - 1.0)", 0.0, 1.0, 0.3, key="combined_threat")
vulnerability_combined = st.sidebar.slider("Vulnerability (0.0 - 1.0)", 0.0, 1.0, 0.4, key="combined_vulnerability")

if st.sidebar.button("Assess CVSS Risk"):
    # Perform risk assessment using CVSS formula
    cvss_score = calculate_cvss_score(impact_cvss, exploitability_cvss, complexity_cvss)
    
    # Display the CVSS risk score
    st.subheader("CVSS Risk Score:")
    st.write(f"The calculated CVSS Risk Score is: {cvss_score:.2f}")
    
    # Interpret the score
    if cvss_score <= 3.9:
        st.write("Severity: Low")
    elif cvss_score <= 6.9:
        st.write("Severity: Medium")
    else:
        st.write("Severity: High")

if st.sidebar.button("Assess Custom Risk"):
    # Perform custom risk assessment
    custom_risk_score = calculate_custom_risk_score(likelihood_custom, impact_custom)
    
    # Display the custom risk score
    st.subheader("Custom Risk Assessment Score:")
    st.write(f"The calculated Custom Risk Score is: {custom_risk_score:.2f}")

    # Interpret the score
    if custom_risk_score <= 10:
        st.write("Risk Level: Low")
    elif custom_risk_score <= 25:
        st.write("Risk Level: Medium")
    else:
        st.write("Risk Level: High")

if st.sidebar.button("Assess MTTI"):
    # Perform MTTI calculation
    mtti_result = calculate_mtti(recovery_time, detection_probability)
    
    # Display the MTTI result
    st.subheader("Mean Time to Identify (MTTI):")
    st.write(f"The calculated MTTI is: {mtti_result:.2f} hours")

if st.sidebar.button("Assess MTTC"):
    # Perform MTTC calculation
    mttc_result = calculate_mttc(recovery_time, containment_probability)
    
    # Display the MTTC result
    st.subheader("Mean Time to Contain (MTTC):")
    st.write(f"The calculated MTTC is: {mttc_result:.2f} hours")

if st.sidebar.button("Assess Combined Risk"):
    # Perform combined risk assessment
    combined_risk_score = calculate_combined_risk(likelihood_combined, impact_combined, threat_combined, vulnerability_combined)
    
    # Display the combined risk score
    st.subheader("Combined Risk Assessment Score:")
    st.write(f"The calculated Combined Risk Score is: {combined_risk_score:.2f}")

    # Interpret the score (customize thresholds as needed)
    if combined_risk_score <= 10:
        st.write("Risk Level: Low")
    elif combined_risk_score <= 25:
        st.write("Risk Level: Medium")
    else:
        st.write("Risk Level: High")
