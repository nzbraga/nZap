import os
import json

def checar_duplicatas_excel_para_json(campo_checado, caminho_json, novo_campo):
    contatos_existentes = []

    # Carregar contatos existentes do JSON, se houver
    if os.path.exists(caminho_json):
        with open(caminho_json, "r", encoding="utf-8") as f:
            try:
                contatos_existentes = json.load(f)
            except json.JSONDecodeError:
                contatos_existentes = []  # Caso o arquivo esteja vazio ou corrompido

    # Criar um conjunto com os telefones já cadastrados, removendo espaços e formatando
    campo_existentes = {str(contato[campo_checado]).strip() for contato in contatos_existentes}

    # Padronizar os telefones do Excel antes da comparação
    novo_campo[campo_checado] = novo_campo[campo_checado].astype(str).str.strip()

    # Filtrar apenas contatos que ainda não existem
    novos_contatos = novo_campo[~novo_campo[campo_checado].isin(campo_existentes)].to_dict(orient="records")

    return novos_contatos, contatos_existentes
