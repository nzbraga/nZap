import os
import sys
import json
import pandas as pd

sys.path.insert(0, 'C:/gitHub/nZap')

from assets.func.uteis.popUp import popUp
from assets.func.contatos.checar_duplicatas_excel_para_json.checar_duplicatas_excel_para_json import checar_duplicatas_excel_para_json

def importar_excel(arquivo):
    caminho_json = "./assets/arquivos/contatos/contatos.json"

    # Carregar a planilha
    info_excel = pd.read_excel(arquivo)
    info_excel.columns = ["Nome", "Telefone", "Email", "Data"]

    # Verificar contatos novos
    novos_contatos, contatos_existentes = checar_duplicatas_excel_para_json("Telefone", caminho_json, info_excel)

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

# Teste
importar_excel('contatos.xlsx')
