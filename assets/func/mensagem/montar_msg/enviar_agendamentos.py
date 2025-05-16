import time
from datetime import datetime
from tkinter import messagebox

from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import enviar_mensagem
from assets.func.mensagem.montar_msg.formatar_mensagem import substituir_variaveis
from assets.func.uteis.popUp import popUp

limitador = 0

def enviar_agendamentos(contato, mensagem, frequencia, data , limite=5):
    global limitador
    #print(f'contatosssss: {contato}')
   
    data_atual = datetime.now().strftime("%d/%m")

    if frequencia == 'hoje':
        frequencia = data_atual

    if not contato:
        popUp("Nenhum contato selecionado.")
        return

    if not mensagem or not mensagem.strip():
        popUp("Mensagem vazia.")
        return
    
    mensagem_personalizada = substituir_variaveis(mensagem, contato)
        
    if mensagem_personalizada is None:
        popUp(f"Erro ao processar mensagem para {contato.get('nome', 'Desconhecido')}.")
        return  # Interrompe a execução se houver erro
        
    mensagem_completa = f"{mensagem_personalizada}"
    
    if frequencia == 'Aniversario':        
        
        if data == data_atual:  
                        
            print(f'enviar msg >> contato: {contato}\n mensagem: {mensagem_completa}')
            
            enviar_mensagem(contato, mensagem_completa)                    
            time.sleep(2)
            
            limitador += 1
            if limitador % limite == 0:  # A cada 'limite' mensagens enviadas, pede confirmação
                resposta = messagebox.askyesno("Confirmação", f"{limite} mensagens enviadas, deseja continuar?")
                if not resposta:
                    print("Usuário optou por parar o envio.")
                    return
