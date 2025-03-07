import os
import json
from pathlib import Path

def checar_duplicatas_excel_para_json(campo_checado, nome_arquivo_json, novo_campo):
    # Define a pasta do usuário para salvar o JSON
    user_dir = Path.home() / "nZap"
    user_dir.mkdir(exist_ok=True)  # Cria a pasta se não existir

    # Define o caminho completo do JSON
    caminho_json = user_dir / nome_arquivo_json

    contatos_existentes = []

    # Carregar contatos existentes do JSON, se houver
    if caminho_json.exists():
        with caminho_json.open("r", encoding="utf-8") as f:
            try:
                contatos_existentes = json.load(f)
            except json.JSONDecodeError:
                contatos_existentes = []  # Caso o arquivo esteja vazio ou corrompido

    # Criar um conjunto com os valores do campo_checado já cadastrados
    campo_existentes = {str(contato[campo_checado]).strip() for contato in contatos_existentes}

    # Padronizar os dados do novo campo antes da comparação
    novo_campo[campo_checado] = novo_campo[campo_checado].astype(str).str.strip()

    # Filtrar apenas contatos que ainda não existem no JSON
    novos_contatos = novo_campo[~novo_campo[campo_checado].isin(campo_existentes)].to_dict(orient="records")

    return novos_contatos, contatos_existentes
