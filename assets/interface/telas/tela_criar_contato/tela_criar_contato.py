import os
import json
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from assets.func.sessao.sessao import sessao_id

# Obtém o ID do usuário e define o caminho do arquivo JSON
usuario_id = sessao_id()

caminho_contatos = Path.home() / "nZap" / "contatos"
caminho_contatos.mkdir(parents=True, exist_ok=True)  # Cria a pasta se não existir
caminho_json = caminho_contatos / f".{usuario_id}.json"


# Função para salvar ou editar um contato
def salvar_contato(nome, telefone, email, data, telefone_original=None, atualizar_lista_callback=None):
    if not nome or not telefone:
        messagebox.showerror("Erro", "Nome e telefone são obrigatórios!")
        return
    
    # Garante que o arquivo JSON existe ou cria um vazio
    if not os.path.exists(caminho_json):
        os.makedirs(os.path.dirname(caminho_json), exist_ok=True)  # Cria os diretórios se não existirem
        with open(caminho_json, "w") as f:
            json.dump([], f)
    
    with open(caminho_json, "r") as f:
        contatos = json.load(f)
    
    # Se telefone_original for passado, edita o contato
    if telefone_original:
        for contato in contatos:
            if contato["telefone"] == telefone_original:
                contato["nome"] = nome
                contato["telefone"] = telefone
                contato["email"] = email
                contato["aniversario"] = data
                break
    else:
        # Adiciona um novo contato
        novo_contato = {
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "aniversario": data,
            "status": True,
            "enviar": False
        }
        contatos.append(novo_contato)
    
    # Atualiza o arquivo JSON com as modificações
    with open(caminho_json, "w", encoding="utf-8") as f:
        json.dump(contatos, f, ensure_ascii=False, indent=4)
    
    messagebox.showinfo("Sucesso", "Contato salvo com sucesso!")
    if atualizar_lista_callback:
        atualizar_lista_callback()

# Função para criar ou editar contatos na interface gráfica
def tela_criar_contatos(atualizar_lista_callback=None, contato=None):
    janela = tk.Toplevel()
    janela.title("Criar/Editar Contato")
    janela.geometry("300x300")
    
    tk.Label(janela, text="Nome:").pack(pady=5)
    entry_nome = tk.Entry(janela)
    entry_nome.pack(pady=5)
    
    tk.Label(janela, text="Telefone:").pack(pady=5)
    entry_telefone = tk.Entry(janela)
    entry_telefone.pack(pady=5)
    
    tk.Label(janela, text="email:").pack(pady=5)
    entry_email = tk.Entry(janela)
    entry_email.pack(pady=5)
    
    tk.Label(janela, text="Data:").pack(pady=5)
    entry_data = tk.Entry(janela)
    entry_data.pack(pady=5)
    
    # Se um contato for passado, preenche os campos com os dados existentes
    if contato:
        entry_nome.insert(0, contato["nome"])
        entry_telefone.insert(0, contato["telefone"])
        entry_email.insert(0, contato["email"])
        entry_data.insert(0, contato["aniversario"])
    
    # Função para salvar e atualizar a lista de contatos
    def salvar_e_atualizar():
        salvar_contato(
            entry_nome.get().upper(), 
            entry_telefone.get(), 
            entry_email.get(), 
            entry_data.get(),
            contato["telefone"] if contato else None,
            atualizar_lista_callback
        )
        janela.withdraw()
    
    tk.Button(janela, text="Salvar", command=salvar_e_atualizar).pack(pady=20)
    
    janela.mainloop()
