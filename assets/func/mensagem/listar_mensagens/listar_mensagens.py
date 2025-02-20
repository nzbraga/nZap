import json
from pathlib import Path

def listar_mensagens(usuario_id: str):
    base_path = Path.home() / "nZap"
    caminho_json = base_path / "mensagens" / f".{usuario_id}.json"
    
    if not caminho_json.exists():
        print("Arquivo JSON não encontrado.")
        return []
    
    with open(caminho_json, "r", encoding="utf-8") as arquivo:
        try:
            dados = json.load(arquivo)
            return list(dados.keys())
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")
            return []
def obter_mensagem(usuario_id: str, indice: str):
    base_path = Path.home() / "nZap"
    caminho_json = base_path / "mensagens" / f".{usuario_id}.json"
    
    if not caminho_json.exists():
        print("Arquivo JSON não encontrado.")
        return None
    
    with open(caminho_json, "r", encoding="utf-8") as arquivo:
        try:
            dados = json.load(arquivo)
            return dados.get(indice, "Índice não encontrado.")
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")
            return None
