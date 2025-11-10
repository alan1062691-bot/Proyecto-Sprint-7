import streamlit as st
import pandas as pd
import plotly.express as px


try:
    df = pd.read_csv("vehicles_us.csv")
except FileNotFoundError:
    st.error("Error: El archivo 'vehicles_us.csv' no se encontró. Asegúrate de que esté en la misma carpeta que 'app.py'.")
    st.stop()




st.header('Análisis Exploratorio de Datos de Anuncios de Vehículos')
st.write("""
Esta aplicación te permite explorar la distribución de precios y la relación entre 
el precio y el kilometraje de los vehículos.
""")



build_histogram = st.checkbox('Mostrar Histograma de Precios')

if build_histogram:
    st.write('Construyendo un histograma de la distribución de precios de los vehículos.')

    
    fig_hist = px.histogram(
        df, 
        x="price", 
        title="Distribución de Precios de Venta",
        labels={'price': 'Precio ($)'}
    )

    
    st.plotly_chart(fig_hist, use_container_width=True)



build_scatter = st.checkbox('Mostrar Gráfico de Dispersión (Precio vs. Kilometraje)')

if build_scatter:
    st.write('Construyendo un gráfico de dispersión para analizar la relación entre el precio y el kilometraje (odómetro).')

    
    fig_scatter = px.scatter(
        df, 
        x="odometer", 
        y="price", 
        title="Precio vs. Kilometraje",
        labels={'odometer': 'Kilometraje (Millas)', 'price': 'Precio ($)'},
        opacity=0.5, 
        log_y=True 
    )

    
    st.plotly_chart(fig_scatter, use_container_width=True)