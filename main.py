from os import system #para limpar a tela
from pickle import dump, load #para salvar os dados
from colorama import Fore, init #para estetica do terminal
from time import sleep #para dar impressão de espera

init(convert=True , autoreset=True) #inicializa o colorama (modulo estetica)

#Limpa o terminal
def limpar():
    system("cls")

#Checa a base de dados
def check_database():
    global cadastrados, database
    #caso já possua o arquivo de cadastrados
    try:
        arquivo_login = open("cadastrados.pck", "rb")
        cadastrados = load(arquivo_login)
        arquivo_login.close()
        
        arquivo_database = open('database.pck' , 'rb')
        database = load(arquivo_database)
        arquivo_database.close()
        
    #caso não possua o arquivo de cadastrados
    except:
        arquivo_login = open("cadastrados.pck", "wb")
        cadastrados = {
            'Admin' : '123',
            
        }
        dump(cadastrados, arquivo_login)
        arquivo_login.close()
        
        arquivo_database = open('database.pck' , 'wb')
        database = {
            'status' : 'Não logado',
            'user_atual' : 'Nenhum!'
            
        }
        dump(database, arquivo_database)
        arquivo_database.close()
        
#Modifica/adiciona os dados na base de dados
def mod_database(key, value):
    global cadastrados
    arquivo_login = open("cadastrados.pck", "wb")
    cadastrados[key] = value
    dump(cadastrados, arquivo_login)
    arquivo_login.close()


#Modifica/adiciona os dados na base de dados
def mod_database2(key, value):
    global database
    arquivo_database = open("database.pck" , "wb")
    database[key] = value 
    dump(database, arquivo_database)
    arquivo_database.close()


#Apaga itens da base de dados
def delete_data(key):
    global cadastrados
    arquivo_login = open("cadastrados.pck" , "wb")
    del cadastrados[f'{key}']
    dump(cadastrados, arquivo_login)
    arquivo_login.close()
    
    
#Apaga itens da base de dados    
def delete_data2(key):
    global database 
    arquivo_database = open("database.pck" , "wb")
    del database[f'{key}']
    dump(database, arquivo_database)
    arquivo_database.close()


def deslogar():
    mod_database2('status' , 'Não logado')
    mod_database2('user_atual' , 'Nenhum!')

def aba_admin():
    while True:
        limpar()
        var = str(input(Fore.LIGHTWHITE_EX + '''
             Aba ADMIN  ( ͡° ͜ʖ ͡°)
┌──────────────────────────────────────────┐
│                                          │
│ 1  ───► Aba de admin                     │
│                                          │
│ 2 ────► Aba normal                       │
│                                          | 
│                                          | 
| 0 ────► Sair                             |
└──────────────────────────────────────────┘ 


────► '''))
        if var == "1":
            while True:
                limpar()
                print(Fore.LIGHTWHITE_EX + """
             Aba ADMIN  ( ͡° ͜ʖ ͡°)
┌──────────────────────────────────────────┐
│                                          │
│ 1  ───► Ver user e senhas                │
│                                          │
│ 0 ────► Sair                             │
│                                          │
└──────────────────────────────────────────┘ 


""")
                var = str(input("────► "))
                if var == "1":
                    limpar()
                    lista_user = list(cadastrados.keys())
                    lista_senha = list(cadastrados.values())
                    for i in range(len(lista_user)):
                        print(Fore.LIGHTYELLOW_EX + f'=============================\n\nUser: {lista_user[i]}\nSenha: {lista_senha[i]}\n')
                        sleep(0.1)
                    print(Fore.LIGHTYELLOW_EX + '=============================')
                    input('')
                elif var == "0":
                    break
        elif var == "2":
            menu_login()
        elif var == "0":
            break

#Menu 
def menu_login():
    loop_1 = True
    loop_senha_nova = True
    while True and loop_1 == True:
        if database['status'] != 'Não logado':
            while True and database['status'] != 'Não logado':
                limpar()
                print(Fore.LIGHTWHITE_EX + """
                       Menu
        ───────────────────────────────────

           1  ────► Ver pessoas cadastradas

           2  ────► Trocar senha do user atual

           3  ────► Remover um usuário 

           0  ────► Sair

        """)
                var = str(input("────► "))
                if var == "1":
                    limpar()
                    lista_cadastrados = list(cadastrados.keys())
                    for i in lista_cadastrados:
                        print("- ", f"'{i}'")
                        sleep(0.1)
                    input('')
                elif var == "2":
                    while True and loop_senha_nova == True:
                        limpar()
                        print("Você tem certeza que deseja trocar a senha?")
                        var = str(input("\n1 ───► Sim\n2 ───► Não\n\n───► "))
                        if var == '1':
                            limpar()
                            senha = str(input(Fore.LIGHTWHITE_EX + f"""
            Digite a senha atual
    ───────────────────────────────────

      Login: {database['user_atual']}
      Senha: """)) 
                            if senha == cadastrados[database['user_atual']]:
                                while True:
                                    limpar()
                                    senha_nova = str(input("Nova senha: "))
                                    if senha_nova == cadastrados[f'{database["user_atual"]}']:
                                        limpar()
                                        print("A senha não pode ser igual a atual!")
                                        input('')
                                        break
                                    elif len(senha_nova) < 3 or senha_nova.isspace():
                                        limpar()
                                        print("A senha deve ter mais caracteres!")
                                        input('')
                                        break
                                    elif len(senha_nova) > 30:
                                        limpar()
                                        print("A senha não pode possuir mais de 30  caracteres!")
                                        input('')
                                    else:
                                        mod_database(f'{database["user_atual"]}' , f'{senha_nova}')
                                        limpar()
                                        print(f"Senha de {database['user_atual']} alterada  com  sucesso!")
                                        input('')
                                        loop_senha_nova = False
                                        break
                            else:
                                limpar()
                                print("Acesso negado!")
                                input('')
                        elif var == '2':
                            loop_senha_nova = False
                            break
                elif var == "3":
                    while True:
                        limpar()
                        login = str(input(Fore.LIGHTWHITE_EX + """
     Faça o login para apagar usuário
    ───────────────────────────────────

      Login: """))
                        if login in cadastrados:
                            limpar()
                            senha = str(input(Fore.LIGHTWHITE_EX + f"""
               Fazer Login
    ───────────────────────────────────

      Login: {login}
      Senha: """)) 
                            if senha == cadastrados[f'{login}']:
                                while True:
                                    limpar()
                                    print(Fore.LIGHTRED_EX + "Você tem certeza que deseja excluir esse usuário?")
                                    var = input(Fore.LIGHTRED_EX + '\n1 ──► Sim\n2 ──► Não\n\n ──► ')
                                    if var == '1':
                                        delete_data(login)
                                        limpar()
                                        print(Fore.LIGHTBLUE_EX + 'Usuário deletado com sucesso!')
                                        if database['user_atual'] == login:
                                            deslogar()
                                        input('')
                                        break
                                    elif var == "2":
                                        break
                            else:
                                limpar()
                                print(Fore.LIGHTRED_EX + "Senha incorreta!")
                                input('')
                                break
                        else:
                            limpar()
                            print(Fore.LIGHTRED_EX + "Usuário não cadastrado")   
                            input('')
                            break  
                        break              
                elif var == "0":
                    loop_1 = False
                    break
        else:
            limpar()
            print(Fore.LIGHTRED_EX + "Você precisa estar logado para entrar!")
            input('')
            fazer_login()
            if database['user_atual'] == "Nenhum!":
                break

