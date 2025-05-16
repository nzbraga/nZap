import json
from pathlib import Path

def obter_mensagem(usuario_id, indice, entrada_mensagem):


    base_path = Path.home() / "nZap"
    caminho_json = base_path / "mensagens" / f".{usuario_id}.json"

    if not caminho_json.exists():
        print("Arquivo JSON não encontrado.")
        return None

    with open(caminho_json, "r", encoding="utf-8") as arquivo:
        try:
            dados = json.load(arquivo)

            # Verifica se os dados são um dicionário
            if not isinstance(dados, dict):
                print("Erro: O JSON deveria ser um dicionário.")
                return None

            # Define as chaves correspondentes ao índice
            chaves = list(dados.keys())  # ['ola', 'tarde']
            
            if indice < 0 or indice >= len(chaves):
                print("Erro: Índice fora do intervalo.")
                return None

            chave = chaves[indice]  
            mensagem = dados[chave]
        
            entrada_mensagem.delete("1.0", "end")
            entrada_mensagem.insert("1.0", mensagem)

        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")
            return None
