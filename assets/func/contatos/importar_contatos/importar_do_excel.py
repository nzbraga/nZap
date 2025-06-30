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
    #print(f'info_excel: {info_excel}\n info_excel.dtypes: {info_excel.dtypes}')

    # Converter nomes para maiúsculas
    info_excel["nome"] = info_excel["nome"].str.upper()
    info_excel["aniversario"] = info_excel["aniversario"].replace("\\", "-").replace("/", "-")
    
    if info_excel["telefone"] == "Telefone" or info_excel["telefone"] == "telefone":
        info_excel["telefone"] = "contato"
    # Verifica duplicatas
    novos_contatos, contatos_existentes = checar_duplicatas_excel_para_json("telefone", caminho_json, info_excel)
    #print(f'novos_contatos: {novos_contatos}\n contatos_existentes: {contatos_existentes}')

    # Adiciona status aos novos contatos
    for contato in novos_contatos:
        contato["status"] = True
        contato["enviar"] = False

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
