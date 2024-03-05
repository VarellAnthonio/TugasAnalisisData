import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
def load_data():
    data = pd.read_csv('day.csv')
    data['dateday'] = pd.to_datetime(data['dateday'])  # Convert 'dateday' to datetime format
    return data

df = load_data()

st.header('Analisis Data Bike Sharing by Varell')
# Sidebar untuk fitur input pengguna
st.sidebar.header('Filter by Date Range')
start_date = st.sidebar.date_input('Start Date', df['dateday'].min().date())
end_date = st.sidebar.date_input('End Date', df['dateday'].max().date())

# Konversi start_date dan end_date ke datetime jika belum
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Pastikan start date tidak setelah end date
if start_date > end_date:
    st.sidebar.error('Error: End date must fall after start date.')

# Filter data berdasarkan input pengguna
filtered_data = df[(df['dateday'] >= start_date) & (df['dateday'] <= end_date)]

# Visualization
st.subheader('Grafik Temperatur Terhadap Penggunaan Sewa Sepeda')
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_data, x='temp', y='count', ax=ax)
st.pyplot(fig)

# Additional Visualizations for Streamlit App

# Bar Chart: Grafik Musim Terhadap Penggunaan Sewa Sepeda
st.subheader('Grafik Musim Terhadap Penggunaan Sewa Sepeda')
fig, ax = plt.subplots()
seasonal_data = df.groupby('season')['count'].sum().reset_index()
sns.barplot(data=seasonal_data, x='season', y='count', ax=ax)
st.pyplot(fig)

# Line Plot: Tren Sewa Sepeda Sepanjang Tahun
st.subheader('Tren Sewa Sepeda Sepanjang Tahun')
fig, ax = plt.subplots()
monthly_data = df.groupby('month')['count'].sum().reset_index()
sns.lineplot(data=monthly_data, x='month', y='count', ax=ax)
st.pyplot(fig)

