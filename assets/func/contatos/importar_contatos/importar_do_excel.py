import os
import sys
import json
import pandas as pd
import tkinter as tk
from tkinter import filedialog

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
    
    caminho_pasta_contatos = os.path.join("assets/arquivos/contatos")
    if not os.path.exists(caminho_pasta_contatos):
        os.makedirs(caminho_pasta_contatos)
    
   
    caminho_json = os.path.join(caminho_pasta_contatos, f"{usuario_id}.json")
  
    info_excel = pd.read_excel(caminho_arquivo)
    info_excel.columns = ["nome", "telefone", "EMAIL", "aniversario"]
    
    # Converter nomes para maiúsculas
    info_excel["nome"] = info_excel["nome"].str.upper()
    
    novos_contatos, contatos_existentes = checar_duplicatas_excel_para_json("telefone", caminho_json, info_excel)
    
    for contato in novos_contatos:
        contato["status"] = True  # Define como novo contato
        contato["enviar"] = True  # Define como novo contato
    
    contatos_sem_duplicatas = list({contato["telefone"]: contato for contato in contatos_existentes + novos_contatos}.values())
    
    with open(caminho_json, "w", encoding="utf-8") as f:
        json.dump(contatos_sem_duplicatas, f, ensure_ascii=False, indent=4)
    
    print(f"{len(novos_contatos)} novos contatos adicionados!")
    print(f"Arquivo salvo em: {caminho_json}")
    popUp(f"{len(novos_contatos)} novos contatos adicionados!")

if __name__ == "__main__":
    importar_excel()
