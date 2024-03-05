import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Memuat data
@st.cache
def load_data():
    day_data = pd.read_csv('day.csv')
    day_data['dteday'] = pd.to_datetime(day_data['dteday'])
    day_data['day_type'] = day_data['workingday'].apply(lambda x: 'Hari Kerja' if x == 1 else 'Akhir Pekan/Hari Libur')
    return day_data

day_df = load_data()

# Judul Dashboard
st.title('Dashboard Analisis Penyewaan Sepeda')

# Visualisasi 1: Hubungan Suhu dengan Jumlah Penyewaan
st.header('Hubungan Suhu dengan Jumlah Penyewaan Sepeda')
fig, ax = plt.subplots()
sns.scatterplot(x='temp', y='cnt', data=day_df, ax=ax)
ax.set_title('Suhu vs. Jumlah Penyewaan')
ax.set_xlabel('Suhu Normalisasi')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# Visualisasi 2: Rata-Rata Jumlah Penyewaan berdasarkan Tipe Hari
st.header('Rata-Rata Jumlah Penyewaan Sepeda: Hari Kerja vs Akhir Pekan/Hari Libur')
average_rentals = day_df.groupby('day_type')['cnt'].mean().reset_index()
fig, ax = plt.subplots()
sns.barplot(x='day_type', y='cnt', data=average_rentals, ax=ax)
ax.set_title('Rata-Rata Jumlah Penyewaan Sepeda')
ax.set_xlabel('Tipe Hari')
ax.set_ylabel('Rata-Rata Jumlah Penyewaan')
st.pyplot(fig)


