import json
from pathlib import Path

# Define a pasta base para armazenar os arquivos do programa
base_dir = Path.home() / "nZap"
base_dir.mkdir(parents=True, exist_ok=True)  # Cria a pasta se não existir

# Define o caminho do arquivo de sessão
ARQUIVO_SESSAO = base_dir / "sessao.json"

def autenticar_falso():
    sessao = {"id": "7400f8e0-95f5-4a08-9b58-9086a8f064f5", "nome": "VERSÃO TESTE"}
    
    with ARQUIVO_SESSAO.open("w", encoding="utf-8") as f:
        json.dump(sessao, f, indent=4)
    
    return True
