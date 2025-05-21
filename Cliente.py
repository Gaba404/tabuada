from util import formata_nome

def cadastrar_cliente(nome: str):
    return{
        'nome': formata_nome(nome)
    }