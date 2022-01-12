from Funcoes.Login.loginLinkedin import logarNoLinkedin
from Funcoes.Coleta.pesquisarLeads import PesquisaLeads
from Funcoes.Coleta.coletarLeads import ColetaLead
import time

#Input dados
email = ""
senha = ""

#email = input("Seu email: ")
#senha = input("Sua senha: ")
#time.sleep(2)

logarNoLinkedin(email, senha)

cargo = "Processos"
estado = "Sergipe"
setor = "Processos"

#Input da pesquisa
#cargo = input("Digite o cargo que deseja procurar: ")
#estado = input("Digite o estado que deseja procurar: ")
#setor = input("Digite o setor que deseja procurar: ")
#time.sleep(2)

PesquisaLeads(cargo, estado, setor)

time.sleep(6)

mensagem = "Olá, tudo bem? Meu nome é Antônio, sou um entusiasta da área de Processos, adoraria te ter em minha rede para gente trocar esse papo"

ColetaLead(mensagem)