import streamlit as st
import datetime
import re
st.title('Cadastro de conta do jogo')

st.write('Preencha os campos abaixo')


data_minima = datetime.date(1900,1,1)
data_maxima = datetime.date(2100,1, 1)

nome = st.text_input('Nome para login')
usua = st.text_input('Nome para o usuario')
email = st.text_input('Email(Formato:123@gmail.com)')
idade = st.number_input('Qual sua idade', step=1, value=0, format='%d')
Dtnasc = st.date_input('Nasc?', format='DD/MM/YYYY',min_value=data_minima   ,   max_value=data_maxima)
senha = st.text_input('Digite sua senha', type='password')



st.write(f'Olá {usua}, pronto para se aventurar?')



col1, col3, col2, col4, col5 = st.columns(5)

with col1:
    st.button("Criar")


with col5:
    st.button("Já tenho login")

