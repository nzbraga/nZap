import json


def sessao_id():
    try:
# Caminho do arquivo JSON
        caminho_arquivo = 'assets/arquivos/sessao/.sessao.json'

        # Abrindo e carregando o JSON
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)  # Carrega os dados do JSON para um dicionário

        # Acessando o valor de "id"
        id_sessao = dados.get("id")  # Usa .get() para evitar erros caso a chave não exista
        #print(f'ID da sessão: {id_sessao}')
        return id_sessao
    except FileNotFoundError:
        print(f'Arquivo {caminho_arquivo} não encontrado.')
        return False

def sessao_nome():
    try:
# Caminho do arquivo JSON
        caminho_arquivo = 'assets/arquivos/sessao/.sessao.json'

        # Abrindo e carregando o JSON
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)  # Carrega os dados do JSON para um dicionário

        # Acessando o valor de "id"
        nome_sessao = dados.get("nome")  # Usa .get() para evitar erros caso a chave não exista
        #print(f'nome da sessão: {nome_sessao}')
        return nome_sessao
    except FileNotFoundError:
        print(f'Arquivo {caminho_arquivo} não encontrado.')
        return False