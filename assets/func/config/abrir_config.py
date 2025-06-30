import json
from pathlib import Path

base_dir = Path.home() / "nZap" / "config"
base_dir.mkdir(parents=True, exist_ok=True)

def abrir_config(id):
    try:
        file_path = base_dir / f"{id}.json"
        
        if not file_path.exists():
            #print(f"Arquivo de configuração '{file_path}' não encontrado.")
            return None

        with open(file_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        
        #print(f"Configuração carregada: {config}")
        return config

    except Exception as e:
        print(f"Erro ao abrir configuração: {e}")
        return None
