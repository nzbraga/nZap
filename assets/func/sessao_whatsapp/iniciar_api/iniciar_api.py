import time
import threading

from assets.func.uteis.popUp import popUp
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import config_webdriver, check_login
loged = False

def start_whatsapp(client):
    global loged
    
    stop_event = threading.Event()
    
    config_webdriver(True, client)

    time.sleep(10)
    loged = check_login() 
    print(f'loged: {loged}')

    if loged:       
        stop_event.set()  # Adicionei essa linha para parar a thread de progresso
      
        popUp('Logado com sucesso!')
        
    else:
        config_webdriver(False, client)
        popUp('Despois de logado, precione OK!')   
        loged = check_login() 
        print(f'loged: {loged}')
