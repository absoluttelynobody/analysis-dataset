import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("Analisis Data Penyewaan Sepeda Harian")

# Data cvs
day_df = pd.read_csv('day_csv')

# Preprocessing Data
day_df['day_df'] = day_df['workingday'].apply(lambda x: 'Hari Kerja' if x == 1 else 'Akhir Pekan/Hari Libur')
day_df['is_workingday'] = day_df['workingday'].apply(lambda x: 'Working Day' if x == 1 else 'Weekend/Holiday')


# Korelasi Cuaca dan Penggunaan
st.subheader('1. Hubungan Kondisi Cuaca dan Penggunaan (Harian)')
weather_usage_correlation_day = day_df[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()
st.write(weather_usage_correlation_day)

# Pengaruh Hari Libur dan Hari Kerja
st.subheader('2. Pengaruh Hari Libur dan Hari Kerja (Harian)')
avg_rentals_by_day_df_day = day_df.groupby('day_df')['cnt'].mean().reset_index()
st.write(avg_rentals_by_day_df_day)


# Visualisasi

# Pertanyaan 1: Kondisi Cuaca
st.subheader('Visualisasi Pengaruh Kondisi Cuaca Terhadap Jumlah Penyewaan')
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sns.scatterplot(ax=axes[0], x='temp', y='cnt', data=day_df, alpha=0.6)
axes[0].set_title('Suhu vs. Jumlah Penyewaan')
sns.scatterplot(ax=axes[1], x='hum', y='cnt', data=day_df, alpha=0.6)
axes[1].set_title('Kelembapan vs. Jumlah Penyewaan')
sns.scatterplot(ax=axes[2], x='windspeed', y='cnt', data=day_df, alpha=0.6)
axes[2].set_title('Kecepatan Angin vs. Jumlah Penyewaan')
st.pyplot(fig)

# Pertanyaan 2: Hari Kerja vs Akhir Pekan/Hari Libur
st.subheader('Perbedaan Jumlah Penyewaan: Hari Kerja vs Akhir Pekan/Hari Libur')
average_rentals_by_day_df = day_df.groupby('is_workingday')['cnt'].mean().reset_index()
plt.figure(figsize=(8, 6))
sns.barplot(x='is_workingday', y='cnt', data=average_rentals_by_day_df)
plt.title('Rata-Rata Jumlah Penyewaan Sepeda: Hari Kerja vs Akhir Pekan/Hari Libur')
st.pyplot(plt)

# Penambahan Fitur Interaktif
# Anda dapat menambahkan slider untuk memfilter data berdasarkan suhu, kelembapan, atau kecepatan angin
# contoh:
temp_slider = st.slider("Filter data berdasarkan Suhu", float(day_df['temp'].min()), float(day_df['temp'].max()))
filtered_data = day_df[day_df['temp'] <= temp_slider]
st.write(filtered_data)




