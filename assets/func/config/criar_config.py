import json
from pathlib import Path
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import remetente

base_dir = Path.home() / "nZap" / "config"
base_dir.mkdir(parents=True, exist_ok=True)

def criar_config(id, remetente_logado=str(remetente), primeira_hora=8, ultima_hora=18, intervalo_envio=12):
    try:
        config = {
            "remetente": remetente_logado,
            "primeira_hora": primeira_hora,
            "ultima_hora": ultima_hora,
            "intervalo_envio": intervalo_envio
        }
        print(f'Configuração: {config}')
        file_path = base_dir / f"{id}.json"  # sem ponto, por segurança
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=4)

        print(f"Configuração salva em: {file_path}")

    except Exception as e:
        print(f"Erro ao salvar configuração: {e}")
