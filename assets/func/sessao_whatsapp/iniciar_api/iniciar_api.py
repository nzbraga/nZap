import threading
import os
import tkinter as tk
from assets.func.uteis.popUp import popUp_bar, popUp
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import config_webdriver, check_login
from assets.func.sessao.sessao import sessao_id

class WhatsAppAPI:
    def __init__(self):
        self._api_logada = False
        self.atualizar_interface_callback = None  # Callback para atualizar a UI

    @property
    def api_logada(self):
        return self._api_logada

    @api_logada.setter
    def api_logada(self, novo_valor):
        if self._api_logada != novo_valor:
            self._api_logada = novo_valor
            print(f"API mudou para: {'Conectado' if novo_valor else 'Desconectado'}")
            if self.atualizar_interface_callback:
                self.atualizar_interface_callback()  # Atualiza a UI

whatsapp_api = WhatsAppAPI()
usuario_id = sessao_id()

def start_whatsapp(client):
    """ Inicia o WhatsApp e exibe um pop-up de carregamento. """
    
    popUp_janela = popUp_bar("Iniciando login no WhatsApp...")

    def login_whatsapp():
        global existe_login

        caminho = f"C:/Users/Jato Gravações/.whatsapp_automation_profile_{usuario_id}"
        existe_login = os.path.isdir(caminho)
        
        # verifica se a pasta de login existe
        if existe_login:
            
            config_webdriver(True, client)
            whatsapp_api.api_logada = check_login(True)
            
            
            # se nao estiver logado abre a janela visivel
            if not whatsapp_api.api_logada:
                
                config_webdriver(False, client)
                whatsapp_api.api_logada = check_login(False)
                # quando estiver logado fecha a janela e abre janela invisivel
                if whatsapp_api.api_logada:
                    config_webdriver(True, client)
                    whatsapp_api.api_logada = check_login(True)
                    # confira janela aberta e finaliza
                    if whatsapp_api.api_logada:
                        print("DEVERIA FECHAR!!!!!!!!!!!!!!!!!!")
                        popUp_janela.after(100, popUp_janela.destroy)  # ✅ Fecha corretamente a UI
                        popUp("WhatsApp iniciado")                
                        return True
                    else:
                        print("DEVERIA FECHAR!!!!!!!!!!!!!!!!!!")
                        popUp_janela.after(100, popUp_janela.destroy)  # ✅ Fecha corretamente a UI
                        popUp("Erro ao logar WhatsApp")                
                        return False
        # se nao tiver a pasta de login cria e abre a janela visivel para ler qr code
            print("DEVERIA FECHAR!!!!!!!!!!!!!!!!!!")
            popUp_janela.after(100, popUp_janela.destroy)  # ✅ Fecha corretamente a UI
        else:
            config_webdriver(False, client)
            print("DEVERIA FECHAR!!!!!!!!!!!!!!!!!!")
            popUp_janela.after(100, popUp_janela.destroy)  # ✅ Fecha corretamente a UI
            popUp('Após conectar o WhatsApp, pressione OK')
            whatsapp_api.api_logada = check_login(False)

            if whatsapp_api.api_logada:
                config_webdriver(True, client)
                whatsapp_api.api_logada = check_login(True)

                if whatsapp_api.api_logada:
                    print("DEVERIA FECHAR!!!!!!!!!!!!!!!!!!")
                    popUp_janela.after(100, popUp_janela.destroy)  # ✅ Fecha corretamente a UI
                    popUp("WhatsApp iniciado")
                    return True

    threading.Thread(target=login_whatsapp, daemon=True).start()
