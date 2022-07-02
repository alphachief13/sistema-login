from os import system #para limpar a tela
from pickle import dump, load #para salvar os dados
from colorama import Fore, init #para estetica do terminal

init(convert=True , autoreset=True) #inicializa o colorama (modulo estetica)

#Checa a base de dados
def check_database():
    global cadastrados
    #caso já possua o arquivo de cadastrados
    try:
        arquivo_login = open("data/cadastrados.pck", "rb")
        cadastrados = load(arquivo_login)
        arquivo_login.close()
    #caso não possua o arquivo de cadastrados
    except:
        arquivo_login = open("data/cadastrados.pck", "wb")
        cadastrados = {
            'Admin' : '123'
        }
        dump(cadastrados, arquivo_login)
        arquivo_login.close()

#Modifica/adiciona os dados na base de dados
def mod_database(key, value):
    global cadastrados
    arquivo_login = open("data/cadastrados.pck", "wb")
    cadastrados[key] = value
    dump(cadastrados, arquivo_login)
    arquivo_login.close()
    
#Apaga itens da base de dados
def delete_data(key):
    global cadastrados
    arquivo_login = open("data/cadastrados.pck" , "wb")
    del cadastrados[f'{key}']
    dump(cadastrados, arquivo_login)
    arquivo_login.close()
    

    
    
    

