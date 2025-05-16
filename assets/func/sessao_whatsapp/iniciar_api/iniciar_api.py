import os
import threading
from pathlib import Path

from assets.func.uteis.popUp import popUp
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import config_webdriver, check_login

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
            
            if self.atualizar_interface_callback:
                self.atualizar_interface_callback()  # Atualiza a UI

whatsapp_api = WhatsAppAPI()

def start_whatsapp(client, visivel=True):
 
    
    def login_whatsapp():
        global existe_login        

        caminho = Path.home() / f".whatsapp_automation_profile_{client}"

        existe_login = os.path.isdir(caminho)
        
        # verifica se a pasta de login existe
        if existe_login:
            
            
            config_webdriver(visivel, client) #headless true
            whatsapp_api.api_logada = check_login(True)            
            
            # se nao estiver logado abre a janela visivel
            if not whatsapp_api.api_logada:                
                
                config_webdriver(visivel, client) #headless false
                #popUp('Após conectar o WhatsApp, pressione OK') 
                config_webdriver(visivel, client) #headless true       
                whatsapp_api.api_logada = check_login(True)            
                    
                # quando estiver logado fecha a janela e abre janela invisivel
                if whatsapp_api.api_logada:                    
                        
                    popUp("WhatsApp iniciado")                
                    return True
                else:                    
                    popUp("Erro ao logar WhatsApp")                
                    return False
        # se nao tiver a pasta de login cria e abre a janela visivel para ler qr code            
        else:
            config_webdriver(visivel, client)  #headless false
            popUp('Após conectar o WhatsApp, pressione OK')  
            config_webdriver(visivel, client)      #headless true  
            whatsapp_api.api_logada = check_login(True)            

            if whatsapp_api.api_logada:
                
                popUp("WhatsApp iniciado")
                return True
            else:                    
                    popUp("Erro ao logar WhatsApp")                
                    return False
        
        
    threading.Thread(target=login_whatsapp, daemon=True).start()

