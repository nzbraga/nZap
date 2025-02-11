import os
import sys
import json
import tkinter as tk
from tkinter import ttk, messagebox
from assets.func.contatos.importar_contatos.importar_do_excel import importar_excel
from assets.interface.telas.tela_criar_contato.tela_criar_contato import tela_criar_contatos
from assets.interface.telas.tela_filtrar_contatos.tela_filtrar_contatos import tela_filtro

from assets.func.sessao.sessao import sessao_id

usuario_id = sessao_id()

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(script_dir, 'nZap'))

# Caminho do arquivo JSON
json_path = os.path.join("assets", "arquivos", "contatos", f"{usuario_id}.json")

# Garantir que o diretório existe
os.makedirs(os.path.dirname(json_path), exist_ok=True)
ordem_atual = {"NOME": True, "TELEFONE": True, "EMAIL": True, "DATA": True}  # Estado da ordenação
# Carregar ou criar o arquivo JSON
def carregar_contatos():
    if not os.path.exists(json_path):
        with open(json_path, "w") as f:
            json.dump([], f)  # Cria um arquivo JSON vazio
    
    with open(json_path, "r") as f:
        return json.load(f)

# Atualizar lista de contatos no Treeview
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

# Atualizar o JSON ao alterar a checkbox
def atualizar_enviar(telefone, status):
    contatos = carregar_contatos()
    for contato in contatos:
        if contato["TELEFONE"] == telefone:
            contato["ENVIAR"] = status
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(contatos, f, ensure_ascii=False, indent=4)

def ordenar_por(coluna):
    atualizar_lista(ordem=(coluna, ordem_atual[coluna]))

# Excluir contato (marcar STATUS como False)
def excluir_contato():
    selecionados = tree.selection()
    if not selecionados:
        return
    
    contatos = carregar_contatos()
    telefones_selecionados = [tree.item(item, "values")[2] for item in selecionados]
    
    for contato in contatos:
        if contato["TELEFONE"] in telefones_selecionados:
            contato["STATUS"] = False
            contato["ENVIAR"] = False
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(contatos, f, ensure_ascii=False, indent=4)
    
    atualizar_lista()
def editar_contato():
    selecionados = tree.selection()
    if not selecionados:
        messagebox.showerror("Erro", "Selecione um contato para editar.")
        return
    
    item = selecionados[0]
    valores = tree.item(item, "values")

    contato = {
        "NOME": valores[1],
        "TELEFONE": valores[2],
        "EMAIL": valores[3],
        "DATA": valores[4]
    }
    
    tela_criar_contatos(atualizar_lista, contato)

def tela_contatos(raiz_principal):
    def desmarcar_enviar_todos():
        items = tree.get_children()
        for item in items:
            valores = tree.item(item, "values")
            telefone = valores[2]
            # Marcar como False em todos os itens
            tree.item(item, values=("", *valores[1:]))  # Remover o "✔"
            atualizar_enviar(telefone, False)
    def alternar_check(event):
        item = tree.identify_row(event.y)  # Identifica a linha clicada
        col = tree.identify_column(event.x)  # Identifica a coluna clicada
        
        if col == "#1" and item:  # Se for a coluna da checkbox
            valores = tree.item(item, "values")
            telefone = valores[2]
            new_value = "✔" if valores[0] == "" else ""
            tree.item(item, values=(new_value, *valores[1:]))
            atualizar_enviar(telefone, new_value == "✔")
    
    def alternar_tudo():
        items = tree.get_children()
        if not items:
            return
        
        tudo_selected = all(tree.item(i, "values")[0] == "✔" for i in items)
        new_value = "" if tudo_selected else "✔"
        
        for item in items:
            valores = tree.item(item, "values")
            telefone = valores[2]
            tree.item(item, values=(new_value, *valores[1:]))
            atualizar_enviar(telefone, new_value == "✔")
    
    def desmarcar_tudo(event):
        if tree.identify_row(event.y) == "":  # Se clicar fora de uma linha, desmarca seleção
            tree.selection_remove(tree.selection())
    
    tela_contato = tk.Frame(raiz_principal)
    tela_importar_botoes = tk.Frame(tela_contato, bg="#d0f0c0", padx=50, pady=5, borderwidth=1, relief="groove")
    tela_importar_botoes.pack(pady=5)

    tk.Label(tela_importar_botoes, text="Importar contatos do excel: ", bg="#d0f0c0", font=("Arial", 10)).pack(side=tk.LEFT, expand=True)
    
    tk.Button(
        tela_importar_botoes,
        text="Importar",
        font=("Arial", 10),
        command=lambda:
        [importar_excel(), atualizar_lista()]
    ).pack(side=tk.LEFT, expand=True, padx=5)
    
    
    
    tela_botoes = tk.Frame(tela_contato)
    tela_botoes.pack(pady=5)
    
    tk.Button(
        tela_botoes,
        text="Adicionar Contato",
        command=lambda: tela_criar_contatos(atualizar_lista) ,
        font=("Arial", 10)).pack(side=tk.LEFT, expand=True, padx=5)
    tk.Button(
        tela_botoes,
        text="Editar",
        command=lambda:editar_contato(),
        font=("Arial", 10)).pack(side=tk.LEFT, expand=True, padx=5)
    tk.Button(
        tela_botoes,
        text="Filtrar",
        command=lambda: tela_filtro(tree, atualizar_lista, desmarcar_enviar_todos),
        font=("Arial", 10)).pack(side=tk.LEFT, expand=True, padx=5)
    tk.Button(
        tela_botoes,
        text="Excluir",
        command=excluir_contato,
        font=("Arial", 10), ).pack(side=tk.LEFT, expand=True, padx=5)
    tk.Button(
        tela_botoes,
        text="⟳", font=("Arial", 10),
        command=atualizar_lista
    ).pack(side=tk.LEFT, expand=True, padx=5)
    
    columns = ("✔", "NOME", "TELEFONE", "EMAIL", "DATA")
    tela_tree = tk.Frame(tela_contato)
    tela_tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    
    tree_scroll = tk.Scrollbar(tela_tree)
    tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    
    global tree
    tree = ttk.Treeview(tela_tree, columns=columns, show="headings", yscrollcommand=tree_scroll.set)
    tree_scroll.config(command=tree.yview)

    for col in columns:
        tree.heading(col, text=col, command=lambda c=col: ordenar_por(c))
        tree.column(col, width=100, anchor="center")

    tree.column("✔", width=30, anchor="center")
    tree.column("NOME", width=100)
    tree.column("TELEFONE", width=80)
    tree.column("EMAIL", width=100)
    tree.column("DATA", width=80, anchor="center")
    
    tree.bind("<ButtonRelease-1>", alternar_check)
    tree.bind("<Button-1>", desmarcar_tudo, add="+")  # Desmarca seleção ao clicar fora
    tree.heading("✔", text="✔", command=alternar_tudo)  # Adiciona alternar_tudo no cabeçalho da checkbox
    tree.pack(pady=10)
    
    atualizar_lista()
    tree.pack(pady=10)
    return tela_contato
