from datetime import datetime as dt2
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

class Navegador:

    def __init__(self,url):
        self.service = ChromeService()
        self.options = Options()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(service=self.service,options=self.options)
        self.web = url
        self.ingresar_url(self.web)

    def ingresar_url(self,url):
        self.web = url
        self.driver.get(url)

    def buscar_elemento(self,xpath):
        return self.driver.find_element('xpath',xpath)
    
    def ingresar_objeto_en_elemento(self,objeto,elemento):
        return elemento.send_keys(objeto)
    
    def click_objeto(self,xpath):
        self.driver.buscar_elemento(xpath).click()
    
    def presionar_enter(self,elemento):
        return elemento.send_keys(Keys.ENTER)

