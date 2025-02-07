import os
import sys
import json
import pandas as pd
import tkinter as tk
from tkinter import filedialog

from assets.func.uteis.popUp import popUp
from assets.func.contatos.checar_duplicatas_excel_para_json.checar_duplicatas_excel_para_json import checar_duplicatas_excel_para_json

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
    
    # Definir o caminho correto para a pasta
    caminho_pasta_contatos = os.path.join( "assets/arquivos/contatos")

    # Criar a pasta se não existir
    if not os.path.exists(caminho_pasta_contatos):
        os.makedirs(caminho_pasta_contatos)

    # Definir o caminho correto do JSON
    caminho_json = os.path.join(caminho_pasta_contatos, "contatos.json")
    
    # Carregar a planilha
    info_excel = pd.read_excel(caminho_arquivo)
    info_excel.columns = ["nome", "telefone", "email", "data"]

    # Verificar contatos novos
    novos_contatos, contatos_existentes = checar_duplicatas_excel_para_json("Telefone", caminho_json, info_excel)
    print(f'novos contatos: {novos_contatos}')
    print(f'contatos existentes: {contatos_existentes}')
    if novos_contatos:
        # Adicionar novos contatos à lista
        contatos_existentes.extend(novos_contatos)

        # Remover duplicatas do JSON final
        contatos_sem_duplicatas = list({contato["Telefone"]: contato for contato in contatos_existentes}.values())

        # Salvar no JSON
        with open(caminho_json, "w", encoding="utf-8") as f:
            json.dump(contatos_sem_duplicatas, f, ensure_ascii=False, indent=4)

        print(f"{len(novos_contatos)} novos contatos adicionados!")
        popUp(f"{len(novos_contatos)} novos contatos adicionados!")
    else:
        print("Nenhum novo contato foi adicionado. Todos os números já existem no sistema.")
        popUp("Nenhum novo contato foi adicionado. Todos os números já existem no sistema.")
    print(f"Arquivo salvo em: {caminho_json}")

# Executar a função
if __name__ == "__main__":
    importar_excel()
