import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Streamlit UI
st.title("Iris_Dataset_Explorer")
st.write("This app allows you to explore the famous Iris dataset and made by Shahbaz.")

# Display dataset
if st.checkbox("Show raw data"):
    st.dataframe(df)

# Select visualization
st.sidebar.header("Visualization Options")
plot_type = st.sidebar.selectbox("Choose a plot type", ["Histogram", "Scatter Plot", "Box Plot"])

# Histogram
if plot_type == "Histogram":
    feature = st.sidebar.selectbox("Select feature", df.columns[:-1])
    fig, ax = plt.subplots()
    sns.histplot(df, x=feature, hue="species", kde=True, ax=ax)
    st.pyplot(fig)

# Scatter Plot
elif plot_type == "Scatter Plot":
    x_feature = st.sidebar.selectbox("X-axis", df.columns[:-1])
    y_feature = st.sidebar.selectbox("Y-axis", df.columns[:-1])
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=x_feature, y=y_feature, hue="species", ax=ax)
    st.pyplot(fig)

# Box Plot
elif plot_type == "Box Plot":
    feature = st.sidebar.selectbox("Select feature", df.columns[:-1])
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="species", y=feature, ax=ax)
    st.pyplot(fig)

# Run the app using: streamlit run filename.py
