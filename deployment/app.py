import streamlit as st
import eda
import prediction_a
import prediction_b


# Set Config dan icon
st.set_page_config(
        page_title='Sales Forecast Prediction',
        layout='wide',
        )

# Hide Streamlit Style
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Membuat navigasi
st.sidebar.markdown("")
navigation = st.sidebar.selectbox('Pilih Halaman (Forecast Category A/Forecast Category B/EDA): ', ('Forecast Category A','Forecast Category B','Exploratory Data Analysis'))


# Run modul dengan if else
if navigation == 'Forecast Category A' :
    prediction_a.run()
elif navigation == 'Forecast Category B' :
    prediction_b.run()
else :
    eda.run()