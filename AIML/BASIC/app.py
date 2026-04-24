import streamlit as st
import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏠 Boston House Price Prediction")

st.write("Adjust the features below to predict house price")

# Sidebar inputs (interactive UI)
CRIM = st.slider("Crime Rate", 0.0, 100.0, 1.0)
ZN = st.slider("Residential Land Zoned (%)", 0.0, 100.0, 10.0)
INDUS = st.slider("Industrial Area (%)", 0.0, 30.0, 5.0)
CHAS = st.selectbox("Charles River (0 = No, 1 = Yes)", [0, 1])
NOX = st.slider("Nitric Oxide Level", 0.0, 1.0, 0.5)
RM = st.slider("Average Rooms", 1.0, 10.0, 6.0)
AGE = st.slider("Old Houses (%)", 0.0, 100.0, 50.0)
DIS = st.slider("Distance to Employment Centers", 1.0, 12.0, 5.0)
RAD = st.slider("Highway Access Index", 1, 24, 5)
TAX = st.slider("Property Tax Rate", 100, 800, 300)
PTRATIO = st.slider("Student-Teacher Ratio", 10.0, 25.0, 18.0)
B = st.slider("Black Population Index", 0.0, 400.0, 350.0)
LSTAT = st.slider("Lower Status Population (%)", 0.0, 40.0, 10.0)

# Input array
features = np.array([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE,
                      DIS, RAD, TAX, PTRATIO, B, LSTAT]])

# Prediction
prediction = model.predict(features)

st.subheader("💰 Predicted House Price")
st.success(f"${prediction[0]*1000:.2f}")

# Feature importance
st.subheader("📊 Feature Importance")

importances = model.feature_importances_
feature_names = ["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE",
                 "DIS","RAD","TAX","PTRATIO","B","LSTAT"]

fig, ax = plt.subplots()
ax.barh(feature_names, importances)
ax.set_title("Feature Importance")
st.pyplot(fig)
