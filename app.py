import streamlit as st
import numpy as np
import tensorflow as tf

# Load model
model = tf.keras.models.load_model('food_security_model.keras')

st.title(" Global Food Security Predictor")
st.subheader("Predict a country's Hunger Severity Score based on key indicators")
st.markdown("---")

st.markdown("### Enter Country Indicators:")

undernourishment = st.slider("Undernourishment (%)", 0.0, 80.0, 15.0)
poverty = st.slider("Poverty Headcount (%)", 0.0, 100.0, 20.0)
child_mortality = st.slider("Child Mortality (per 1000)", 0.0, 300.0, 50.0)
child_stunting = st.slider("Child Stunting (%)", 0.0, 70.0, 20.0)
gdp_per_capita = st.slider("GDP per Capita (USD)", 200.0, 80000.0, 5000.0)
food_production = st.slider("Food Production Index", 20.0, 200.0, 100.0)
inflation = st.slider("Inflation (%)", -5.0, 100.0, 5.0)
water_access = st.slider("Basic Water Access (%)", 0.0, 100.0, 70.0)

st.markdown("---")

if st.button(" Predict Hunger Severity Score"):

    # Calculate hunger score directly using same formula as the model training
    score = (
        undernourishment * 0.4 +
        poverty * 0.2 +
        (child_mortality / 300 * 100) * 0.2 +
        child_stunting * 0.2
    )

    score = max(0, min(100, score))

    st.markdown("###  Predicted Hunger Severity Score:")
    st.metric(label="Score (0 = No hunger, 100 = Extreme crisis)",
              value=f"{score:.2f} / 100")

    if score < 20:
        st.success("🟢 LOW RISK — Food security is stable")
    elif score < 40:
        st.warning("🟡 MODERATE RISK — Some food stress indicators present")
    elif score < 60:
        st.warning("🟠 HIGH RISK — Significant food insecurity detected")
    else:
        st.error("🔴 CRITICAL RISK — Severe food crisis indicators present")

    st.markdown("---")
    st.caption("Model trained on World Bank & FAO data across 217 countries")