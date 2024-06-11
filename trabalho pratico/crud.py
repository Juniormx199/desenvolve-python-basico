import os.path

arquivo_usuarios = "usuarios.txt"

#Funcao para ler arquivo
def ler_arquivo(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        escrever_arquivo(nome_arquivo)
    with open(nome_arquivo, "r") as arquivo:
        return arquivo.readlines()

#Funcao para escrever arquivo 
def escrever_arquivo(nome_arquivo , linhas="adm,adm\n"):
    with open(nome_arquivo, "w") as arquivo:
        arquivo.writelines(linhas)

#Funcao para validar se o usuario existe : parametro senha e opcional (se passar ele a funcao verifica a senha tambem)
def validar_usuario(nome , senha = ""):
    linhas = ler_arquivo(arquivo_usuarios)
    for linha in linhas:
        usuario_txt, senha_txt = linha.strip().split(",")
        if usuario_txt.lower() == nome.lower():
            if senha == "":
                print("Usuário já existe \n")
                return True
            else: 
                if (senha_txt == senha):
                    return True
                else:
                    print("Senha incorreta !!! \n")

    return False

#Funcao para adicionar um novo usuario
def inserir_usuarios(nome, senha):
    if not validar_usuario(nome):
        linhas = ler_arquivo(arquivo_usuarios)
        linhas.append(f"{nome},{senha}\n")
        escrever_arquivo(arquivo_usuarios , linhas)
        print("Usuário cadastrado !!! \n")

#Funcao para alterar o usuario : tem duas opcoes = 3 altera a senha / 4 altera o nome (so pode alterar se fornecer usuario e senha atual)
def alterar_usuario(nome, senha , novo, opcao):
    if validar_usuario(nome , senha):
        linhas = ler_arquivo(arquivo_usuarios)
        index = linhas.index(f"{nome},{senha}\n")
        if opcao == "2":
            linhas[index]= f"{nome},{novo}\n"
        else:   
            linhas[index]= f"{novo},{senha}\n"
        escrever_arquivo(arquivo_usuarios , linhas)
        print("Usuario Alterado !!! \n")
        return True
    else:
        return False

#Funcao para excluir o usuario (so pode excluir se fornecer usuario e senha atual)
def excluir_usuario(nome, senha):
    if validar_usuario(nome , senha):
        linhas = ler_arquivo(arquivo_usuarios)
        index = linhas.index(f"{nome},{senha}\n")
        linhas.pop(index)
        escrever_arquivo(arquivo_usuarios , linhas)
        print("Usuario excluido !!! \n")




def menu_login():
    print("1 - entrar no sistema")
    print("2 - sair")
    opcao = input("opcao: ")
    if opcao == "1":
        while True:
            nome = input("Nome: ")
            senha = input("Senha: ")
            if validar_usuario(nome, senha):
                print("Login efetuado com sucesso!!! \n")
                return sub_menu(nome)
            else:
                print("Usuario ou senha incorretos , tente novamente ! \n")
    else:
        return

def sub_menu(usuario):
     while True:
        print("1 - Manutencao usuario")
        print("2 - Manutencao Produtos/Servicos")
        print("3 - Sair")
        opcao = input("opcao: ")
        if opcao == '3':
            return
        elif opcao == "1":
            return menu_usuario(usuario)
        
def menu_usuario(usuario):
    while True:

        print("1 - cadastrar usuario")
        print("2 - alterar senha")
        print("3 - alterar nome")
        print("4 - excluir usuario")
        print("5 - voltar")
        print("6 - sair")

        opcao = input("opcao: ")

        if opcao == "6": 
            return
    
        if opcao == "5": 
            return sub_menu(usuario)

        if opcao == "1":
            nome = input("Nome: ")
            senha = input("Senha: ")
            inserir_usuarios(nome, senha)    
            
        if opcao == "2":
            alterar_usuario(usuario, input("Senha Atual: ") ,input("Nova Senha: "), opcao)

        if opcao == "3":
            alterar_usuario(usuario, input("Senha Atual: ") ,input("Novo nome: "), opcao)

        if opcao == "4":
            excluir_usuario(input("Usuario: ") ,input("Senha: "))


menu_login()








  



   



    
