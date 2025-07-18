import json
from pathlib import Path
from assets.func.config.criar_config import criar_config

base_dir = Path.home() / "nZap" / "config"
base_dir.mkdir(parents=True, exist_ok=True)

def abrir_config(id):
    try:
        file_path = base_dir / f"{id}.json"
        
        if not file_path.exists():
            criar_config(id)

        with open(file_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        
        #print(f"Configuração carregada: {config}")
        return config

    except Exception as e:
        print(f"Erro ao abrir configuração: {e}")
        return None
