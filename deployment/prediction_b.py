import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import plotly.express as px

# Load Model Kategori B
with open('model_b.pkl', 'rb') as file_2:
  model_b = pickle.load(file_2)

# Load Model Produk B1
with open('model_b1.pkl', 'rb') as file_5:
  model_b1 = pickle.load(file_5)

# Load Model Produk B2
with open('model_b2.pkl', 'rb') as file_6:
  model_b2 = pickle.load(file_6)

def run() :
    st.markdown("<h1 style='text-align: center;'>Category B Sales Prediction</h1>", unsafe_allow_html=True)
    st.write('Page ini berisi model untuk prediksi sales Category B, Product B1 & Product B2')

    with st.form(key= 'form_b'):
        st.markdown('##### **Forecast Sales Category B**')
        input_b = st.number_input('Periode', min_value=0, max_value=90, value=5 ,step=1)
        st.write('###### **Mean Absolute Error :** ', 194.48)
        submitted_b = st.form_submit_button('Predict')

    if submitted_b :
        # Prediction
        result_b = model_b.forecast(input_b)
        result_b = pd.DataFrame(result_b)

        # Visualisasi
        fig = px.line(result_b, x=result_b.index, y=result_b.predicted_mean, title='Prediction Category B')
        fig.update_layout(xaxis_title="Days", yaxis_title="Prediction")
        fig.update_traces(line_color='red')
        st.plotly_chart(fig)
        st.write('**Prediction Category B :** ', result_b)

    with st.form(key= 'form_b1'):
        st.markdown('##### **Forecast Sales Product B1**')
        input_b1 = st.number_input('Periode', min_value=0, max_value=90, value=5 ,step=1)
        st.write('###### **Mean Absolute Error :** ', 120.9)
        submitted_b1 = st.form_submit_button('Predict')

    if submitted_b1 :
        # Prediction
        result_b1 = model_b1.forecast(input_b1)
        result_b1 = pd.DataFrame(result_b1, columns=['predicted_mean'])

        # Visualisasi
        fig = px.line(result_b1, x=result_b1.index, y= result_b1.predicted_mean, title='Prediction Product B1')
        fig.update_layout(xaxis_title="Days", yaxis_title="Prediction")
        fig.update_traces(line_color='red')
        st.plotly_chart(fig)
        st.write('**Prediction Product B1 :** ', result_b1)

    with st.form(key= 'form_b2'):
        st.markdown('##### **Forecast Sales Product B2**')
        input_b2 = st.number_input('Periode', min_value=0, max_value=90, value=5 ,step=1)
        st.write('###### **Mean Absolute Error :** ', 118.66)
        submitted_b2 = st.form_submit_button('Predict')

    if submitted_b2 :
        # Prediction
        result_b2 = model_b2.forecast(input_b2)
        result_b2 = pd.DataFrame(result_b2, columns=['predicted_mean'])

        # Visualisasi
        fig = px.line(result_b2, x=result_b2.index, y=result_b2.predicted_mean, title='Prediction Product B2')
        fig.update_layout(xaxis_title="Days", yaxis_title="Prediction")
        fig.update_traces(line_color='red')
        st.plotly_chart(fig)
        st.write('**Prediction Product B2 :** ', result_b2)


if __name__ == '__main__':
    run()
    