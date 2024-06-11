import os.path

arquivo_usuarios = "usuarios.txt"

#------------------------------------------------------------------------------------------------------------------------

#Funcoes Globais
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

#------------------------------------------------------------------------------------------------------------------------

#Funcoes Usuario
#Funcao para validar se o usuario existe : parametro senha e opcional (se passar ele a funcao verifica a senha tambem)
def validar_usuario(nome , senha = ""):
    linhas = ler_arquivo(arquivo_usuarios)
    for linha in linhas:
        usuario_txt, senha_txt = linha.strip().split(",")
        if senha != "":
            if usuario_txt.lower() == nome.lower() and senha_txt == senha:
                return True  
        else: 
            if usuario_txt.lower() == nome.lower():
                print("*** Usuário já existe ***\n")
                return True
            
    print("*** Usuario ou senha incorretos ***\n")    
    return False

#Funcao para adicionar um novo usuario
def inserir_usuario(nome, senha):
    if not validar_usuario(nome):
        linhas = ler_arquivo(arquivo_usuarios)
        linhas.append(f"{nome},{senha}\n")
        escrever_arquivo(arquivo_usuarios , linhas)
        print("*** Usuário cadastrado ***\n")

#Funcao para alterar o usuario : tem duas opcoes = 3 altera a senha / 4 altera o nome (so pode alterar se fornecer senha atual do usuario logado)
def alterar_usuario(nome, senha , novo, opcao):
    if validar_usuario(nome , senha):
        linhas = ler_arquivo(arquivo_usuarios)
        index = linhas.index(f"{nome},{senha}\n")
        if opcao == "2":
            linhas[index]= f"{nome},{novo}\n"
        else:   
            linhas[index]= f"{novo},{senha}\n"
        escrever_arquivo(arquivo_usuarios , linhas)
        print("*** Usuario Alterado ***\n")
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
        print("*** Usuario excluido ***\n")



#--------------------------------------------------------------------------------------------------------------------------------------

#Funcoes de menu
def menu_login():
    print("\n===========================")
    print("     SISTEMA DE GESTÃO")
    print("===========================\n")
    print("1 - Entrar no sistema")
    print("2 - Sair")
    opcao = input("\nOpção: ")
    if opcao == "1":
        print("\n===========================")
        print("Informe seus dados: ")
        while True:
            nome = input("Nome: ")
            senha = input("Senha: ")
            if validar_usuario(nome, senha):
                print("Login efetuado com sucesso!!! \n")
                return sub_menu(nome)
    else:
        return

def sub_menu(usuario):
    while True:
        print("\n===========================")
        print("       MENU PRINCIPAL")
        print("===========================\n")
        print("1 - Manutenção Usuário")
        print("2 - Manutenção Produtos/Serviços")
        print("3 - Sair")
        opcao = input("\nOpção: ")
        if opcao == '3':
            return
        elif opcao == "1":
            return menu_usuario(usuario)

def menu_usuario(usuario):
    while True:
        print("===========================")
        print("     MANUTENÇÃO USUÁRIO")
        print("===========================\n")
        print("1 - Cadastrar Usuário")
        print("2 - Alterar Senha")
        print("3 - Alterar Nome")
        print("4 - Excluir Usuário")
        print("5 - Voltar")
        print("6 - Sair")
        opcao = input("\nOpção: ")

        if opcao == "6":
            return

        if opcao == "5":
            return sub_menu(usuario)

        if opcao == "1":
            nome = input("\nNome: ")
            senha = input("Senha: ")
            inserir_usuario(nome, senha)

        if opcao == "2":
            alterar_usuario(usuario, input("\nSenha Atual: "), input("Nova Senha: "), opcao)

        if opcao == "3":
            alterar_usuario(usuario, input("\nSenha Atual: "), input("Novo Nome: "), opcao)

        if opcao == "4":
            excluir_usuario(input("\nUsuário: "), input("Senha: "))

menu_login()








  



   



    
