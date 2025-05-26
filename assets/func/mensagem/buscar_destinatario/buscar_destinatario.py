import time
import psutil   
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def buscar_destinatario(numero, driver):
    search_box = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div/div/div[1]')
    search_box.click()     
    search_box.send_keys(Keys.CONTROL + "a")
    search_box.send_keys(Keys.BACKSPACE)

    search_box.send_keys(str(numero) + Keys.ENTER)

    