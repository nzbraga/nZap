import time
import psutil   
from pathlib import Path
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from assets.func.sessao_whatsapp.uteis.definir_pasta import definir_pasta
from assets.func.mensagem.buscar_destinatario.buscar_destinatario import buscar_destinatario
from assets.func.mensagem.enviar_texto.enviar_texto import enviar_texto
from assets.func.uteis.popUp import popUp

driver = None
options = None
nome = None
remetente = None

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
    
    numero_perfil = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/div/span/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]'))
    )
    

    nome = nome_perfil.text
    # Remove tudo que não for dígito
    numero = re.sub(r'\D', '', numero_perfil.text) 
    #remove o +55 caso esteja no início:
    numero = re.sub(r'^55', '', numero)
    #print(f'nome: {nome}, numero: {numero}')
    
    # voltar pra conversas
    conversas_button = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div/header/div/div[1]/div/div[1]/button/div/div/div/span'))
    )


    # Clicar ou fazer outra ação
    conversas_button.click()
    
    return nome,numero    

def enviar_mensagem(nome, numero, mensagem):
    global driver
    
    from assets.func.sessao_whatsapp.iniciar_api.iniciar_api import whatsapp_api

    if nome == "Agendamento: Processo concluído.":
        if whatsapp_api.api_logada:
            buscar_destinatario('21997633265', driver)
            time.sleep(2)  # Aguarda a tela do contato carregar
            enviar_texto(mensagem, driver)
        else:
            pass

    if whatsapp_api.api_logada:
        try:

            if nome == "Agendamento: Processo concluído.":
                pass
            else:

                #print(f"enviar_mensagem >>> numero: {numero}")
                buscar_destinatario(numero, driver)
                time.sleep(2)  # Aguarda a tela do contato carregar

                try:
                    enviar_texto(mensagem, driver)
                    # Digita e envia a mensagem
                    
                    buscar_destinatario('21997633265', driver)
                    time.sleep(2)  # Aguarda a tela do contato carregar
                    enviar_texto(f"Enviada com Sucesso para: {nome} - {numero}", driver)

                    #atualizar pagina aqui
                    time.sleep(2)  # Aguarda a tela do contato carregar
                    driver.refresh()
                    time.sleep(5)  # Aguarda a tela do contato carregar

                except:
                    buscar_destinatario('21997633265', driver)
        
                    time.sleep(2)  # Aguarda a tela do contato carregar
                    # Digita e envia a mensagem
                    enviar_texto(f"Numero nao encontrado: {nome} - {numero}", driver)
                    #atualizar pagina aqui
                    time.sleep(2)  # Aguarda a tela do contato carregar
                    driver.refresh()
                    time.sleep(5)  # Aguarda a tela do contato carregar


            
                    

        except Exception as e:
            print("Erro ao enviar mensagem\n erro:", e)
            mensagem_erro ="Erro ao enviar mensagem\n erro:", e

            buscar_destinatario('21997633265', driver)
    
            time.sleep(2)  # Aguarda a tela do contato carregar
            # Digita e envia a mensagem
            enviar_texto(mensagem_erro, driver)

            # voltar pra conversas

    else:
        raise popUp("Whatsapp não está Conectado!")





