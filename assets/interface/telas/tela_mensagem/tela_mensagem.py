import json
import tkinter as tk
from pathlib import Path
from tkinter import ttk, messagebox, simpledialog

from assets.func.sessao.sessao import sessao_id

usuario_id = sessao_id()

def carregar_mensagens(caminho_json):
    if caminho_json.exists():
        with open(caminho_json, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return {}

def salvar_mensagens(caminho_json, mensagens):
    with open(caminho_json, "w", encoding="utf-8") as arquivo:
        json.dump(mensagens, arquivo, indent=4, ensure_ascii=False)

def tela_mensagem(raiz_principal):
    base_path = Path.home() / "nZap"
    base_path.mkdir(parents=True, exist_ok=True)
    
    caminho_json = base_path / "mensagens" / f".{usuario_id}.json"
    caminho_json.parent.mkdir(parents=True, exist_ok=True)
    
    mensagens = carregar_mensagens(caminho_json)
    
    mensagem_raiz = tk.Frame(raiz_principal)
    tk.Label(mensagem_raiz, text="Mensagens", font=("Arial", 14)).pack(pady=5)
    
    tree = ttk.Treeview(mensagem_raiz, columns=("#1", "#2"), show="headings")
    tree.heading("#1", text="Título")
    tree.heading("#2", text="Mensagem")
    tree.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)
    
    def atualizar_lista():
        tree.delete(*tree.get_children())
        for titulo, msg in mensagens.items():
            tree.insert("", tk.END, values=(titulo, msg))
    
    def editar_mensagem():
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma mensagem para editar.")
            return
        
        item = selecionado[0]
        titulo_atual, mensagem_atual = tree.item(item, "values")
        
        novo_titulo = simpledialog.askstring("Editar Título", "Edite o título:", initialvalue=titulo_atual)
        nova_mensagem = simpledialog.askstring("Editar Mensagem", "Edite a mensagem:", initialvalue=mensagem_atual)
        
        if novo_titulo and nova_mensagem:
            mensagens.pop(titulo_atual)
            mensagens[novo_titulo] = nova_mensagem
            salvar_mensagens(caminho_json, mensagens)
            atualizar_lista()
    
    def apagar_mensagem():
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma mensagem para apagar.")
            return
        
        item = selecionado[0]
        titulo_atual = tree.item(item, "values")[0]
        
        if messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir esta mensagem?"):
            mensagens.pop(titulo_atual)
            salvar_mensagens(caminho_json, mensagens)
            atualizar_lista()
    
    btn_editar = tk.Button(mensagem_raiz, text="Editar Mensagem", command=editar_mensagem)
    btn_editar.pack(pady=5)
    
    btn_apagar = tk.Button(mensagem_raiz, text="Apagar Mensagem", command=apagar_mensagem)
    btn_apagar.pack(pady=5)
    
    atualizar_lista()
    
    return mensagem_raiz
