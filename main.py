from Funcoes.Login.loginLinkedin import logarNoLinkedin
from Funcoes.Coleta.pesquisarLeads import PesquisaLeads
from Funcoes.Coleta.coletarLeads import ColetaLead
import time

#Input dados
email = input("Seu email: ")
senha = input("Sua senha: ")

#Input da pesquisa
cargo = input("Digite o cargo que deseja procurar: ")
estado = input("Digite o estado que deseja procurar: ")
setor = input("Digite o setor que deseja procurar: ")

mensagem = input("Digite a mensagem que deseja enviar para os leads: ")

logarNoLinkedin(email, senha)
time.sleep(8)
PesquisaLeads(cargo, estado, setor)
time.sleep(6)
ColetaLead(mensagem)