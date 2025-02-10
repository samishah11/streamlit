import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
# df=sns.load_dataset("titanic")
data_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(data_url)


# Title of the app
st.title("My_first_app_on_Titanic")

# Sidebar filters
st.sidebar.header("Filter Options")
selected_class = st.sidebar.selectbox("Select Passenger Class", ["All"] + sorted(df['Pclass'].unique().tolist()))
selected_gender = st.sidebar.selectbox("Select Gender", ["All"] + sorted(df['Sex'].unique().tolist()))

# Apply filters
filtered_df = df.copy()
if selected_class != "All":
    filtered_df = filtered_df[filtered_df['Pclass'] == selected_class]
if selected_gender != "All":
    filtered_df = filtered_df[filtered_df['Sex'] == selected_gender]

# Display dataset
st.write("### Filtered Data Preview")
st.dataframe(filtered_df.head())

# Display summary statistics
st.write("### Summary Statistics")
st.write(filtered_df.describe())

# Data Visualization
st.write("### Survival Count by Class")
fig, ax = plt.subplots()
sns.countplot(data=filtered_df, x='Pclass', hue='Survived', ax=ax)
ax.set_xlabel("Passenger Class")
ax.set_ylabel("Count")
st.pyplot(fig)

st.write("### Age Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_df['Age'].dropna(), kde=True, bins=20, ax=ax)
ax.set_xlabel("Age")
ax.set_ylabel("Count")
st.pyplot(fig)

# Run the app with `streamlit run script.py`
