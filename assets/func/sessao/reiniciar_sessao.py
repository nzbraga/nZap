import json
import time
import os
from datetime import datetime, timedelta
from pathlib import Path

# Define o caminho seguro para armazenar arquivos, evitando problemas no PyInstaller
base_dir = Path.home() / "nZap" / "sessao"
base_dir.mkdir(parents=True, exist_ok=True)  # Garante que a pasta existe
caminho_sessao = base_dir / ".sessao.json"

def limpar_data():
    """
    Limpa o arquivo de sessão se tiver mais de um dia.
    
    Se o arquivo de sessão existir, verifica a data salva e compara com a data atual.
    Se a data for superior a 1 dia, apaga o arquivo. Caso contrário, mantém.
    """
    if caminho_sessao.exists():
        try:
            with caminho_sessao.open("r", encoding="utf-8") as f:
                dados = json.load(f)
                data_salva = datetime.fromisoformat(dados.get("data", "2000-01-01T00:00:00"))

            if datetime.now() >= data_salva + timedelta(days=1):
                caminho_sessao.unlink()  # Remove o arquivo
                print("Arquivo de sessão apagado.")

        except (json.JSONDecodeError, KeyError, ValueError):
            print("Erro ao ler o arquivo de sessão. Apagando por segurança.")
            caminho_sessao.unlink()

    else:
        print("Arquivo de sessão não encontrado.")

    print("Limpar data rodando...")

if __name__ == "__main__":
    time.sleep(2)  # Simula tempo de espera
    limpar_data()
