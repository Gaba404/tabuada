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
        json.dump(dados, f,ensure_ascii=False, indent=4)





'''
def criar_conta(login, usua, email, idade, data, senha):
    return{
    'login': login,
    'usuario': usua,
    'email': email,
    'idade': idade,
    'data': data,
    'senha': senha,
    }

'''


def criar_conta_dict(login, usua, email, idade, data, senha):
    return {
        'login': login,
        'usuario': usua,
        'email': email,
        'idade': idade,
        'data': data,
        'senha': senha,
    }

def criar_conta():
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
        submit_button = st.form_submit_button("Cadastrar Conta")
    
    if submit_button:
        if not email or not login:
            st.error("Email e login são campos obrigatórios!")
            return
        
        dados = carregar_dados()
        
        if email in dados:
            st.error("Conta com este Email já cadastrado!")
            return
        
        conta = criar_conta(
               login = login,
        usua = usua,
        email = email,
        idade = data.strftime("%d/%m/%Y"),
        data = data,
        senha = senha
        )
        
        dados[email] = login
        salvar_dados(dados)
        
        st.success("Conta cadastrada com sucesso!")
        st.balloons()

    with col5:
        st.button("Já tenho login")











def listar_contas():
    st.subheader("Listar contas")
    
    dados = carregar_dados()
    
    if not dados:
        st.info("Nenhuma conta cadastrada ainda.")
        return
    
    # Filtro por nome
    filtro_nome = st.text_input("Filtrar por nome:")
    
    contas_filtrados = []
    for gmail, login in dados.items():
        if filtro_nome.lower() in login["nome"].lower():
            contas_filtrados.append((gmail, login))
    
    if not contas_filtrados:
        st.warning("Nenhuma conta encontrada com o filtro aplicado.")
        return
    
    for gmail, login in contas_filtrados:
        with st.expander(f"{login['Login']} - Gmail: {gmail}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Login:** {login['login']}")
                st.write(f"**Usuaro:** {login['Usuario']}")
                st.write(f"**Email:** {login['Email']}")
            
            with col2:
                st.write(f"**Telefone:** {login['telefone']}")
                st.write(f"**E-mail:** {login['email']}")
                st.write(f"**Cadastrado em:** {login['data_cadastro']}")
            
            if login["historico_Conta"]:
                st.write("**Histórico de Conta:**")
                for item in login["historico_Contas"]:
                    st.write(f"- {item}")

def editar_contas():
    pass

def excluir_conta():
    pass

st.sidebar.title('Menu')
opcao = st.sidebar.radio(
    'Selecine uma opção',
    ('Cadastrar Conta','Listar Contas',
     'Editar Contas','Excluir Conta')
)


if opcao == 'Cadastrar Conta':
    criar_conta()
elif opcao == 'Listar Contas':
    listar_contas()
elif opcao == 'Editar Contas':
    editar_contas()
elif opcao == 'Excluir Conta':
    excluir_conta()



st.sidebar.markdown('---')
st.sidebar.markdown('Desenvolvido por Gabriel')
st.sidebar.markdown(f'Total de contas: ')















