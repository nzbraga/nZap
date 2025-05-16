import time
import psutil   
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from assets.func.sessao_whatsapp.uteis.definir_pasta import definir_pasta
from assets.func.uteis.popUp import popUp

driver = None
options = None

base_dir = Path.home() / "nZap"
base_dir.mkdir(parents=True, exist_ok=True)

sucesso_arquivo = base_dir / "sucesso.txt"
erro_arquivo = base_dir / "erro.txt"

def encerrar_chrome_existente(client):
    caminho_perfil = definir_pasta(client)

    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['name'] == 'chrome' or proc.info['name'] == 'chrome.exe':
                cmdline = " ".join(proc.info['cmdline'])
                if '--user-data-dir=' in cmdline and str(caminho_perfil) in cmdline:
                    print(f"Encerrando processo Chrome PID {proc.pid} com perfil: {caminho_perfil}")
                    proc.terminate()
                    proc.wait(timeout=5)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

def config_webdriver(headless, client):
    global driver, options

    if driver is not None:
        driver.quit

    encerrar_chrome_existente(client)
   

    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    if headless:
        options.add_argument("--headless=new")  # Usa um modo mais estável do headless
    options.add_argument("--disable-gpu")  # Corrige problemas gráficos em headless
    options.add_argument("--no-sandbox")  # Evita problemas de permissões
    options.add_argument("--no-first-run")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")  # Evita uso excessivo de memória compartilhada
    options.add_argument(f"user-data-dir={definir_pasta(client)}")

    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com")

    
def desconectar_whatsapp():
    global driver

    elemento = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//span[@data-icon="settings-outline"]'))
    )

    if elemento:
        #print("Elemento encontrado:", elemento)
        elemento.click()
        desconectar = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//span[@data-icon="exit"]'))
        )
        desconectar.click()
        confirme_desconectar = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "x1c4vz4f") and contains(text(), "Desconectar")]'))
        )
        confirme_desconectar.click()
    else:
        print("Elemento NÃO encontrado:", elemento)

def check_login(existe_login=False):
    global driver
    try:
        if existe_login:
            #print('checando login com pasta')
            logado = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
            )
            return bool(logado)
        else:
            #print('checando QR sem pasta')
            qr_code = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "//canvas[@aria-label='Scan this QR code to link a device!']"))
            )
            #print("QR Code encontrado:", qr_code)
            return False
        
    except:
        #print('checando login sem pasta')
        try:
            logado = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
            )
            return bool(logado)
        except:
            #print("Erro ao checar login")
            return False

def obter_dados_usuario():
    global driver
    
    botao_perfil = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Perfil"]'))
    )
    # Clicar no botão
    botao_perfil.click()

    #CAMPO NOME
    time.sleep(3)
    nome_perfil = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/div/span/div/div/div[2]/div[1]/div[1]/div[2]'))
    )
    

    nome = nome_perfil.text
    
    # voltar pra conversas
    conversas_button = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div/header/div/div[1]/div/div[1]/button/div/div/div/span'))
    )

    # Clicar ou fazer outra ação
    conversas_button.click()
    
    return nome    

def enviar_mensagem(numero, mensagem):
    global driver
    
    from assets.func.sessao_whatsapp.iniciar_api.iniciar_api import whatsapp_api

    if whatsapp_api.api_logada:
        try:

            #print(f"enviar_mensagem >>> numero: {numero}")
            
            # Busca pelo contato ou número
            search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div/div/div[1]')
            search_box.click()     
            search_box.send_keys(Keys.CONTROL + "a")
            search_box.send_keys(Keys.BACKSPACE)

            search_box.send_keys(str(numero) + Keys.ENTER)
            time.sleep(2)  # Aguarda a tela do contato carregar

            try:
                # Digita e envia a mensagem
                msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
                msg_box.click()
                msg_box.send_keys(mensagem + Keys.ENTER)
                time.sleep(3)   
            except:
                #print("Erro ao enviar mensagem\n erro: NÃO ENCONTRADO")
                search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div/div/div[1]')
                search_box.click()     
                search_box.send_keys(Keys.CONTROL + "a")
                search_box.send_keys(Keys.BACKSPACE)

                search_box.send_keys(str('2137055362') + Keys.ENTER)
                time.sleep(2)  # Aguarda a tela do contato carregar

                msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
                msg_box.click()
                msg_box.send_keys(Keys.CONTROL + "a")
                msg_box.send_keys(Keys.BACKSPACE)
                msg_box.send_keys(f"Numero nao encontrado {numero}" + Keys.ENTER)
                time.sleep(3)  
            #search_box.clear()
                
            """
            with sucesso_arquivo.open("a", encoding="utf-8") as f:
                f.write(f"Sucesso: {numero}\n")
            """
        except Exception as e:
            """
            with erro_arquivo.open("a", encoding="utf-8") as f:
                f.write(f"Erro: {numero}\n")
            """
            print("Erro ao enviar mensagem\n erro:", e)
    else:
        raise popUp("Whatsapp não está Conectado!")

