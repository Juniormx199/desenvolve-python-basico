import csv
import pandas as pd
import os

linha_estilo = lambda: print("-----------------------------------------")

def salvar_usuarios(usuarios):
    with open('usuarios.csv', mode='w' , newline='') as arquivo:
        nomes_campos = ['codigo', 'nome_completo', 'usuario', 'senha', 'administrador','funcionario']
        linhas = csv.DictWriter(arquivo, fieldnames = nomes_campos)
        linhas.writeheader()
        for linha in usuarios:
            linhas.writerow(linha)

def carregar_usuarios():
    usuarios = []
    if not os.path.exists('usuarios.csv'):
        salvar_usuarios(usuarios)    
    with open('usuarios.csv', mode='r') as arquivo:
        linhas = csv.DictReader(arquivo)
        for linha in linhas:
            usuarios.append(linha)
    return usuarios

def busca_ultimo_codigo(usuarios):
    if len(usuarios) > 0:
        codigo = usuarios[-1]["codigo"]
        return int(codigo) + 1
    else:
        return 1

def criar_usuario(usuarios, nome_completo, usuario, senha, administrador, funcionario):
    list(usuarios)
    codigo = busca_ultimo_codigo(usuarios)
    for linha in usuarios:
        if linha['usuario'] == usuario:
            linha_estilo()
            print("usuario ja existe")
            linha_estilo()
            return
    usuarios.append({
        'codigo': codigo,
        'nome_completo': nome_completo,
        'usuario': usuario,
        'senha': senha,
        'administrador': administrador,
        'funcionario': funcionario
    })
    salvar_usuarios(usuarios)
    linha_estilo()
    print("Usuário criado com sucesso!")
    print(f"Codigo do usuario: {codigo}")
    linha_estilo()

def alterar_usuario(usuarios, nome_codigo, **parametros):
    for index ,linha in enumerate(usuarios):
        if linha['usuario'] == nome_codigo or linha['codigo'] == nome_codigo:
            usuarios[index].update(parametros)
            salvar_usuarios(usuarios)
            linha_estilo()
            print("Usuário atualizado com sucesso!")
            linha_estilo()
            return
    return                  

def deletar_usuario(usuarios, nome_codigo):
    for index ,linha in enumerate(usuarios):
        if linha['usuario'] == nome_codigo or linha['codigo'] == nome_codigo:
            del usuarios[index]
            salvar_usuarios(usuarios)
            linha_estilo()
            print("Usuário removido com sucesso!")
            linha_estilo()
            return
    linha_estilo()    
    print("Usuario não encontrado")
    linha_estilo()
    return        


def listar_usuarios(usuarios):
      linha_estilo()
      print("Lista de usuarios")
      print(pd.DataFrame(usuarios))
      linha_estilo()


def login_usuario(usuarios , nome_usuario , senha_usuario):
    for usuario in usuarios:
        if (usuario['usuario'] == nome_usuario or usuario['codigo'] == nome_usuario ) and usuario['senha'] == senha_usuario:
            return True , usuario
    return False , {}


def validar_usuario_codigo(usuarios , nome_codigo):
    for usuario in usuarios:
        if usuario['usuario'] == nome_codigo or usuario['codigo'] == nome_codigo:
            return True
    linha_estilo()    
    print("Usuario não encontrado")
    linha_estilo()
    return False
