import re
import time
from datetime import datetime
from tkinter import messagebox

from assets.func.uteis.popUp import popUp
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import enviar_mensagem
from assets.func.mensagem.montar_msg.formatar_mensagem import substituir_variaveis, formatar_valor

limitador = 0

def enviar_msg(contatos, mensagem, frequencia="hoje",  destinatario= 'contato', limite=5):
    global limitador
    #print(f'contatosssss: {contatos}')
   
    data_atual = datetime.now().strftime("%d/%m")

    if frequencia == 'hoje':
        frequencia = data_atual

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
        print(f'contato: {contato.get(destinatario)}')
        if not contato.get(destinatario):  # Verifica se a chave não existe ou está vazia
            popUp(f"Contato não encontrado.\nConfirme se o campo '{destinatario}' existe no arquivo Excel.")
        
        mensagem_completa = f"{mensagem_personalizada}"
        
        if frequencia == 'Aniversario':
            
            if formatar_valor(contato,'aniversario') == data_atual:            
                
                enviar_mensagem(contato[destinatario], mensagem_completa)                    
                time.sleep(2)
                
                limitador += 1
                if limitador % limite == 0:  # A cada 'limite' mensagens enviadas, pede confirmação
                    resposta = messagebox.askyesno("Confirmação", f"{limite} mensagens enviadas, deseja continuar?")
                    if not resposta:
                        print("Usuário optou por parar o envio.")
                        return
