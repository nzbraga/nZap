import re
from datetime import datetime

from assets.func.uteis.popUp import popUp



def formatar_valor(contato, chave):
    valor = contato.get(chave)  # Obtém o valor de forma segura

    if isinstance(valor, str):
        return valor.upper()  # Retorna string com a primeira letra maiúscula
    elif isinstance(valor, datetime):
        return valor.strftime("%d/%m")  # Retorna data formatada como dia/mês
    
    return valor

def substituir_variaveis(mensagem, contato):
  
    def substituir(match):
        chave = match.group(1)
        if chave not in contato:
            raise popUp(f"Palavra chave: '{chave}' não encontrada!")
            #raise ValueError(f"Erro: chave '{chave}' não encontrada para o contato {contato.get('nome', 'Desconhecido')}.")
        return formatar_valor(contato, chave)
    
    try:
        return re.sub(r"@(\w+)", substituir, mensagem)
    except ValueError:
        return None  # Retorna None para indicar erro
