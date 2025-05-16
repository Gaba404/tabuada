import streamlit as st
import json
import os
import datetime

# ===================== ESTILO PERSONALIZADO =====================
st.set_page_config(page_title="Sistema de Contas", layout="wide")

st.markdown("""
    <style>
        .stApp {
            background: linear-gradient( #ffffff);
            color: #333;
            font-family: 'Segoe UI', sans-serif;
        }

        .stTextInput > div > input,
        .stNumberInput > div > input,
        .stPassword > div > input {
            border: 1px solid #0099cc;
            border-radius: 8px;
        }

        .stButton > button {
            background-color: #0099cc;
            color: white;
            padding: 10px 16px;
            border-radius: 8px;
            font-weight: bold;
        }

        .stButton > button:hover {
            background-color: #007bb5;
        }

        .stSidebar {
            background-color: #f0f8ff;
        }

        .stExpander {
            background-color: #f8fbff !important;
            border-radius: 8px;
            border: 1px solid #cce7ff;
            padding: 10px;
        }

        .css-1v0mbdj p {
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# ===================== CABEÇALHO COM IMAGEM =====================
st.image("https://cdn-icons-png.flaticon.com/512/1208/1208852.png", width=50)
st.title("🌐 Sistema de Gerenciamento de Contas")
st.caption("Organize, edite e gerencie usuários com facilidade")

# ===================== JSON =====================
ARQUIVO_DADOS = "Conta.json"

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def criar_conta(login, usua, email, idade, data, senha):
    return {
        'login': login,
        'usuario': usua,
        'email': email,
        'idade': idade,
        'data': data,
        'senha': senha,
        'historico_conta': []
    }

# ===================== FUNÇÕES CRUD =====================

def cadastrar_conta():
    st.subheader("📋 Cadastrar Nova Conta")

    with st.form(key="form_cadastro"):
        login = st.text_input('👤 Nome para login')
        usua = st.text_input('📛 Nome do usuário')
        email = st.text_input('📧 Email')
        idade = st.number_input('🎂 Idade', step=1, value=0, format='%d')
        senha = st.text_input('🔐 Senha', type='password')
        submit_button = st.form_submit_button("✅ Cadastrar Conta")
    
    if submit_button:
        if not login or not senha or not email:
            st.error("⚠️ Login, e-mail e senha são campos obrigatórios!")
            return
        
        dados = carregar_dados()
        
        if email in dados:
            st.error("❌ Conta com este e-mail já existe!")
            return
        
        Conta = criar_conta(
            login=login,
            usua=usua,
            email=email,
            idade=idade,
            data=str(datetime.datetime.now()),
            senha=senha
        )
        
        dados[email] = Conta
        salvar_dados(dados)
        
        st.success("🎉 Conta cadastrada com sucesso!")
        st.balloons()

def listar_contas():
    st.subheader("📂 Contas Cadastradas")

    dados = carregar_dados()
    
    if not dados:
        st.info("📭 Nenhuma conta cadastrada.")
        return
    
    filtro_nome = st.text_input("🔍 Filtrar por nome:")

    contas_filtradas = []
    for email, conta in dados.items():
        if filtro_nome.lower() in conta["usuario"].lower():
            contas_filtradas.append((email, conta))
    
    if not contas_filtradas:
        st.warning("😕 Nenhuma conta encontrada com esse nome.")
        return
    
    for email, conta in contas_filtradas:
        with st.expander(f"{conta['usuario']} - Login: {conta['login']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**👤 Login:** {conta['login']}")
                st.write(f"**📧 Email:** {conta['email']}")
            with col2:
                st.write(f"**🎂 Idade:** {conta['idade']}")
                st.write(f"**🔐 Senha:** {conta['senha']}")
            
            if conta["historico_conta"]:
                st.write("📜 **Histórico:**")
                for item in conta["historico_conta"]:
                    st.write(f"- {item}")

def editar_conta():
    st.subheader("✏️ Editar Conta")
    
    dados = carregar_dados()
    if not dados:
        st.info("⚠️ Nenhuma conta para editar.")
        return

    emails = list(dados.keys())
    conta_selecionada = st.selectbox("📧 Selecione a conta (e-mail)", options=emails)
    conta = dados[conta_selecionada]
    
    with st.form(key="form_edicao"):
        novo_login = st.text_input("Novo Login", value=conta["login"])
        novo_usuario = st.text_input("Novo Nome de Usuário", value=conta["usuario"])
        nova_idade = st.number_input("Nova Idade", step=1, value=int(conta["idade"]), format='%d')
        nova_senha = st.text_input("Nova Senha", value=conta["senha"])
        submit_button = st.form_submit_button("💾 Atualizar Conta")
    
    if submit_button:
        conta["login"] = novo_login
        conta["usuario"] = novo_usuario
        conta["idade"] = nova_idade
        conta["senha"] = nova_senha
        conta["data"] = str(datetime.datetime.now())

        dados[conta_selecionada] = conta
        salvar_dados(dados)
        st.success("✅ Conta atualizada com sucesso!")

def excluir_conta():
    st.subheader("🗑️ Excluir Conta")
    
    dados = carregar_dados()
    if not dados:
        st.info("⚠️ Nenhuma conta para excluir.")
        return

    emails = list(dados.keys())
    conta_selecionada = st.selectbox("📧 Escolha uma conta para excluir", options=emails)
    conta = dados[conta_selecionada]

    st.warning("🚨 Esta conta será excluída permanentemente:")
    st.json(conta)

    if st.button("❌ Confirmar Exclusão"):
        dados.pop(conta_selecionada)
        salvar_dados(dados)
        st.success("🗑️ Conta excluída com sucesso!")

# ===================== MENU =====================
st.sidebar.title("📌 Menu")
opcao = st.sidebar.radio(
    "Escolha uma opção:",
    ("Cadastrar Conta", "Listar Contas", "Editar Conta", "Excluir Conta")
)

# ===================== NAVEGAÇÃO =====================
if opcao == "Cadastrar Conta":
    cadastrar_conta()
elif opcao == "Listar Contas":
    listar_contas()
elif opcao == "Editar Conta":
    editar_conta()
elif opcao == "Excluir Conta":
    excluir_conta()

# ===================== RODAPÉ =====================
st.sidebar.markdown("---")
st.sidebar.markdown("👨‍💻 Desenvolvido por Gabriel")
dados = carregar_dados()
st.sidebar.markdown(f"📊 Total de Contas: **{len(dados)}**")
