import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import driver

#from assets.func.sessao_whatsapp.uteis.definir_pasta import sucesso_arquivo, erro_arquivo
from assets.func.uteis.popUp import popUp

def enviar_mensagem(numero, mensagem):
    global driver
    
    from assets.func.sessao_whatsapp.iniciar_api.iniciar_api import whatsapp_api

    if whatsapp_api.api_logada:
        try:

            print(f"Enviando mensagem para: {numero}")

            
            # Busca pelo contato ou número
            search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
            search_box.click()
            search_box.clear()
            search_box.send_keys(str(numero) + Keys.ENTER)
            time.sleep(2)  # Aguarda a tela do contato carregar

            # Digita e envia a mensagem
            msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
            msg_box.click()
            msg_box.send_keys(mensagem + Keys.ENTER)
            time.sleep(3)

            """
            
            with sucesso_arquivo.open("a", encoding="utf-8") as f:
                f.write(f"Sucesso: {numero}\n")
            """
        except:
            """
            with erro_arquivo.open("a", encoding="utf-8") as f:
                f.write(f"Erro: {numero}\n")
            """
            print("Erro ao enviar mensagem")
    else:
        raise popUp("Whatsapp não está Conectado!")