#Faz o usuario logar
def fazer_login():
    while True:
        limpar()
        login = str(input(Fore.LIGHTWHITE_EX + """
           Fazer Login
───────────────────────────────────

  Login: """))
        if login in cadastrados: #Se o user estiver no dicionário ele irá permitir a entrada da senha
            limpar()
            senha = str(input(Fore.LIGHTWHITE_EX + f"""
           Fazer Login
───────────────────────────────────

  Login: {login}
  Senha: """)) 
            if senha == cadastrados[f'{login}']: #Se a senha atribuida pelo usuario for a mesma pertencente ele será logado
                limpar()
                mod_database2('status' , 'Logado')
                mod_database2('user_atual', f'{login}')
                print(Fore.LIGHTGREEN_EX + "Logado com sucesso!")
                input('')
                break
            else:
                limpar()
                print(Fore.LIGHTRED_EX + "Senha incorreta!")
                input('')
                break
        else:
            limpar()
            print(Fore.LIGHTRED_EX + "Usuário não cadastrado")   
            input('')
            break                            
            
#Cadastro
def cadastrar_user():
    while True:
        limpar()
        username = str(input(Fore.LIGHTWHITE_EX + """
          Cadastrar user
───────────────────────────────────

  Username: """))
        if username not in cadastrados and len(username) > 3 and not username.isspace() and len(username) < 20:
            while True:   
                limpar()
                senha = str(input(Fore.LIGHTWHITE_EX + f"""
          Cadastrar user
───────────────────────────────────

  Username: {username}
  Senha: """))
                if len(senha) < 3 or senha.isspace():
                    limpar()
                    print(Fore.LIGHTRED_EX + "Digite uma senha com mais caracteres!")
                    input('')
                elif len(senha) > 30:
                    limpar()
                    print(Fore.LIGHTRED_EX + "Máximo permitido: 30 Letras!")
                    input('')
                else:
                    limpar()
                    mod_database(username, senha)
                    print(Fore.LIGHTRED_EX + "Usúario cadastrado com sucesso!!")
                    input('')
                    break
            break
        elif username in cadastrados:
            limpar()
            print(Fore.LIGHTRED_EX + "Usuário já possui cadastro!!")
            input('')
        elif len(username) < 3 or username.isspace():
            print(Fore.LIGHTRED_EX + "Não possui caracteres suficientes!")
            input('')
        elif len(username) > 20:
            limpar()
            print(Fore.LIGHTRED_EX + "Máximo permitido: 20 Letras!")

#Checa e salva todos os dados na base de dados
check_database()




#loop principal
while True:
    if database['status'] == 'Não logado':
        status = Fore.LIGHTRED_EX + database['status'] + Fore.LIGHTWHITE_EX + ''
    elif database['status'] == 'Logado':
        status = Fore.LIGHTGREEN_EX + database['status']  + Fore.LIGHTWHITE_EX + ''  
    user_atual_status = Fore.LIGHTCYAN_EX + database['user_atual']  + Fore.LIGHTWHITE_EX + ''
    
    
    limpar()
    print(f"""        
───────────────────────────────────          
Status: {status}         
───────────────────────────────────
User atual: {user_atual_status}
───────────────────────────────────

        Entrar no sistema
───────────────────────────────────

    1 ────► Menu 

    2 ────► Fazer Login

    3 ────► Cadastrar-se

    4 ────► Sair

    0 ────► Fechar aplicação

""")
    var = str(input("───► "))
    if var == "1":
        if database['user_atual'] == 'Admin':
            aba_admin()
        else:
            menu_login()
    elif var == "2":
        fazer_login()
    elif var == "3":
        cadastrar_user() 
    elif var == "4":
        if database['status'] == 'Logado' and database['user_atual'] != 'Nenhum!':
            deslogar()
    elif var == "0":
        break
    