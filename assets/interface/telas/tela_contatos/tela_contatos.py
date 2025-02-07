import os
import sys
import json
import tkinter as tk
from tkinter import ttk

from assets.func.contatos.importar_contatos.importar_do_excel import importar_excel

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(script_dir, 'nZap'))

# Caminho do arquivo JSON
json_path = os.path.join("assets", "arquivos", "contatos", "contatos.json")

# Garantir que o diretório existe
os.makedirs(os.path.dirname(json_path), exist_ok=True)

# Carregar ou criar o arquivo JSON
def carregar_contatos():
    if not os.path.exists(json_path):
        with open(json_path, "w") as f:
            json.dump([], f)  # Cria um arquivo JSON vazio
    
    with open(json_path, "r") as f:
        return json.load(f)

dados = carregar_contatos()

def tela_contatos(raiz_principal):
    def toggle_check(item):
        current_value = tree.item(item, "values")[0]
        new_value = "✔" if current_value == "" else ""
        tree.item(item, values=(new_value, *tree.item(item, "values")[1:]))

    def toggle_all():
        items = tree.get_children()
        if not items:
            return
        
        all_selected = all(tree.item(i, "values")[0] == "✔" for i in items)
        new_value = "" if all_selected else "✔"
        
        for item in items:
            tree.item(item, values=(new_value, *tree.item(item, "values")[1:]))

    frame_contato = tk.Frame(raiz_principal)
    frame_importar_botoes = tk.Frame(frame_contato)
    frame_importar_botoes.pack(pady=5)

    tk.Label(frame_importar_botoes, text="Importar contatos do excel: ", font=("Arial", 10)).pack(side=tk.LEFT, expand=True)
    tk.Button(
        frame_importar_botoes,
        text="Importar", font=("Arial", 10),
        command=lambda: importar_excel()).pack(side=tk.LEFT, expand=True, padx=5)

    frame_botoes = tk.Frame(frame_contato)
    frame_botoes.pack(pady=5)

    tk.Button(frame_botoes, text="Adicionar Contato", font=("Arial", 10)).pack(side=tk.LEFT, expand=True, padx=5)
    tk.Button(frame_botoes, text="Filtrar", font=("Arial", 10)).pack(side=tk.LEFT, expand=True, padx=5)
    
    columns = ("✔", "Nome", "Telefone", "Email", "Data")
    frame_tree = tk.Frame(frame_contato)
    frame_tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    
    tree_scroll = tk.Scrollbar(frame_tree)
    tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    
    tree = ttk.Treeview(frame_tree, columns=columns, show="headings", yscrollcommand=tree_scroll.set)
    tree_scroll.config(command=tree.yview)

    for col in columns:
        tree.heading(col, text=col)
    
    tree.column("✔", width=30, anchor="center")
    tree.column("Nome", width=100)
    tree.column("Telefone", width=80)
    tree.column("Email", width=100)
    tree.column("Data", width=80, anchor="center")

    for item in dados:
        tree.insert("", "end", values=("", item.get("nome", ""), item.get("telefone", ""), item.get("email", ""), item.get("data", "")))

    tree.bind("<ButtonRelease-1>", lambda event: toggle_check(tree.focus()))
    tree.heading("✔", text="✔", command=toggle_all)
    tree.pack(pady=10)
    
    return frame_contato
