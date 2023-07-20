import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image


# Load data dengan pandas dan assign ke variabel df
xls = pd.ExcelFile('kalbe_data.xlsx')
df_a1 = pd.read_excel(xls,'A1')
df_a2 = pd.read_excel(xls,'A2')
df_b1 = pd.read_excel(xls,'B1')
df_b2 = pd.read_excel(xls,'B2')

# Membuat df kategori A
df_a = df_a1.copy()
df_a.rename(columns = {'Sales':'Sales_A1'}, inplace = True)
# Concat & rename
df_a = pd.concat([df_a, df_a2['Sales']], axis=1)
df_a.rename(columns = {'Sales':'Sales_A2'}, inplace = True)
df_a.replace(np.nan, 0, inplace=True)
# Menghitung total sales kategori A
df_a['sales_total'] = df_a['Sales_A1'] + df_a['Sales_A2']
# Membuat df kategori B
df_b = df_b1.copy()
df_b.rename(columns = {'Sales':'Sales_B1'}, inplace = True)
# Concat & rename
df_b = pd.concat([df_b, df_b2['Sales']], axis=1)
df_b.rename(columns = {'Sales':'Sales_B2'}, inplace = True)
df_b.replace(np.nan, 0, inplace=True)
# Menghitung total sales kategori B
df_b['sales_total'] = df_b['Sales_B1'] + df_b['Sales_B2']


def run() :
    # Membuat Title 
    st.markdown("<h1 style='text-align: center;'>Exploratory Data Analysis</h1>", unsafe_allow_html=True)
    st.write('Berikut adalah EDA dari setiap feature')

    # Membuat Sub Header
    st.subheader('**Trend Category A**')
    fig = px.line(df_a, x=df_a.Day, y=df_a.sales_total)
    fig.update_layout(xaxis_title="Day", yaxis_title="Actual Sales")
    st.plotly_chart(fig)

    # Membuat Sub Header
    st.subheader('**Trend Category B**')
    fig = px.line(df_b, x=df_b.Day, y=df_b.sales_total)
    fig.update_layout(xaxis_title="Day", yaxis_title="Actual Sales")
    st.plotly_chart(fig)

    # Membuat Sub Header
    st.subheader('**Trend Product A1**')
    fig = px.line(df_a1, x=df_a1.Day, y=df_a1.Sales)
    fig.update_layout(xaxis_title="Day", yaxis_title="Actual Sales")
    st.plotly_chart(fig)

    # Membuat Sub Header
    st.subheader('**Trend Product A2**')
    fig = px.line(df_a2, x=df_a2.Day, y=df_a2.Sales)
    fig.update_layout(xaxis_title="Day", yaxis_title="Actual Sales")
    st.plotly_chart(fig)

    # Membuat Sub Header
    st.subheader('**Trend Product B1**')
    fig = px.line(df_b1, x=df_b1.Day, y=df_b1.Sales)
    fig.update_layout(xaxis_title="Day", yaxis_title="Actual Sales")
    st.plotly_chart(fig)

    # Membuat Sub Header
    st.subheader('**Trend Product B2**')
    fig = px.line(df_b2, x=df_b2.Day, y=df_b2.Sales)
    fig.update_layout(xaxis_title="Day", yaxis_title="Actual Sales")
    st.plotly_chart(fig)

if __name__ == '__main__':
    run()