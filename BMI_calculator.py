import streamlit as st

# App title
st.title("💪 BMI Calculator")

# Input fields
weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (cm)", min_value=1.0, step=0.1)

# Calculate BMI
if st.button("Calculate BMI"):
    height_m = height / 100  # convert cm to meters
    bmi = weight / (height_m ** 2)
    st.success(f"Your BMI is: {bmi:.2f}")

    # BMI category
    if bmi < 18.5:
        st.info("You are underweight.")
    elif 18.5 <= bmi < 25:
        st.success("You are in the normal weight range.")
    elif 25 <= bmi < 30:
        st.warning("You are overweight.")
    else:
        st.error("You are in the obese range.")
