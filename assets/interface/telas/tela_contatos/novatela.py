import os
import sys
import json
import tkinter as tk
from tkinter import ttk
from assets.func.contatos.importar_contatos.importar_do_excel import importar_excel
from assets.func.sessao.sessao import sessao_id

usuario_id = sessao_id()

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(script_dir, 'nZap'))

json_path = os.path.join("assets", "arquivos", "contatos", f"{usuario_id}.json")

os.makedirs(os.path.dirname(json_path), exist_ok=True)

ordem_atual = {"NOME": True, "TELEFONE": True, "EMAIL": True, "DATA": True}  # Estado da ordenação

def carregar_contatos():
    if not os.path.exists(json_path):
        with open(json_path, "w") as f:
            json.dump([], f)
    with open(json_path, "r") as f:
        return json.load(f)

def atualizar_lista(ordem=None):
    global dados
    dados = carregar_contatos()
    if ordem:
        chave, crescente = ordem
        dados.sort(key=lambda x: x.get(chave, ""), reverse=not crescente)
        ordem_atual[chave] = not crescente
    
    tree.delete(*tree.get_children())
    for item in dados:
        if item.get("STATUS", True):
            enviar_status = "✔" if item.get("ENVIAR", False) else ""
            tree.insert("", "end", values=(enviar_status, item.get("NOME", ""), item.get("TELEFONE", ""), item.get("EMAIL", ""), item.get("DATA", "")))

def ordenar_por(coluna):
    atualizar_lista(ordem=(coluna, ordem_atual[coluna]))

def tela_contatos(raiz_principal):
    frame_contato = tk.Frame(raiz_principal)
    frame_importar_botoes = tk.Frame(frame_contato, bg="#d0f0c0", padx=50, pady=5, borderwidth=1, relief="groove")
    frame_importar_botoes.pack(pady=5)

    tk.Label(frame_importar_botoes, text="Importar contatos do excel: ", bg="#d0f0c0", font=("Arial", 10)).pack(side=tk.LEFT, expand=True)
    tk.Button(frame_importar_botoes, text="Importar", font=("Arial", 10), command=lambda: [importar_excel(), atualizar_lista()]).pack(side=tk.LEFT, expand=True, padx=5)
    tk.Button(frame_importar_botoes, text="⟳", font=("Arial", 10), command=atualizar_lista).pack(side=tk.LEFT, expand=True, padx=5)

    frame_botoes = tk.Frame(frame_contato)
    frame_botoes.pack(pady=5)
    tk.Button(frame_botoes, text="Excluir", font=("Arial", 10), command=lambda: excluir_contato()).pack(side=tk.LEFT, expand=True, padx=5)

    columns = ("✔", "NOME", "TELEFONE", "EMAIL", "DATA")
    frame_tree = tk.Frame(frame_contato)
    frame_tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    tree_scroll = tk.Scrollbar(frame_tree)
    tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    global tree
    tree = ttk.Treeview(frame_tree, columns=columns, show="headings", yscrollcommand=tree_scroll.set)
    tree_scroll.config(command=tree.yview)

    for col in columns:
        tree.heading(col, text=col, command=lambda c=col: ordenar_por(c))
        tree.column(col, width=100, anchor="center")
    tree.column("✔", width=30, anchor="center")
    
    atualizar_lista()
    tree.pack(pady=10)
    return frame_contato
