import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import plotly.express as px

# Load Model Kategori A
with open('model_a.pkl', 'rb') as file_1:
  model_a = pickle.load(file_1)

# Load Model Produk A1
with open('model_a1.pkl', 'rb') as file_3:
  model_a1 = pickle.load(file_3)

# Load Model Produk A2
with open('model_a2.pkl', 'rb') as file_4:
  model_a2 = pickle.load(file_4)

def run() :
  st.markdown("<h1 style='text-align: center;'>Category A Sales Prediction</h1>", unsafe_allow_html=True)
  st.write('Page ini berisi model untuk prediksi sales Category A, Product A1 & Product A2')

  with st.form(key= 'form_a'):
      st.markdown('##### **Forecast Sales Category A**')
      input_a = st.number_input('Periode', min_value=0, max_value=90, value=5 ,step=1)
      st.write('###### **Mean Absolute Error :** ', 3.69)
      submitted_a = st.form_submit_button('Predict')

  if submitted_a :
      # Prediction
      result_a = model_a.forecast(input_a)
      result_a = pd.DataFrame(result_a)

      # Visualisasi
      fig = px.line(result_a, x=result_a.index, y=result_a.predicted_mean, title='Prediction Category A')
      fig.update_layout(xaxis_title="Days", yaxis_title="Prediction")
      fig.update_traces(line_color='red')
      st.plotly_chart(fig)
      st.write('**Prediction Category A :** ', result_a)

  with st.form(key= 'form_a1'):
      st.markdown('##### **Forecast Sales Product A1**')
      input_a1 = st.number_input('Periode', min_value=0, max_value=90, value=5 ,step=1)
      st.write('###### **Mean Absolute Error :** ', 7.4)
      submitted_a1 = st.form_submit_button('Predict')

  if submitted_a1 :
      # Prediction
      result_a1 = model_a1.forecast(input_a1)
      result_a1 = pd.DataFrame(result_a1)

      # Visualisasi
      fig = px.line(result_a1, x=result_a1.index, y=result_a1.predicted_mean, title='Prediction Product A1')
      fig.update_layout(xaxis_title="Days", yaxis_title="Prediction")
      fig.update_traces(line_color='red')
      st.plotly_chart(fig)
      st.write('**Prediction Product A1 :** ', result_a1)

  with st.form(key= 'form_a2'):
      st.markdown('##### **Forecast Sales Product A2**')
      input_a2 = st.number_input('Periode', min_value=0, max_value=90, value=5 ,step=1)
      st.write('###### **Mean Absolute Error :** ', 1.73)
      submitted_a2 = st.form_submit_button('Predict')

  if submitted_a2 :
      # Prediction
      result_a2 = model_a2.forecast(input_a2)
      result_a2 = pd.DataFrame(result_a2)

      # Visualisasi
      fig = px.line(result_a2, x=result_a2.index, y=result_a2.predicted_mean, title='Prediction Product A2')
      fig.update_layout(xaxis_title="Days", yaxis_title="Prediction")
      fig.update_traces(line_color='red')
      st.plotly_chart(fig)
      st.write('**Prediction Product A2 :** ', result_a2)


if __name__ == '__main__':
    run()
      