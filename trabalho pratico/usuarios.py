import csv
import pandas as pd
import os

#Função para salvar um novo arquivo dos usuarios
def salvar_usuarios(usuarios):
    with open('usuarios.csv', mode='w' , newline='') as arquivo:
        nomes_campos = ['codigo', 'nome_completo', 'usuario', 'senha', 'administrador','funcionario']
        linhas = csv.DictWriter(arquivo, fieldnames = nomes_campos)
        linhas.writeheader()
        for linha in usuarios:
            linhas.writerow(linha)

#Função para ler o arquivo dos usuarios
def carregar_usuarios():
    usuarios = []
    if not os.path.exists('usuarios.csv'):
        salvar_usuarios(usuarios)    
    with open('usuarios.csv', mode='r') as arquivo:
        linhas = csv.DictReader(arquivo)
        for linha in linhas:
            usuarios.append(linha)
    return usuarios

#Função para buscar o ultimo codigo cadastrado para incluir um novo usuario seguindo a sequencia dos codigos
def busca_ultimo_codigo(usuarios):
    return int(usuarios[-1]["codigo"]) + 1 if len(usuarios) > 0 else 1

#Função para criar um novo usuario
def criar_usuario(usuarios, nome_completo, usuario, senha, administrador, funcionario):
    list(usuarios)
    codigo = busca_ultimo_codigo(usuarios)
    usuarios.append({
        'codigo': codigo,
        'nome_completo': nome_completo,
        'usuario': usuario,
        'senha': senha,
        'administrador': administrador,
        'funcionario': funcionario
    })
    salvar_usuarios(usuarios)
    return f"Usuário criado com sucesso!\nCodigo do usuario: {codigo}"

#Funçãpo para alterar um usuario
def alterar_usuario(usuarios, usuario_codigo, **parametros):
    for index ,linha in enumerate(usuarios):
        if linha['usuario'] == usuario_codigo or linha['codigo'] == usuario_codigo:
            usuarios[index].update(parametros)
            salvar_usuarios(usuarios)
            return "Usuário atualizado com sucesso!"             

#Função para exluir um usuario
def deletar_usuario(usuarios, nome_codigo):
    for index ,linha in enumerate(usuarios):
        if linha['usuario'] == nome_codigo or linha['codigo'] == nome_codigo:
            del usuarios[index]
            salvar_usuarios(usuarios)
            return "Usuário removido com sucesso!"
        
#Função para listar os usuarios cadastrados
def listar_usuarios(usuarios):
    return pd.DataFrame(usuarios)

#Função para validar usuario e senha
def login_usuario(usuarios , nome_usuario , senha_usuario):
    for usuario in usuarios:
        if (usuario['usuario'] == nome_usuario or usuario['codigo'] == nome_usuario ) and usuario['senha'] == senha_usuario:
            return True , usuario
    return False , {}

#Função para ver se o usuario existe , pode usar o nome ou codigo do usuario
def validar_existencia_usuario_codigo(usuarios , nome_codigo):
    for usuario in usuarios:
        if usuario['usuario'] == nome_codigo or usuario['codigo'] == nome_codigo:
            return True
    return False
