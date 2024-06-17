import os.path
import os

arquivo_usuarios = "usuarios.csv"
arquivo_produtos = "produtos.csv"

#------------------------------------------------------------------------------------------------------------------------

#Funcoes Globais
#Funcao para ler arquivo
def ler_arquivo(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        if nome_arquivo == 'usuarios.csv':
            escrever_arquivo(nome_arquivo , "adm,adm,True,False\n")
        else:
            escrever_arquivo(nome_arquivo , "")

    with open(nome_arquivo, "r") as arquivo:
        return arquivo.readlines()

#Funcao para escrever arquivo 
def escrever_arquivo(nome_arquivo , linhas , modo ="w"):
    with open(nome_arquivo, modo) as arquivo:
        arquivo.writelines(linhas)

def limpar_console():
    os.system('cls') or None

#------------------------------------------------------------------------------------------------------------------------

#Funcoes Usuario

def validar_usuario(usuario , senha= ''):
    for linha in ler_arquivo(arquivo_usuarios):
        usuario_csv, senha_csv , adm_csv , funcionario_csv = linha.strip().split(",")
        if usuario_csv.lower() == usuario.lower():
            if senha != " ":
                if senha_csv == senha:
                    return True 
            return True      
    return False

def permissoes_usuario(usuario):
    linhas = ler_arquivo(arquivo_usuarios)
    for linha in linhas:
        usuario_csv, senha_csv , adm_csv , funcionario_csv = linha.strip().split(",")
        if usuario_csv == usuario:
            return adm_csv , funcionario_csv

def busca_index_usuario(usuario):
    linhas = ler_arquivo(arquivo_usuarios)
    for linha in linhas:
        usuario_csv, senha_csv , adm_csv , funcionario_csv = linha.strip().split(",")
        if usuario_csv == usuario:
            return linhas , linhas.index(linha) 
        
        
#Funcao para adicionar um novo usuario
def inserir_usuario(usuario, senha , adm , funcionario):
    if not validar_usuario(usuario):
        dados_usuario = f"{usuario},{senha},{adm},{funcionario}\n"
        escrever_arquivo(arquivo_usuarios , dados_usuario , "a")
        print("Usuário cadastrado !!!\n")
    else:
        print("Nome de usuario ja existe! tente novamente...\n")


#Funcao para excluir o usuario (so pode excluir se fornecer usuario e senha atual)
def excluir_usuario(usuario):
    if validar_usuario(usuario):
        if input("Realmente deseja excluir o usuario? (sim/nao)").lower() == "sim":
            linhas , index = busca_index_usuario(usuario)
            linhas.pop(index)
            escrever_arquivo(arquivo_usuarios , linhas)
            print("*** Usuario excluido ***\n")

def alterar_usuario(usuario):
    senha = input("Senha atual do usuario logado: ")
    if validar_usuario(usuario , senha):
        nova_senha = input("nova senha: ")
        adm , funcionario = permissoes_usuario(usuario)

        if input("Usuario e adm? (sim/nao)").lower() == "sim":
            adm = True        
        else:
            adm = False
            funcionario = True

        linhas , index = busca_index_usuario(usuario)
        linhas[index] = f"{usuario},{nova_senha},{adm},{funcionario}\n"
        escrever_arquivo(arquivo_usuarios , linhas)

    
#funcoes produtos
def validar_produto(descricao , codigo = ""):
    for linha in ler_arquivo(arquivo_produtos):
        codigo_csv ,descricao_csv, unidade_csv , valor_csv , estoque_csv = linha.strip().split(",")
        if descricao_csv.lower() == descricao.lower():
            if codigo != "":
                if codigo_csv == codigo:
                    return True 
            return True      
    return False

def busca_index_produtos(descricao):
    linhas = ler_arquivo(arquivo_produtos)
    for linha in linhas:
        codigo_csv ,descricao_csv, unidade_csv , valor_csv , estoque_csv = linha.strip().split(",")
        if descricao_csv == descricao:
            return linhas , linhas.index(linha)     
        
def inserir_produto(codigo, descricao , unidade , valor , estoque):
    if not validar_produto(descricao , codigo):
        dados_produto = f"{codigo},{descricao},{unidade},{valor},{estoque}\n"
        escrever_arquivo(arquivo_produtos , dados_produto , "a")
        print("Produto cadastrado !!!\n")
    else:
        print("Produto ja existe! tente novamente...\n")

def excluir_produto(descricao):
    if validar_produto(descricao):
        if input("Realmente deseja excluir o produto? (sim/nao)").lower() == "sim":
            linhas , index = busca_index_usuario(descricao)
            linhas.pop(index)
            escrever_arquivo(arquivo_produtos , linhas)
            print("*** Produto excluido ***\n")

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
            usuario = input("Nome: ")
            senha = input("Senha: ")
            if validar_usuario(usuario, senha):
                limpar_console()
                print("Login efetuado com sucesso!!!")
                return sub_menu(usuario)
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
            limpar_console()
            return menu_usuario(usuario)
        elif opcao == "2":
            return menu_produto(usuario)

def menu_usuario(usuario):
    while True:
        adm , funcionario = permissoes_usuario(usuario)
        print("===========================")
        print("     MANUTENÇÃO USUÁRIO")
        print("===========================\n")
        if adm == True:
            print("1 - Cadastrar Usuário")
            print("2 - Excluir Usuário")
            print("3 - Listar Usuário")

            if opcao == "1":
                nome = input("\nNome: ")
                senha = input("Senha: ")
                adm = False
                funcionario = False
                if input("Usuario e adm? (sim ou nao) ").lower() == "sim":
                    adm = True
                inserir_usuario(nome, senha , adm, funcionario)
            
            if opcao == "2":
                excluir_usuario(input("\nUsuário: "))

        print("4 - Alterar Usuário")
        print("5 - Voltar")
        print("6 - Sair")
        opcao = input("\nOpção: ")

        if opcao == "6":
            return

        if opcao == "5":
            return sub_menu(usuario)

        if opcao == "4":
           alterar_usuario(usuario)


def menu_produto(usuario):
    while True:
        adm , funcionario = permissoes_usuario(usuario)
        print("===========================")
        print("     MANUTENÇÃO PRODUTO")
        print("===========================\n")
        print("1 - Cadastrar Produto")
        print("2 - Excluir Produto")
        print("3 - Listar Produto")
        print("4 - Alterar Produto")
        print("5 - Voltar")
        print("6 - Sair")
        opcao = input("\nOpção: ")

        if opcao == "6":
            return

        if opcao == "5":
            return sub_menu(usuario)

        if opcao == "1":
            codigo = input("codigo: ")
            descricao = input("descricao: ")
            unidade = input("unidade: ")
            valor = input("valor: ")
            estoque = input("estoque: ")
            inserir_produto(codigo,descricao,unidade,valor,estoque)

        if opcao == "2":
            excluir_produto(input("\nDescricao: "))

        

menu_login()








  



   



    
