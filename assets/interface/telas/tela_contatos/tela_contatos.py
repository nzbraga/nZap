"""

import os
import sys
import json
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path

from assets.func.contatos.importar_contatos.importar_do_excel import importar_excel
from assets.interface.telas.tela_criar_contato.tela_criar_contato import tela_criar_contatos
from assets.func.sessao.sessao import sessao_id

usuario_id = sessao_id()


base_path = Path.home() / "nZap" 
base_path.mkdir(parents=True, exist_ok=True)  # Cria a pasta se não existir

# Define o caminho completo do JSON
caminho_json = base_path / "contatos" / f".{usuario_id}.json"

# Garantir que o diretório existe
os.makedirs(os.path.dirname(caminho_json), exist_ok=True)

ordem_atual = {"nome": True, "telefone": True, "email": True, "aniversario": True}  # Estado da ordenação

# Carregar ou criar o arquivo JSON
def carregar_contatos():
    if not os.path.exists(caminho_json):
        with open(caminho_json, "w") as f:
            json.dump([], f)  # Cria um arquivo JSON vazio
    
    with open(caminho_json, "r") as f:
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
        if item.get("status", True):
            enviar_status = "✔" if item.get("enviar", False) else ""
            tree.insert("", "end", values=(enviar_status, item.get("nome", ""), item.get("telefone", ""), item.get("email", ""), item.get("aniversario", "")))

# Atualizar o JSON ao alterar a checkbox
def atualizar_enviar(telefone, status):
    contatos = carregar_contatos()
    for contato in contatos:
        if contato["telefone"] == telefone:
            contato["enviar"] = status
    with open(caminho_json, "w", encoding="utf-8") as f:
        json.dump(contatos, f, ensure_ascii=False, indent=4)

def ordenar_por(coluna):
    atualizar_lista(ordem=(coluna, ordem_atual[coluna]))

# Excluir contato (marcar status como False)
def excluir_contato():
    selecionados = tree.selection()
    if not selecionados:
        return
    
    contatos = carregar_contatos()
    telefones_selecionados = [tree.item(item, "values")[2] for item in selecionados]
    
    for contato in contatos:
        if contato["telefone"] in telefones_selecionados:
            contato["status"] = False
            contato["enviar"] = False
    
    with open(caminho_json, "w", encoding="utf-8") as f:
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
        "nome": valores[1],
        "telefone": valores[2],
        "email": valores[3],
        "aniversario": valores[4]
    }
    
    tela_criar_contatos(atualizar_lista, contato)

def tela_contatos(raiz_principal):
    global tree
    def filtrar_contatos(event=None):
        termo = entrada_filtro.get().strip().lower()  # Captura o texto digitado e converte para minúsculas
        contatos = carregar_contatos()
        
        # Desmarcar todos os "enviar"
        for contato in contatos:
            contato["enviar"] = False
        
        # Atualiza o JSON com os contatos desmarcados
        with open(caminho_json, "w", encoding="utf-8") as f:
            json.dump(contatos, f, ensure_ascii=False, indent=4)

        # Filtra os contatos
        filtrados = [
            contato for contato in contatos 
            if contato.get("status", True) and (
                termo in contato.get("nome", "").lower() or 
                termo in contato.get("telefone", "").lower() or 
                termo in contato.get("email", "").lower() or
                termo in contato.get("aniversario", "").lower() 
            )
        ]

        # Atualiza a exibição na interface
        tree.delete(*tree.get_children())
        for item in filtrados:
            tree.insert("", "end", values=(
                "",  # Checkbox sempre vazia após filtro
                item.get("nome", ""), 
                item.get("telefone", ""), 
                item.get("email", ""), 
                item.get("aniversario", "")
            ))

    def limpar_filtro():
        entrada_filtro.delete(0, tk.END)  # Apaga o texto digitado
        atualizar_lista() 

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
        command=lambda: [importar_excel(), atualizar_lista()]
    ).pack(side=tk.LEFT, expand=True, padx=5)

    tela_botoes = tk.Frame(tela_contato)
    tela_botoes.pack(pady=5)
    tela_filtro = tk.Frame(tela_contato)
    tela_filtro.pack(pady=5)
    
    tk.Button(
        tela_botoes,
        text="Adicionar Contato",
        command=lambda: tela_criar_contatos(atualizar_lista),
        font=("Arial", 10)).pack(side=tk.LEFT, expand=True, padx=5)
    tk.Button(
        tela_botoes,
        text="Editar",
        command=lambda: editar_contato(),
        font=("Arial", 10)).pack(side=tk.LEFT, expand=True, padx=5)
    tk.Label(tela_filtro, text="Filtrar: ", font=("Arial", 10)).pack(side=tk.LEFT, expand=True)
    entrada_filtro = tk.Entry(tela_filtro, font=("Arial", 10))
    entrada_filtro.pack(side=tk.LEFT, expand=True, padx=5)
    entrada_filtro.bind("<KeyRelease>", filtrar_contatos)
   
    tk.Button(
        tela_filtro,
        text="Limpar",
        command=lambda: limpar_filtro(),
        font=("Arial", 10)).pack(side=tk.LEFT, expand=True, padx=5)
    tk.Button(
        tela_botoes,
        text="Excluir",
        command=excluir_contato,
        font=("Arial", 10)).pack(side=tk.LEFT, expand=True, padx=5)
    tk.Button(
        tela_botoes,
        text="⟳", font=("Arial", 10),
        command=atualizar_lista
    ).pack(side=tk.LEFT, expand=True, padx=5)
    
    columns = ("✔", "nome", "telefone", "email", "aniversario")
    tela_tree = tk.Frame(tela_contato)
    tela_tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    
    tree_scroll = tk.Scrollbar(tela_tree)
    tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    
    
    tree = ttk.Treeview(tela_tree, columns=columns, show="headings", yscrollcommand=tree_scroll.set)
    tree_scroll.config(command=tree.yview)

    for col in columns:
        tree.heading(col, text=col, command=lambda c=col: ordenar_por(c))
        tree.column(col, width=100, anchor="center")

    tree.column("✔", width=30, anchor="center")
    tree.column("nome", width=100)
    tree.column("telefone", width=80)
    tree.column("email", width=100)
    tree.column("aniversario", width=80, anchor="center")
    
    tree.bind("<ButtonRelease-1>", alternar_check)
    tree.bind("<Button-1>", desmarcar_tudo, add="+")  # Desmarca seleção ao clicar fora
    tree.heading("✔", text="✔", command=alternar_tudo)  # Adiciona alternar_tudo no cabeçalho da checkbox
    tree.pack(pady=10)
    
    atualizar_lista()
    tree.pack(pady=10)
    return tela_contato

    """