import streamlit as st
import pickle
import numpy as np

# Load Pipeline
with open("house_price_pipeline.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🏠 House Price Prediction")

area = st.number_input(
    "Area (sq ft)",
    min_value=100,
    value=1000
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    value=2
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    value=2
)

if st.button("Predict Price"):

    features = np.array([
        [area, bedrooms, bathrooms]
    ])

    prediction = model.predict(features)

    st.success(
        f"Predicted House Price: ₹ {prediction[0]:,.2f}"
    )

    st.balloons()