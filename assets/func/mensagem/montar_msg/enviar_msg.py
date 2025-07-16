import re
import time
from datetime import datetime

from assets.func.uteis.popUp import popUp
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import enviar_mensagem
from assets.func.mensagem.montar_msg.formatar_mensagem import substituir_variaveis
from assets.func.mensagem.saudacao.saudacao import definir_saudacao


def enviar_msg(contatos, mensagem, frequencia="hoje"):
    #print(f'contatosssss: {contatos}')
   
    data_atual = datetime.now().strftime("%d-%m")
    data_envio = None



    if not contatos:
        popUp("Nenhum contato selecionado.")
        return

    if not mensagem or not mensagem.strip():
        popUp("Mensagem vazia.")
        return
  
      
    for contato in contatos:

        print(f'Chaves --- disponíveis: {contato[frequencia]}')
        #print(f'Chaves disponíveis: >>> {contato.get(chave_destinatario)}')
                     
        mensagem_personalizada = substituir_variaveis(mensagem, contato)
        
           
        if mensagem_personalizada is None:
            popUp(f"Erro ao processar mensagem para {contato.get('nome', 'Desconhecido')}.")
            return  # Interrompe a execução se houver erro
        
        
        mensagem_completa = f"{definir_saudacao(contato.get('nome'))}{mensagem_personalizada}"       
                          

        if frequencia == 'hoje':
            data_envio = data_atual
        else:
            data_envio = contato[frequencia]
    
        print(f'data de envio: {data_envio}\n data atual: {data_atual}')

        if data_envio == data_atual:
            #print(f'enviar msg >> contato: {contato}\n mensagem: {mensagem_completa}')
            enviar_mensagem(contato['nome'], contato['contato'], mensagem_completa)
            
        time.sleep(1)
      
