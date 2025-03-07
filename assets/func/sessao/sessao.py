import json
from pathlib import Path

# Define o caminho seguro para armazenar arquivos de sessão
base_dir = Path.home() / "nZap" 
base_dir.mkdir(parents=True, exist_ok=True)  # Garante que a pasta exista
caminho_arquivo = base_dir / "sessao" / ".sessao.json"

def sessao_id():
    try:
        # Abrindo e carregando o JSON
        if caminho_arquivo.exists():
            with caminho_arquivo.open('r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)  # Carrega os dados do JSON para um dicionário

            # Acessando o valor de "id"
            id_sessao = dados.get("id")  # Usa .get() para evitar erros caso a chave não exista
            #print(f'ID da sessão: {id_sessao}')
            return id_sessao
        else:
            print(f'Arquivo {caminho_arquivo} não encontrado.')
            return False
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Erro ao ler o arquivo {caminho_arquivo}: {e}')
        return False

def sessao_nome():
    try:
        # Abrindo e carregando o JSON
        if caminho_arquivo.exists():
            with caminho_arquivo.open('r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)  # Carrega os dados do JSON para um dicionário

            # Acessando o valor de "nome"
            nome_sessao = dados.get("nome").upper()  # Usa .get() para evitar erros caso a chave não exista
            #print(f'nome da sessão: {nome_sessao}')
            return nome_sessao
        else:
            print(f'Arquivo {caminho_arquivo} não encontrado.')
            return False
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Erro ao ler o arquivo {caminho_arquivo}: {e}')
        return False
