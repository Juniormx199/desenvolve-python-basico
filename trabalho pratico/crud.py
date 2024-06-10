import os.path

def ler_arquivo_usuarios():
    with open("usuarios.txt", "r") as arquivo:
        return arquivo.readlines()

def escreve_arquivo_usuarios(linhas):
    with open("usuarios.txt", "w") as arquivo:
        arquivo.writelines(linhas)
    
def alterar_usuario(nome, senha , novo, opcao):
    valido , index = validar_usuario(nome , senha)
    if valido:
        linhas = ler_arquivo_usuarios()
        if opcao == "3":
            linhas[index]= f"{nome},{novo}\n"
        else:   
            linhas[index]= f"{novo},{senha}\n"
        escreve_arquivo_usuarios(linhas)

def excluir_usuario(nome, senha):
    valido , index = validar_usuario(nome , senha)
    if valido:
        linhas = ler_arquivo_usuarios()
        linhas.pop(index)
        escreve_arquivo_usuarios(linhas)

def validar_usuario(nome , senha = ""):
    linhas = ler_arquivo_usuarios()
    for linha in linhas:
        usuario_txt, senha_txt = linha.strip().split(",")
        if usuario_txt.lower() == nome.lower():
            if senha == "":
                return True
            else: 
                if (senha_txt == senha):
                    return True , linhas.index(f"{nome},{senha}\n")
    return False , -1

def inserir_usuarios(nome, senha):
    if not validar_usuario(nome):
        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(f"{nome},{senha}\n")
            print("Usuário cadastrado")
    else:
        print("Usuário já existe")



while True:
    print("1 - entrar no sistema")
    print("2 - cadastrar usuario")
    print("3 - alterar senha")
    print("4 - alterar nome")
    print("5 - excluir usuario")
    print("6 - sair")

    opcao = input("opcao: ")

    if opcao == "6": break

    nome = input("Nome: ")
    senha = input("Senha: ")

    if opcao == "1":
        if validar_usuario(nome, senha):
            print("Login efetuado com sucesso!!!")
        else:
            print("Usuario ou senha incorretos!!!")

    if opcao == "2":
        inserir_usuarios(nome, senha)

    if opcao == "3":
        alterar_usuario(nome, senha ,input("Nova Senha: "), opcao)
    
    if opcao == "4":
        alterar_usuario(nome, senha ,input("Novo nome: "), opcao)

    if opcao == "5":
        excluir_usuario(nome, senha)

    
