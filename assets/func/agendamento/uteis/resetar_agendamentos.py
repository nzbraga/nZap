import json
import time
import threading
from pathlib import Path
from assets.func.sessao.sessao import sessao_id

usuario_id = sessao_id()

base_dir = Path.home() / "nZap"
agendado_dir = base_dir / "agendados"

ARQUIVO_AGENDADO = agendado_dir / f".{usuario_id}.json"

def resetar_agendamentos(arquivo):
    time.sleep(86400)  # Aguarda 1 minuto antes de repetir
    while True:        
        try:
            print("\nVerificando se o arquivo existe...")

            # Verifica se o arquivo existe
            if not arquivo.exists():
                print("Arquivo JSON não encontrado.")
                time.sleep(60)
                continue

            print("Arquivo encontrado! Lendo conteúdo...")

            # Lê o arquivo JSON
            with open(arquivo, 'r', encoding='utf-8') as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError as e:
                    print(f"Erro ao decodificar JSON: {e}")
                    time.sleep(60)
                    continue

            print(f"Conteúdo do JSON carregado: {dados}")

            # Garante que os dados são uma lista
            if not isinstance(dados, list):
                print("Erro: JSON deve conter uma lista de objetos.")
                time.sleep(60)
                continue

            print("Resetando 'enviado' para False...")

            # Reseta o campo "enviado" para False
            for item in dados:
                print(f"Processando item: {item}")  # Log do item atual
                if isinstance(item, dict) and "enviado" in item:
                    item["enviado"] = False  

            print("Salvando o JSON atualizado...")

            # Escreve de volta no JSON
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)

            print("Todos os agendamentos foram resetados!")

        except Exception as e:
            print(f"Erro inesperado: {e}")


