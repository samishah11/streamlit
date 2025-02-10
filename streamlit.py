import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Title of the app
st.title("Simple Streamlit Dashboard")

# Sidebar inputs
st.sidebar.header("User Input")
n_rows = st.sidebar.slider("Number of Data Points", min_value=1, max_value=1000, value=100, step=50)

# Generate random data
np.random.seed(52)  # Set seed for reproducibility
data = pd.DataFrame({
    'X': np.arange(n_rows),
    'Y': np.random.randn(n_rows) * 10
})

# Show data
st.write("### Sample_deshboard_made_by_SHAHBAZ")
st.dataframe(data.head())

# Plot data
st.write("### Data Visualization")
fig, ax = plt.subplots()
ax.plot(data['X'], data['Y'], marker='o', linestyle='-')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Random Data Plot")
st.pyplot(fig)

# Metrics
st.write("### Data Statistics")
st.metric("Mean", round(data['Y'].mean(), 2))
st.metric("Standard Deviation", round(data['Y'].std(), 2))

# Run this app with:

