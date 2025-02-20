import sys
import json
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

from assets.func.uteis.popUp import popUp
from assets.func.contatos.checar_duplicatas_excel_para_json.checar_duplicatas_excel_para_json import checar_duplicatas_excel_para_json
from assets.func.sessao.sessao import sessao_id

usuario_id = sessao_id()

def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()  # Esconder a janela principal
    caminho_arquivo = filedialog.askopenfilename(title="Selecione o arquivo Excel", filetypes=[("Arquivos Excel", "*.xlsx;*.xls")])
    return caminho_arquivo

def importar_excel():
    caminho_arquivo = selecionar_arquivo()
    if not caminho_arquivo:
        print("Nenhum arquivo selecionado.")
        popUp("Nenhum arquivo selecionado.")
        return

    # Define a pasta de contatos dentro da pasta do usuário
    caminho_pasta_contatos = Path.home() / "nZap" / "contatos"
    caminho_pasta_contatos.mkdir(parents=True, exist_ok=True)  # Cria a pasta se não existir

    # Define o caminho completo do JSON
    caminho_json = caminho_pasta_contatos / f".{usuario_id}.json"

    # Carrega os contatos do Excel
    info_excel = pd.read_excel(caminho_arquivo)
    info_excel.columns = ["nome", "telefone", "email", "aniversario"]

    # Converter nomes para maiúsculas
    info_excel["nome"] = info_excel["nome"].str.upper()

    # Verifica duplicatasimport json
from pathlib import Path

# Define a pasta base para armazenar os arquivos do programa
base_dir = Path.home() / "nZap"
sessao_dir = base_dir / "sessao"
sessao_dir.mkdir(parents=True, exist_ok=True)  # Garante que a pasta "sessao" exista

# Define os caminhos dos arquivos JSON
ARQUIVO_USUARIOS = base_dir / ".usuarios.json"
ARQUIVO_SESSAO = sessao_dir / ".sessao.json"

def autenticar_login(raw_usuario, senha):
    usuario = raw_usuario.strip().upper()
    senha = senha.strip()  # Garantir que a senha também não tenha espaços extras
    
    try:
        with ARQUIVO_USUARIOS.open("r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):  # Verifica se os dados são uma lista válida
                raise ValueError("Formato inválido no arquivo de usuários.")
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        data = []  # Se houver erro, assume que não há usuários cadastrados

    for user in data:
        if not user.get("status", True):  # Se status for False, negar login
            return False
        
        if user.get("usuario") == usuario and user.get("senha") == senha:
            # Criando sessão com ID e nome do usuário autenticado
            sessao = {"id": user.get("id", "desconhecido"), "nome": user.get("usuario", "desconhecido")}
            with ARQUIVO_SESSAO.open("w", encoding="utf-8") as f:
                print(f'arquivo criado na pasta{ARQUIVO_SESSAO} com sucesso.')
                json.dump(sessao, f, indent=4)
            return True
    
    return False

    novos_contatos, contatos_existentes = checar_duplicatas_excel_para_json("telefone", caminho_json, info_excel)

    # Adiciona status aos novos contatos
    for contato in novos_contatos:
        contato["status"] = True
        contato["enviar"] = True

    # Remove duplicatas, mantendo os mais recentes
    contatos_sem_duplicatas = list({contato["telefone"]: contato for contato in contatos_existentes + novos_contatos}.values())

    # Salva o JSON
    with caminho_json.open("w", encoding="utf-8") as f:
        json.dump(contatos_sem_duplicatas, f, ensure_ascii=False, indent=4)

    print(f"{len(novos_contatos)} novos contatos adicionados!")
    print(f"Arquivo salvo em: {caminho_json}")
    popUp(f"{len(novos_contatos)} novos contatos adicionados!")

if __name__ == "__main__":
    importar_excel()
