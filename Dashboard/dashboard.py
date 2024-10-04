import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
from PIL import Image  # Untuk memuat gambar

# Memuat dataset dari file CSV lokal
df = pd.read_csv('cleaned_bikeshare_hour.csv')
df['dteday'] = pd.to_datetime(df['dteday'])

# Pengaturan halaman Streamlit
st.set_page_config(page_title="Bike Ride Analytics",
                   page_icon="🚴‍♀️",
                   layout="wide")

image = Image.open('bike.jpg')

# Sidebar untuk filter data berdasarkan rentang tanggal
st.sidebar.image(image, caption='Bike Sharing Logo', use_column_width=True)  # Tampilkan gambar di sidebar
st.sidebar.header("Filter Data:")

min_date = df["dteday"].min()
max_date = df["dteday"].max()

start_date, end_date = st.sidebar.date_input(
    label="Pilih rentang tanggal", min_value=min_date,
    max_value=max_date, value=[min_date, max_date]
)

# Filter dataset berdasarkan tanggal yang dipilih
filtered_df = df[(df["dteday"] >= pd.to_datetime(start_date)) &
                 (df["dteday"] <= pd.to_datetime(end_date))]

# Fungsi bantu untuk agregasi data bulanan
def aggregate_monthly_rides(dataframe):
    monthly_data = dataframe.resample('M', on='dteday').agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    })
    monthly_data.index = monthly_data.index.strftime('%b-%y')
    return monthly_data.reset_index().rename(columns={
        "dteday": "month",
        "cnt": "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    })

# Fungsi bantu untuk agregasi data berdasarkan musim
def aggregate_seasonal_rides(dataframe):
    seasonal_data = dataframe.groupby('season').agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    }).reset_index().rename(columns={
        "cnt": "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    })
    seasonal_data = pd.melt(seasonal_data, id_vars=['season'],
                            value_vars=['casual_rides', 'registered_rides'],
                            var_name='ride_type', value_name='ride_count')
    seasonal_data['season'] = pd.Categorical(seasonal_data['season'],
                                             categories=['Spring', 'Summer', 'Fall', 'Winter'])
    return seasonal_data.sort_values('season')

# Fungsi bantu untuk agregasi data berdasarkan hari kerja
def aggregate_weekday_rides(dataframe):
    weekday_data = dataframe.groupby('weekday').agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    }).reset_index().rename(columns={
        "cnt": "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    })
    weekday_data = pd.melt(weekday_data, id_vars=['weekday'],
                           value_vars=['casual_rides', 'registered_rides'],
                           var_name='ride_type', value_name='ride_count')
    weekday_data['weekday'] = pd.Categorical(weekday_data['weekday'],
                                             categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    return weekday_data.sort_values('weekday')

# Fungsi bantu untuk agregasi data berdasarkan jam
def aggregate_hourly_rides(dataframe):
    hourly_data = dataframe.groupby('hr').agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    }).reset_index().rename(columns={
        "cnt": "total_rides",
        "casual": "casual_rides",
        "registered": "registered_rides"
    })
    return hourly_data

# Fungsi bantu untuk agregasi berdasarkan suhu
def aggregate_rides_by_temperature(dataframe):
    temperature_data = dataframe.groupby('temp').agg({
        'cnt': 'mean'
    }).reset_index().rename(columns={
        'temp': 'temperature',
        'cnt': 'average_rides'
    })
    return temperature_data

# Buat dataset berdasarkan fungsi-fungsi agregasi di atas
monthly_data = aggregate_monthly_rides(filtered_df)
seasonal_data = aggregate_seasonal_rides(filtered_df)
weekday_data = aggregate_weekday_rides(filtered_df)
hourly_data = aggregate_hourly_rides(filtered_df)
temperature_data = aggregate_rides_by_temperature(filtered_df)

# Halaman utama Dashboard
st.title("🚴‍♂️ Bike-Sharing Dashboard by Rini")  # Menambahkan nama di judul
st.markdown("#### Analisis penggunaan sepeda berdasarkan data Capital Bikeshare.")

# Menampilkan metrik utama
col1, col2, col3 = st.columns(3)

with col1:
    total_rides = filtered_df['cnt'].sum()
    st.metric("Total Rides", total_rides)

with col2:
    total_casual = filtered_df['casual'].sum()
    st.metric("Total Casual Rides", total_casual)

with col3:
    total_registered = filtered_df['registered'].sum()
    st.metric("Total Registered Rides", total_registered)

st.markdown("---")

# Visualisasi menggunakan Plotly
fig_monthly = px.line(monthly_data, x='month', y=['casual_rides', 'registered_rides', 'total_rides'],
                      color_discrete_sequence=["#007bff", "#ff851b", "#2ca02c"],
                      markers=True, title="Total Rides Per Month")

fig_seasonal = px.bar(seasonal_data, x='season', y='ride_count', color='ride_type',
                      title="Rides Per Season", barmode='group',
                      color_discrete_sequence=["#007bff", "#ff851b"])

fig_weekday = px.bar(weekday_data, x='weekday', y='ride_count', color='ride_type',
                     title="Rides Per Weekday", barmode='group',
                     color_discrete_sequence=["#007bff", "#ff851b"])

# Tampilkan grafik di halaman utama
left_col, right_col = st.columns(2)
left_col.plotly_chart(fig_seasonal, use_container_width=True)
right_col.plotly_chart(fig_weekday, use_container_width=True)

# Visualisasi berdasarkan jam
fig_hourly = px.line(hourly_data, x='hr', y=['casual_rides', 'registered_rides'],
                     color_discrete_sequence=["#007bff", "#ff851b"],
                     markers=True, title="Rides Per Hour")

# Visualisasi berdasarkan suhu
fig_temperature = px.scatter(temperature_data, x='temperature', y='average_rides',
                              title="Average Rides by Temperature",
                              labels={'temperature': 'Temperature (normalized)', 'average_rides': 'Average Rides'},
                              color_discrete_sequence=["#ff851b"])

st.plotly_chart(fig_monthly, use_container_width=True)
st.plotly_chart(fig_hourly, use_container_width=True)
st.plotly_chart(fig_temperature, use_container_width=True)  # Tampilkan grafik baru

# Sembunyikan elemen default Streamlit
st.markdown(""" 
    <style> 
    #MainMenu {visibility: hidden;} 
    footer {visibility: hidden;} 
    header {visibility: hidden;} 
    </style> 
    """, unsafe_allow_html=True)

# Menambahkan footer dengan nama
st.markdown("<br><br><h5 style='text-align: center;'>Created by Rini</h5>", unsafe_allow_html=True)  # Menambahkan nama di footer
