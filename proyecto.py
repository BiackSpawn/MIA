import streamlit as st
import pandas as pd
import numpy as np
import google
import altair as alt

#from google.oauth2 import service_account
#from google.cloud import storage

# Create API client.
#credentials = service_account.Credentials.from_service_account_info(
#    st.secrets["gcp_service_account"]
#)
#client = storage.Client(credentials=credentials)

st.title('Proyecto Visualizacion')

df_ventas=pd.read_csv("datos_uc.csv",delimiter=';')
venta_mensual=pd.pivot_table(df_ventas,values=['Venta_Neta','Ofs'],index=['Fecha Nominal','Nombre_Categoria'],aggfunc=np.sum).reset_index()

st.st.altair_chart(
    alt.Chart(venta_mensual).mark_bar().encode(
        alt.X('yearmonth(Fecha Nominal):N', title='Fecha'),
        alt.Y('Venta_Neta:Q', title='Venta Neta Mensual'), 
    ).properties(
        width=1000,
        height=500,
        title='Ventas Netas Mensaules 2018 a 2022'
    )
)
