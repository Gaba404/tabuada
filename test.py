import streamlit as st
import datetime
import re

# Inicializa a variável de controle de navegação
if 'page' not in st.session_state:
    st.session_state.page = 'cadastro'

def ir_para_login():
    st.session_state.page = 'login'

def ir_para_jogo():
    st.session_state.page = 'jogo'

# Página de cadastro
if st.session_state.page == 'cadastro':
    st.title('Cadastro de conta do jogo')
    st.write('Preencha os campos abaixo')

    data_minima = datetime.date(1900, 1, 1)
    data_maxima = datetime.date(2100, 1, 1)

    nome = st.text_input('Nome para login')
    usua = st.text_input('Nome para o usuário')
    email = st.text_input('Email (Formato: 123@gmail.com)')
    idade = st.number_input('Qual sua idade', step=1, value=0, format='%d')
    Dtnasc = st.date_input('Data de nascimento', format='DD/MM/YYYY', min_value=data_minima, max_value=data_maxima)
    senha = st.text_input('Digite sua senha', type='password')

    st.write(f'Olá {usua}, pronto para se aventurar?')

    col1, col3, col2, col4, col5 = st.columns(5)

    with col1:
        if st.button("Criar"):
            ir_para_jogo()

    with col5:
        if st.button("Já tenho login"):
            ir_para_login()

# Página de jogo
elif st.session_state.page == 'jogo':
    st.title("Bem-vindo ao jogo!")
    st.write("Você criou sua conta com sucesso.")
    st.button("Voltar ao cadastro", on_click=lambda: st.session_state.update(page='cadastro'))

# Página de login
elif st.session_state.page == 'login':
    st.title("Login")
    login_user = st.text_input("Usuário")
    login_pass = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        st.success("Login realizado com sucesso!")
    
    st.button("Voltar ao cadastro", on_click=lambda: st.session_state.update(page='cadastro'))
