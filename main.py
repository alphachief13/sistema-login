from os import system #para limpar a tela
from pickle import dump, load #para salvar os dados
from colorama import Fore, init #para estetica do terminal
from time import sleep

init(convert=True , autoreset=True) #inicializa o colorama (modulo estetica)





def limpar():
    system("cls")

#Checa a base de dados
def check_database():
    global cadastrados, user_status, user_atual
    #caso já possua o arquivo de cadastrados
    try:
        arquivo_login = open("cadastrados.pck", "rb")
        cadastrados = load(arquivo_login)
        arquivo_login.close()
    #caso não possua o arquivo de cadastrados
    except:
        arquivo_login = open("cadastrados.pck", "wb")
        cadastrados = {
            'Admin' : '123',
            'user_status' : Fore.LIGHTRED_EX + 'Não logado'
        }
        dump(cadastrados, arquivo_login)
        arquivo_login.close()
        user_atual = '[VAZIO]'
        

#Modifica/adiciona os dados na base de dados
def mod_database(key, value):
    global cadastrados
    arquivo_login = open("cadastrados.pck", "wb")
    cadastrados[key] = value
    dump(cadastrados, arquivo_login)
    arquivo_login.close()
    
#Apaga itens da base de dados
def delete_data(key):
    global cadastrados
    arquivo_login = open("cadastrados.pck" , "wb")
    del cadastrados[f'{key}']
    dump(cadastrados, arquivo_login)
    arquivo_login.close()
    
def menu_logados():
    print("""

""")
    
#Faz o usuario logar
def fazer_login():
    global user_atual
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
                user_atual = login
                mod_database('user_status' , Fore.LIGHTGREEN_EX + f'Logado como: {user_atual}')
                sleep(3)
                break
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
    while True:
        limpar()
        username = str(input("""
          Cadastrar user
───────────────────────────────────

  Username: """))
        if username not in cadastrados:
            while True:   
                limpar()
                senha = str(input(f"""
          Cadastrar user
───────────────────────────────────

  Username: {username}
  Senha: """))
                if len(senha) < 3 or senha == '   ':
                    limpar()
                    print("Digite uma senha com mais caracteres!")
                    sleep(2)
                else:
                    limpar()
                    mod_database(username, senha)
                    print("Usúario cadastrado com sucesso!!")
                    sleep(2)
                    break
            break
        else:
            limpar()
            print("Usuário já possui cadastro!!")
            sleep(3)

#Checa e salva todos os dados na base de dados
check_database()

#loop principal
while True:
    limpar()
    print(f"""
{cadastrados['user_status']}""" + Fore.LIGHTWHITE_EX +"""        

        Entrar no sistema
───────────────────────────────────

    1 ────► Fazer Login

    2 ────► Cadastrar-se

    3 ────► Sair

    0 ────► Fechar aplicação


""")
    var = str(input("───► "))
    if var == "1":
        fazer_login()
    elif var == "2":
        cadastrar_user() 
    elif var == "3":
        if user_atual != "[VAZIO]":
            mod_database('user_status' , Fore.LIGHTRED_EX + 'Não logado')
            user_atual = "[VAZIO]"
        else:
            limpar()
            print("Impossível sair agora, o usuário não possui login!")
            sleep(3)
        
    elif var == "0":
        break
    

#agora eu irei fazer uma função que irá permitir o usuario verificar as pessoas cadastradas.