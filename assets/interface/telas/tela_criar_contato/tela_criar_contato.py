import os
import json
import tkinter as tk
from tkinter import messagebox
from assets.func.sessao.sessao import sessao_id

usuario_id = sessao_id()
json_path = os.path.join("assets", "arquivos", "contatos", f"{usuario_id}.json")

def salvar_contato(nome, telefone, email, data, telefone_original=None, atualizar_lista_callback=None):
    if not nome or not telefone:
        messagebox.showerror("Erro", "nome e telefone são obrigatórios!")
        return
    
    if not os.path.exists(json_path):
        with open(json_path, "w") as f:
            json.dump([], f)
    
    with open(json_path, "r") as f:
        contatos = json.load(f)
    
    if telefone_original:
        for contato in contatos:
            if contato["telefone"] == telefone_original:
                contato["nome"] = nome
                contato["telefone"] = telefone
                contato["EMAIL"] = email
                contato["aniversario"] = data
                break
    else:
        novo_contato = {
            "nome": nome,
            "telefone": telefone,
            "EMAIL": email,
            "aniversario": data,
            "enviar": False,
            "status": True
        }
        contatos.append(novo_contato)
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(contatos, f, ensure_ascii=False, indent=4)
    
    messagebox.showinfo("Sucesso", "Contato salvo com sucesso!")
    if atualizar_lista_callback:
        atualizar_lista_callback()

def tela_criar_contatos(atualizar_lista_callback=None, contato=None):
    janela = tk.Toplevel()
    janela.title("Criar/Editar Contato")
    janela.geometry("300x300")
    
    tk.Label(janela, text="nome:").pack(pady=5)
    entry_nome = tk.Entry(janela)
    entry_nome.pack(pady=5)
    
    tk.Label(janela, text="telefone:").pack(pady=5)
    entry_telefone = tk.Entry(janela)
    entry_telefone.pack(pady=5)
    
    tk.Label(janela, text="Email:").pack(pady=5)
    entry_email = tk.Entry(janela)
    entry_email.pack(pady=5)
    
    tk.Label(janela, text="Data:").pack(pady=5)
    entry_data = tk.Entry(janela)
    entry_data.pack(pady=5)
    
    if contato:
        entry_nome.insert(0, contato["nome"])
        entry_telefone.insert(0, contato["telefone"])
        entry_email.insert(0, contato["EMAIL"])
        entry_data.insert(0, contato["aniversario"])
    
    def salvar_e_atualizar():
        salvar_contato(
            entry_nome.get().upper(), 
            entry_telefone.get(), 
            entry_email.get(), 
            entry_data.get(),
            contato["telefone"] if contato else None,
            atualizar_lista_callback
        )
        janela.destroy()
    
    tk.Button(janela, text="Salvar", command=salvar_e_atualizar).pack(pady=20)
    
    janela.mainloop()

