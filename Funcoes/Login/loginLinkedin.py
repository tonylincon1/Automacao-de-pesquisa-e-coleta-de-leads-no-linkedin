from selenium import webdriver
import time

#Instanciando webdriver
navegador = webdriver.Chrome()
time.sleep(2)

def logarNoLinkedin (email, senha):
    
    #Acessando navegador
    navegador.get("https://www.linkedin.com/")

    #Login
    navegador.find_element_by_xpath('/html/body/nav/div/a[2]').click()
    time.sleep(2)
    navegador.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[1]/input').send_keys(email)
    time.sleep(2)
    navegador.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[2]/input').send_keys(senha)
    time.sleep(1)
    navegador.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[3]/button').click()

    navegador.get("https://www.linkedin.com/")