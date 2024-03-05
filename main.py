import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns

# Memuat Data
@st.cache
def load_data():
    day_data = pd.read_csv('path/to/day.csv') # Sesuaikan dengan path file Anda
    hour_data = pd.read_csv('path/to/hour.csv') # Sesuaikan dengan path file Anda
    return day_data, hour_data

day_df, hour_df = load_data()

# Judul Dashboard
st.title('Dashboard Analisis Penyewaan Sepeda')

# Menampilkan Dataset
st.header('Preview Dataset')
if st.checkbox('Tampilkan Data Harian'):
    st.write(day_df.head())

if st.checkbox('Tampilkan Data Per Jam'):
    st.write(hour_df.head())

# EDA dan Visualisasi
## Contoh: Hubungan Suhu dengan Jumlah Penyewaan
st.header('Analisis Hubungan Suhu dengan Jumlah Penyewaan')
fig, ax = plt.subplots()
ax = sns.scatterplot(x='temp', y='cnt', data=day_df)
plt.xlabel('Suhu')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(fig)


