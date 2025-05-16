import json
from pathlib import Path
import tkinter as tk
from tkinter import simpledialog

def salvar_mensagem(usuario_id: str, texto: str):
    base_path = Path.home() / "nZap"
    base_path.mkdir(parents=True, exist_ok=True)
    
    caminho_json = base_path / "mensagens" / f".{usuario_id}.json"
    caminho_json.parent.mkdir(parents=True, exist_ok=True)  # Cria a pasta mensagens se não existir
    
    # Criar popup para usuário inserir o nome do índice
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    indice = simpledialog.askstring("Entrada", "Titulo da mensagem:")
    
    if not indice:
        print("Nenhum índice fornecido. Operação cancelada.")
        return
    
    # Carregar ou criar o dicionário
    if caminho_json.exists():
        with open(caminho_json, "r", encoding="utf-8") as arquivo:
            try:
                dados = json.load(arquivo)
            except json.JSONDecodeError:
                dados = {}
    else:
        dados = {}
    
    # Atualizar o dicionário e salvar
    dados[indice] = texto
    with open(caminho_json, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
    
    print(f"Texto salvo com o índice '{indice}' em {caminho_json}")