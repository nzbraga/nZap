import re
import time
from datetime import datetime
from tkinter import messagebox

from assets.func.uteis.popUp import popUp
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import enviar_mensagem
from assets.func.mensagem.montar_msg.formatar_mensagem import substituir_variaveis, formatar_valor

limitador = 0

def enviar_msg(contatos, mensagem, frequencia="hoje",  chave_destinatario='contato', limite=5):
    global limitador
    #print(f'contatosssss: {contatos}')
   
    data_atual = datetime.now().strftime("%d/%m")
    data_envio = None

    if frequencia == 'hoje':
        data_envio = data_atual

    if not contatos:
        popUp("Nenhum contato selecionado.")
        return

    if not mensagem or not mensagem.strip():
        popUp("Mensagem vazia.")
        return
  
      
    for contato in contatos:

        #print(f'Chaves disponíveis: {contato.keys()}')
        #print(f'Chaves disponíveis: >>> {contato.get(chave_destinatario)}')
        
        if not contato.get(chave_destinatario):  # Verifica se a chave nao existe ou esta vazia
            popUp(f"Contato nao encontrado para: {contato.get('nome')}.\nConfirme se o campo '{chave_destinatario}' existe no arquivo Excel.")
            continue
        
        mensagem_personalizada = substituir_variaveis(mensagem, contato)
           
        if mensagem_personalizada is None:
            popUp(f"Erro ao processar mensagem para {contato.get('nome', 'Desconhecido')}.")
            return  # Interrompe a execução se houver erro
        
        
        mensagem_completa = f"{mensagem_personalizada}"       
                          
        #print(f'enviar msg >> contato: {contato.get(chave_destinatario)}')
        #print(f'data de envio: {data_envio}\n data atual: {data_atual}')

        if data_envio == data_atual:
            enviar_mensagem(contato.get(chave_destinatario), mensagem_completa)
            
        time.sleep(2)
        
        limitador += 1
        if limitador % limite == 0:  # A cada 'limite' mensagens enviadas, pede confirmação
            resposta = messagebox.askyesno("Confirmação", f"{limite} mensagens enviadas, deseja continuar?")
            if not resposta:
                print("Usuário optou por parar o envio.")
                return

