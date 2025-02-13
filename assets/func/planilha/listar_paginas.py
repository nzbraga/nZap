import os
import openpyxl
import tkinter as tk

from tkinter import filedialog

def listar_paginas():
    try:
        caminho_arquivo = "contatos.xlsx"  # Caminho do arquivo na raiz do projeto
        
        # Verifica se o arquivo existe
        if not os.path.exists(caminho_arquivo):
            # Abre a janela para selecionar o arquivo
            root = tk.Tk()
            root.withdraw()  # Esconde a janela principal do Tkinter
            caminho_arquivo = filedialog.askopenfilename(
                title="Selecione o arquivo Excel",
                filetypes=[("Arquivos Excel", "*.xlsx;*.xls")]  # Filtra apenas arquivos Excel
            )

            if not caminho_arquivo:  # Caso o usuário cancele a seleção
                print("Nenhum arquivo selecionado.")
                return []
        
        # Abre a planilha em modo somente leitura
        planilha = openpyxl.load_workbook(caminho_arquivo, read_only=True)
        
        # Pega os nomes das sheets
        nomes_paginas = planilha.sheetnames      
        planilha.close()
        
        return nomes_paginas
    
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado. Verifique o caminho do arquivo.")
        return []
    except Exception as e:
        print(f"Erro inesperado ao listar: {e}")
        return []


