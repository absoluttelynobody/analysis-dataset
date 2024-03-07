import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title('Analisis Data Proyek')

# Memuat dan Menampilkan Dataset
data_path = 'path_ke_dataset_anda.csv' # Ganti dengan path yang sesuai
data = pd.read_csv(data_path)
st.write(data.head())

# Analisis dan Visualisasi
st.header('Visualisasi Data')
option = st.selectbox(
    'Pilih visualisasi yang Anda inginkan:',
    ('Distribusi Suhu', 'Hubungan Suhu dengan Kelembapan')
)

if option == 'Distribusi Suhu':
    plt.figure(figsize=(10, 6))
    sns.histplot(data['temp'], bins=20, kde=True)
    st.pyplot(plt)
elif option == 'Hubungan Suhu dengan Kelembapan':
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='temp', y='hum', data=data)
    st.pyplot(plt)

# Menambahkan lebih banyak analisis dan visualisasi sesuai dengan notebook Jupyter Anda.



