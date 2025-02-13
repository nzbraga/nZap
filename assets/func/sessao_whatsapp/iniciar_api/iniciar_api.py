import time
import os

from assets.func.uteis.popUp import popUp
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import config_webdriver, check_login, navegador_aberto
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
                self.atualizar_interface_callback()  # Chama a atualização da UI

    def acao_quando_muda(self):
        if self._api_logada:
            print("A API foi conectada!")
            popUp("A API foi conectada!")
        else:
            print("A API foi desconectada!")
            popUp("A API foi desconectada!")

# Criar uma instância global para ser usada em toda a aplicação
whatsapp_api = WhatsAppAPI()


usuario_id = sessao_id()




import time

def start_whatsapp(client):
    global existe_login, navegador_aberto

    #print(f"navegador_aberto: {navegador_aberto}")
    caminho = f"C:/Users/Jato Gravações/.whatsapp_automation_profile_{usuario_id}"

    existe_login = os.path.isdir(caminho)
    #print(f"caminho: {caminho}")
    #print(f"Existe login: {existe_login}")

    if existe_login:
        # se a pasta de login existe abre navegador invisivel
       
        config_webdriver(True, client)
        
        whatsapp_api.api_logada = check_login(True)  # Usa o setter da classe

        # se nao estiver logado, fecha a janela invisivel e abre uma visivel pra logar usando qr code
        if not WhatsAppAPI.api_logada:
            config_webdriver(False, client)
            
            whatsapp_api.api_logada = check_login(False)  # Usa o setter da classe

            if WhatsAppAPI.api_logada:
                config_webdriver(True, client)
                
                whatsapp_api.api_logada = check_login(True)  # Usa o setter da classe

                if WhatsAppAPI.api_logada: 
                    popUp("Whatsapp iniciado")
                    return True
                else:
                    popUp("Erro ao logar Whatsapp")
                    return False
       
    else:
        # se a pasta nao existe abre uma visivel pra logar usando qr code
        config_webdriver(False, client)
        popUp('Após conectar o whatsapp, pressione OK') 
        
        whatsapp_api.api_logada = check_login(False)  # Usa o setter da classe

        if WhatsAppAPI.api_logada:
            config_webdriver(True, client)
            
            whatsapp_api.api_logada = check_login(True)  # Usa o setter da classe

            if WhatsAppAPI.api_logada:
                popUp("Whatsapp iniciado")
                return True
        
           



