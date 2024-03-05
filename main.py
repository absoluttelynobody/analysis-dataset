import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
@st.cache
def load_data():
    day_data = pd.read_csv('day.csv')
    day_data['dteday'] = pd.to_datetime(day_data['dteday'])
    return day_data

day_df = load_data()

# Page title
st.title('Bike Rentals Analysis Dashboard')

# Weather conditions and bike rentals correlation
st.header('Correlation Between Weather Conditions and Bike Rentals')
weather_features = ['temp', 'atemp', 'hum', 'windspeed', 'cnt']
corr_matrix = day_df[weather_features].corr()

# Plotting heatmap
fig, ax = plt.subplots()
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .5})
st.pyplot(fig)

# Bike rentals on working days vs holidays/weekends
st.header('Bike Rentals on Working Days vs. Holidays/Weekends')
day_df['day_type'] = day_df['workingday'].apply(lambda x: 'Working Day' if x == 1 else 'Holiday/Weekend')

# Plotting boxplot
fig, ax = plt.subplots()
sns.boxplot(x='day_type', y='cnt', data=day_df)
plt.xticks(rotation=45)
st.pyplot(fig)


