import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from assets.func.sessao_whatsapp.uteis.definir_pasta import definir_pasta

driver = None


def config_webdriver(headless, client):
   
    global driver
    
    if driver:
        driver.quit()

    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    if headless:
        options.add_argument("--headless=new")  # Usa um modo mais estavel do headless
    options.add_argument("--disable-gpu")  # Corrige problemas graficos em headless
    options.add_argument("--no-sandbox")  # Evita problemas de permissões
    options.add_argument("--disable-dev-shm-usage")  # Evita uso excessivo de memória compartilhada
    options.add_argument(f"user-data-dir={definir_pasta(client)}")

    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com")

    time.sleep(5)

def check_login():
   
    if WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, '//div[@data-ref]//canvas'))
    ):
        return False
    
    elif WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="side"]'))
    ):
        return True


def send_message(number, message):
    
    # Busca pelo contato ou número
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.click()
    search_box.clear()
    search_box.send_keys(number + Keys.ENTER)
    time.sleep(2)  # Aguarda a tela do contato carregar

    # Digita e envia a message
    msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    msg_box.click()
    msg_box.send_keys(message + Keys.ENTER)
    #print(f"Mensagem enviada para {name}")
    time.sleep(5)
