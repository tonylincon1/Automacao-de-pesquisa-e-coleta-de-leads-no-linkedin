from Funcoes.Login.loginLinkedin import navegador
import time


def ColetaLead (mensagem):
    total_contatos = navegador.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[2]/div/div[1]/main/div/div/div[1]').text.split()[0]
    
    print(total_contatos)
    
    quantidade_atual_de_envios = 0
    
    while total_contatos != quantidade_atual_de_envios:
        
        convite1 = navegador.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[2]/div/div[1]/main/div/div/div[2]/ul/li[1]/div/div/div[3]/button/span')
        if convite1.text != "Pendente" and convite1.text != "Seguir":
            convite1.click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]').click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').click()
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').send_keys(mensagem)
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
            time.sleep(2)
            
        convite2 = navegador.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[2]/div/div[1]/main/div/div/div[2]/ul/li[2]/div/div/div[3]/button/span')
        if convite2.text != "Pendente" and convite2.text != "Seguir":
            convite2.click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]').click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').click()
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').send_keys(mensagem)
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
            time.sleep(2)
            
        convite3 = navegador.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[2]/div/div[1]/main/div/div/div[2]/ul/li[3]/div/div/div[3]/button/span')
        if convite3.text != "Pendente" and convite3.text != "Seguir":
            convite3.click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]').click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').click()
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').send_keys(mensagem)
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
            time.sleep(2)
            
        convite4 = navegador.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[2]/div/div[1]/main/div/div/div[2]/ul/li[4]/div/div/div[3]/button/span')
        if convite4.text != "Pendente" and convite4.text != "Seguir":
            convite4.click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]').click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').click()
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').send_keys(mensagem)
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
            time.sleep(2)
            
        convite5 = navegador.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[2]/div/div[1]/main/div/div/div[2]/ul/li[5]/div/div/div[3]/button/span')
        if convite5.text != "Pendente" and convite5.text != "Seguir":
            convite5.click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]').click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').click()
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').send_keys(mensagem)
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
            time.sleep(2)
            
        convite6 = navegador.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[2]/div/div[1]/main/div/div/div[2]/ul/li[6]/div/div/div[3]/button/span')
        if convite6.text != "Pendente" and convite6.text != "Seguir":
            convite6.click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]').click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').click()
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').send_keys(mensagem)
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
            time.sleep(2)
            
        convite7 = navegador.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[2]/div/div[1]/main/div/div/div[2]/ul/li[7]/div/div/div[3]/button/span')
        if convite7.text != "Pendente" and convite7.text != "Seguir":
            convite7.click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]').click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').click()
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').send_keys(mensagem)
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
            time.sleep(2)
            
        convite8 = navegador.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[2]/div/div[1]/main/div/div/div[2]/ul/li[8]/div/div/div[3]/div/button/span')
        if convite8.text != "Pendente" and convite8.text != "Seguir":
            convite8.click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]').click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').click()
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').send_keys(mensagem)
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
            time.sleep(2)
            
        convite9 = navegador.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[2]/div/div[1]/main/div/div/div[2]/ul/li[9]/div/div/div[3]/button/span')
        if convite9.text != "Pendente" and convite9.text != "Seguir":
            convite9.click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]').click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').click()
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').send_keys(mensagem)
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
            time.sleep(2)
            
        convite10 = navegador.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[2]/div/div[1]/main/div/div/div[2]/ul/li[10]/div/div/div[3]/button/span')
        if convite10.text != "Pendente" and convite10.text != "Seguir":
            convite10.click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[1]').click()
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').click()
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/textarea').send_keys(mensagem)
            time.sleep(2)
            navegador.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
            time.sleep(2)
            
        quantidade_atual_de_envios = quantidade_atual_de_envios + 10
        navegador.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[2]/div/div[1]/main/div/div/div[5]/div/div/button[2]/span').click()
        
        time.sleep(5)
    
    
    
    