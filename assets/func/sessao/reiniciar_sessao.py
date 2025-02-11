import os
import json
import time
from datetime import datetime, timedelta

def limpar_data():
    """
    Limpa o arquivo de sessao se ele tiver mais de um dia.
    
    Verifica se o arquivo de sess o existe. Se existir, l  a data
    salva nele e compara com a data atual. Se a data atual for
    maior ou igual  data salva + 1 dia, apaga o arquivo.
    
    Caso o arquivo n o exista, imprime uma mensagem de erro.
    """
    caminho = 'assets/arquivo/sessao/.sessao.json'
    if os.path.exists(caminho):
        with open(caminho, 'r') as f:
            dados = json.load(f)
            data_salva = datetime.fromisoformat(dados['data'])
            
        if datetime.now() >= data_salva + timedelta(days=1):
            os.remove(caminho)
            print("Arquivo de sessão apagado.")
        else:
            print("Ainda não é hora de apagar o arquivo.")
    else:
        print("Arquivo não encontrado.")
    
    print("limpar data rodando...")

if __name__ == "__main__":
    time.sleep(2)  # Simula tempo de espera
    limpar_data()
