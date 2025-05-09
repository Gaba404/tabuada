import streamlit as st
import datetime
import re
import json
import os

ARQUIVO_DADOS = 'Login.json'

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, 'w', encoding= 'utf-8') as f:
        json.dump(dados, f,ensure_ascii=False, indet=4)






def criar_conta(login, usua, email, idade, data, senha):
    return{
    'login': login,
    'usuario': usua,
    'email': email,
    'idade': idade,
    'data': data,
    'senha': senha,
    }



st.sidebar.title('Menu')
opcao = st.sidebar.radio(
    'Selecine uma opção',
    ('Cadastrar Conta','Listar Contas',
     'Editar Contas','Excluir Conta')
)
def cadastrar_conta():
    st.title('Cadastro de conta do jogo')

    st.write('Preencha os campos abaixo')

    data_minima = datetime.date(1900,1,1)
    data_maxima = datetime.date(2100,1, 1)

    login = st.text_input('Nome para login')
    usua = st.text_input('Nome para o usuario')
    email = st.text_input('Email(Formato:123@gmail.com)')
    idade = st.number_input('Qual sua idade', step=1, value=0, format='%d')
    data = st.date_input('Nasc?', format='DD/MM/YYYY',min_value=data_minima   ,   max_value=data_maxima)
    senha = st.text_input('Digite sua senha', type='password')



    st.write(f'Olá {usua}, pronto para se aventurar?')



    col1, col3, col2, col4, col5 = st.columns(5)

    with col1:
        st.button("Criar")


    with col5:
        st.button("Já tenho login")

def listar_contas():
    st.title('Lista ')
    pass

def editar_contas():
    pass

def excluir_conta():
    pass




if opcao == 'Cadastrar Conta':
    cadastrar_conta()
elif opcao == 'Listar Contas':
    listar_contas()
elif opcao == 'Editar Contas':
    editar_contas()
elif opcao == 'Excluir Conta':
    excluir_conta()



st.sidebar.markdown('---')
st.sidebar.markdown('Desenvolvido por Gabriel')
st.sidebar.markdown(f'Total de contas: ')















