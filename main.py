from os import system #para limpar a tela
from pickle import dump, load #para salvar os dados
from colorama import Fore, init #para estetica do terminal
from time import sleep

init(convert=True , autoreset=True) #inicializa o colorama (modulo estetica)

def limpar():
    system("cls")

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
    
#Faz o usuario logar
def fazer_login():
    while True:
        limpar()
        login = str(input("""
           Fazer Login
───────────────────────────────────

  Login: """))
        if login in cadastrados: #Se o user estiver no dicionário ele irá permitir a entrada da senha
            limpar()
            senha = str(input(f"""
           Fazer Login
───────────────────────────────────

  Login: {login}
  Senha: """)) 
            if senha == cadastrados[f'{login}']: #Se a senha atribuida pelo usuario for a mesma pertencente ele será logado
                limpar()
                print("Logado com sucesso!")
                sleep(3)
            else:
                limpar()
                print("Senha incorreta!")
                sleep(2.5)
                break
        else:
            limpar()
            print("Usuário não cadastrado")   
            sleep(3)
            break                            
            

def cadastrar_user():
    pass
# com a base de dados preparada é só criar toda a logica por trás
# quando voltar dê uma lida no código para refrescar 
# tente criar uma interface 
# tente fazer algo bonitinho
'''
- Fazer Cadastro
- Verificar Cadastro
- Fazer Login
- Remover login
'''

#Checa e salva todos os dados na base de dados
check_database()

#loop principal
while True:
    limpar()
    print("""
         Entrar no sistema
───────────────────────────────────

1 ────► Fazer Login

2 ────► Cadastrar-se

3 ────► Sair
          
""")
    var = str(input("───► "))
    if var == "1":
        fazer_login()
    elif var == "2":
        cadastrar_user()  
    elif var == "3":
        break
    

