import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json

def carregar_de_json():
    global pessoas, next_id

    arquivo = filedialog.askopenfilename(
        filetypes=[("Arquivos JSON", "*.json")],
        title="Selecionar arquivo JSON para carregar"
    )

    if not arquivo:
        return

    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            pessoas_carregadas = json.load(f)

        pessoas = pessoas_carregadas
        if pessoas:
            next_id = max(p['id'] for p in pessoas) + 1
        else:
            next_id = 1

        carregar_pessoas()
        messagebox.showinfo("Sucesso", f"Dados carregados com sucesso de:\n{arquivo}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao carregar:\n{str(e)}")

def salvar_para_json():
    if not pessoas:
        messagebox.showwarning("Aviso", "Não há pessoas cadastradas!")
        return

    arquivo = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("Arquivos JSON", "*.json")],
        title="Salvar lista de pessoas como JSON"
    )

    if not arquivo:
        return

    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(pessoas, f, ensure_ascii=False, indent=4)
        messagebox.showinfo("Sucesso", f"Dados salvos com sucesso em:\n{arquivo}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao salvar:\n{str(e)}")

def carregar_pessoas():
    for item in tree.get_children():
        tree.delete(item)

    for p in pessoas:
        tree.insert('', 'end', values=(
            p['id'], 
            p['nome'], 
            p['data_nasc'], 
            p['genero'],
            p['estado_civil'], 
            p['profissao'], 
            p['celular']
        ))

def adicionar_pessoa():
    global next_id
    nome = entry_nome.get()
    data_nasc = entry_data_nasc.get()
    genero = entry_genero.get()
    estado_civil = entry_estado_civil.get()
    profissao = entry_profissao.get()
    celular = entry_celular.get()

    if not nome:
        messagebox.showerror("Erro", "O campo nome é obrigatório!")
        return

    nova_pessoa = {
        'id': next_id,
        'nome': nome,
        'data_nasc': data_nasc,
        'genero': genero,
        'estado_civil': estado_civil,
        'profissao': profissao,
        'celular': celular
    }

    pessoas.append(nova_pessoa)
    next_id += 1
    messagebox.showinfo("Sucesso", "Pessoa cadastrada com sucesso!")
    carregar_pessoas()
    limpar_campos()

def selecionar_pessoa(event):
    selected_item = tree.selection()
    if not selected_item:
        return
    values = tree.item(selected_item)['values']
    limpar_campos()
    entry_nome.insert(0, values[1])
    entry_data_nasc.insert(0, values[2])
    entry_genero.insert(0, values[3])
    entry_estado_civil.insert(0, values[4])
    entry_profissao.insert(0, values[5])
    entry_celular.insert(0, values[6])

def limpar_campos():
    entry_nome.delete(0, 'end')
    entry_data_nasc.delete(0, 'end')
    entry_genero.delete(0, 'end')
    entry_estado_civil.delete(0, 'end')
    entry_profissao.delete(0, 'end')
    entry_celular.delete(0, 'end')

def editar_pessoa():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erro", "Selecione uma pessoa para editar!")
        return

    pessoa_id = tree.item(selected_item)['values'][0]
    for p in pessoas:
        if p['id'] == pessoa_id:
            p.update({
                'nome': entry_nome.get(),
                'data_nasc': entry_data_nasc.get(),
                'genero': entry_genero.get(),
                'estado_civil': entry_estado_civil.get(),
                'profissao': entry_profissao.get(),
                'celular': entry_celular.get()
            })
            break

    messagebox.showinfo("Sucesso", "Pessoa atualizada com sucesso!")
    carregar_pessoas()

def remover_pessoa():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erro", "Selecione uma pessoa para remover!")
        return

    pessoa_id = tree.item(selected_item)['values'][0]

    if messagebox.askyesno("Confirmação", "Tem certeza que deseja remover esta pessoa?"):
        global pessoas
        pessoas = [p for p in pessoas if p['id'] != pessoa_id]
        messagebox.showinfo("Sucesso", "Pessoa removida com sucesso!")
        carregar_pessoas()
        limpar_campos()

# Dados em memória
pessoas = []
next_id = 1

# Interface
root = tk.Tk()
root.title("Cadastro de Pessoas")
root.geometry("850x500")

frame_form = ttk.LabelFrame(root, text="Formulário de Pessoa")
frame_form.pack(padx=10, pady=5, fill='x')

labels = ["Nome", "Data de Nascimento", "Gênero", "Estado Civil", "Profissão", "Celular"]
entries = []
for i, label_text in enumerate(labels):
    ttk.Label(frame_form, text=label_text + ":").grid(row=i, column=0, padx=5, pady=5, sticky='e')
    entry = ttk.Entry(frame_form, width=40)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

entry_nome, entry_data_nasc, entry_genero, entry_estado_civil, entry_profissao, entry_celular = entries

frame_botoes = ttk.Frame(root)
frame_botoes.pack(pady=5)

ttk.Button(frame_botoes, text="Adicionar",
            command=adicionar_pessoa).grid(row=0, column=0, padx=5)
ttk.Button(frame_botoes, text="Editar",
            command=editar_pessoa).grid(row=0, column=1, padx=5)
ttk.Button(frame_botoes, text="Remover", 
            command=remover_pessoa).grid(row=0, column=2, padx=5)
ttk.Button(frame_botoes, text="Limpar",
            command=limpar_campos).grid(row=0, column=3, padx=5)
ttk.Button(frame_botoes, text="Salvar ",
            command=salvar_para_json).grid(row=0, column=4, padx=5)
ttk.Button(frame_botoes, text="Carregar ",
            command=carregar_de_json).grid(row=0, column=5, padx=5)

frame_tabela = ttk.Frame(root)
frame_tabela.pack(padx=10, pady=5, fill='both', expand=True)

tree = ttk.Treeview(frame_tabela, columns=('ID', 'Nome', 'Data Nasc.', 'Gênero', 'Estado Civil', 'Profissão', 'Celular'), show='headings')
colunas = ['ID', 'Nome', 'Data Nasc.', 'Gênero', 'Estado Civil', 'Profissão', 'Celular']
larguras = [40, 120, 100, 80, 100, 120, 100]

for col, largura in zip(colunas, larguras):
    tree.heading(col, text=col)
    tree.column(col, width=largura)

scrollbar = ttk.Scrollbar(frame_tabela, orient='vertical', command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

tree.bind('<<TreeviewSelect>>', selecionar_pessoa)

root.mainloop()