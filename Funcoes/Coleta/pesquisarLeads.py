from Funcoes.Login.loginLinkedin import navegador
from selenium.webdriver.common.keys import Keys
import pyautogui
import time

def PesquisaLeads (cargo, estado, setor):
    pesquisa = navegador.find_element_by_xpath('/html/body/div[5]/header/div/div/div/div[1]/input').send_keys(cargo, Keys.ENTER)
    time.sleep(4)

    navegador.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[2]/section/div/nav/div/div/div/button').click()
    time.sleep(3)
    filtro = navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/h2/span/div/button')
    filtro.click()
    time.sleep(1)
    pyautogui.press("down")
    pyautogui.press("enter")
    time.sleep(2)
    
    navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/ul/li[1]/fieldset/div/ul/li[2]/label').click() 
    navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/ul/li[1]/fieldset/div/ul/li[3]/label').click() 
    
    localidade = navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[6]/button')
    localidade.click() 
    time.sleep(2)
    escrever_localidade = navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[6]/div/div/input')
    escrever_localidade.send_keys(estado)
    time.sleep(2)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("enter")
    
    area = navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/ul/li[7]/fieldset/div/ul/li[6]/button')
    area.click() 
    time.sleep(2)
    escrever_area = navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/ul/li[7]/fieldset/div/ul/li[6]/div/div/input')
    escrever_area.send_keys(setor)
    time.sleep(2)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("enter")
    
    navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/div/button[2]').click() 