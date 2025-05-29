import threading
from assets.func.sessao_whatsapp.iniciar_api.iniciar_api import whatsapp_api
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import obter_dados_usuario
from assets.func.agendamento.checar_agendamento.checar_agendamento import checar_agendamentos, ARQUIVO_AGENDADO
from assets.func.agendamento.uteis.resetar_agendamentos import resetar_agendamentos

def atualizar_interface(status_label, info_label, botao_desconectar):
    """ Atualiza os elementos da interface com base no estado da API """
    if whatsapp_api.api_logada:
        nome_logado = obter_dados_usuario()

        status_label.config(text=f"WhatsApp Conectado como:\n{nome_logado}", fg="green")
        info_label.pack_forget()      
        botao_desconectar.pack(pady=5)

        # Inicia a thread de checagem de agendamentos após conectar ao WhatsApp
        thread = threading.Thread(target=checar_agendamentos, args=(ARQUIVO_AGENDADO,), daemon=True)
        thread.start()

        # Inicia a thread para rodar a função em segundo plano
        thread = threading.Thread(target=resetar_agendamentos, args=(ARQUIVO_AGENDADO,), daemon=True)
        thread.start()


    else:
        status_label.config(text="WhatsApp Desconectado! \n Aguarde...", fg="red")
        info_label.config(text="Conecte ao WhatsApp\npara enviar e agendar mensagens.")
        botao_desconectar.pack_forget()
     
