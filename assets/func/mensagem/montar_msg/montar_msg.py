import re
from tkinter import messagebox
import time

from assets.func.uteis.popUp import popUp
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import enviar_mensagem
from assets.func.mensagem.saudacao.saudacao import definir_saudacao

def substituir_variaveis(mensagem, contato):
    """
    Substitui palavras iniciadas com @ pelos valores correspondentes do dicionário contato.
    Lança um erro e para a execução se uma chave não for encontrada.
    """
    def substituir(match):
        chave = match.group(1)
        if chave not in contato:
            raise popUp(f"Erro: chave '{chave}' não encontrada para o contato {contato.get('nome', 'Desconhecido')}.")
            #raise ValueError(f"Erro: chave '{chave}' não encontrada para o contato {contato.get('nome', 'Desconhecido')}.")
        return contato[chave]
    
    try:
        return re.sub(r"@(\w+)", substituir, mensagem)
    except ValueError:
        return None  # Retorna None para indicar erro

limitador = 0

def montar_msg(contatos, mensagem, destinatario= 'contato', limite=5):
    global limitador
    if not contatos:
        popUp("Nenhum contato selecionado.")
        return

    if not mensagem or not mensagem.strip():
        popUp("Mensagem vazia.")
        return
  
      
    for contato in contatos:
        mensagem_personalizada = substituir_variaveis(mensagem, contato)
           
        if mensagem_personalizada is None:
            popUp(f"Erro ao processar mensagem para {contato.get('nome', 'Desconhecido')}.")
            return  # Interrompe a execução se houver erro
        
        if not contato.get(destinatario):  # Verifica se a chave não existe ou está vazia
            popUp(f"Contato não encontrado.\nConfirme se o campo '{destinatario}' existe no arquivo Excel.")
        
        mensagem_completa = f"{mensagem_personalizada}"
        print(f"contato: {contato[destinatario]}\nmensagem: {mensagem_completa}")
        enviar_mensagem(contato[destinatario], mensagem_completa)
        print('pausa de 3s')
        time.sleep(3)
        
        limitador += 1
        if limitador % limite == 0:  # A cada 'limite' mensagens enviadas, pede confirmação
            resposta = messagebox.askyesno("Confirmação", f"{limite} mensagens enviadas, deseja continuar?")
            if not resposta:
                print("Usuário optou por parar o envio.")
                return
            
    popUp("Mensagens enviadas com sucesso.")  