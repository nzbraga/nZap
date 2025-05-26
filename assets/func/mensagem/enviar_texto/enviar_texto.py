from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def enviar_texto(mensagem, driver):
    msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    msg_box.click()
    msg_box.send_keys(mensagem + Keys.ENTER)
 