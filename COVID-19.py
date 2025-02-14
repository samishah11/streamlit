import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
    df = pd.read_csv(url, parse_dates=['date'])
    return df

df = load_data()

# Streamlit App
st.title("COVID-19 Data Visualization with Plotly")

# Sidebar filters
countries = df['location'].unique()
selected_country = st.sidebar.selectbox("Select a Country", countries, index=list(countries).index("United States"))

# Filter data
country_data = df[df['location'] == selected_country]

# Plotly Charts
st.subheader(f"COVID-19 Trends in {selected_country}")

# Cases over time
fig_cases = px.line(country_data, x='date', y='new_cases', title="Daily New Cases", labels={'new_cases': 'New Cases'})
st.plotly_chart(fig_cases)

# Deaths over time
fig_deaths = px.line(country_data, x='date', y='new_deaths', title="Daily New Deaths", labels={'new_deaths': 'New Deaths'})
st.plotly_chart(fig_deaths)

# Vaccinations over time
fig_vax = px.line(country_data, x='date', y='people_vaccinated', title="Total People Vaccinated", labels={'people_vaccinated': 'People Vaccinated'})
st.plotly_chart(fig_vax)

# Data Table
st.subheader("Data Table")
st.dataframe(country_data[['date', 'new_cases', 'new_deaths', 'people_vaccinated']].dropna().tail(20))

st.write("Data Source: Our World in Data")
st.write("This app is made by SHAHBAZ MEHMOOD with the help of ChatGPT.")
