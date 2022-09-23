from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Instanciando webdriver
navegador = webdriver.Chrome()
time.sleep(2)

def logarNoLinkedin (email, senha):
    
    #Acessando navegador
    navegador.get("https://www.linkedin.com/")
    time.sleep(3)
    
    #Login
    navegador.find_element(By.XPATH,'/html/body/main/section[1]/div/div/form/div[2]/div[1]/input').send_keys(email)
    time.sleep(2)
    navegador.find_element(By.XPATH,'/html/body/main/section[1]/div/div/form/div[2]/div[2]/input').send_keys(senha)
    time.sleep(1)
    navegador.find_element(By.XPATH,'/html/body/main/section[1]/div/div/form/button').click()

    navegador.get("https://www.linkedin.com/")