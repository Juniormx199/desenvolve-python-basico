import csv
import os

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
            print("usuario ja existe")
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
    print("Usuário criado com sucesso!")
#criar_usuario(usuarios, '1', 'usuario', 'senha', 'administrador')

def alterar_usuario(usuarios, nome_codigo, **kwargs):
    for index ,linha in enumerate(usuarios):
        if linha['usuario'] == nome_codigo or linha['codigo'] == nome_codigo:
            usuarios[index].update(kwargs)
            salvar_usuarios(usuarios)
            print("Usuário atualizado com sucesso!")
            return
        
    print("Usuario não encontrado")
    return                  
#alterar_usuario(usuarios,'usuario121111', senha='Paulo Henrique', administrador='paulohenrique@example.com')


def deletar_usuario(usuarios, nome_codigo):
    for index ,linha in enumerate(usuarios):
        if linha['usuario'] == nome_codigo or linha['codigo'] == nome_codigo:
            del usuarios[index]
            salvar_usuarios(usuarios)
            print("Usuário removido com sucesso!")
            return
        
    print("Usuario não encontrado")
    return        
#deletar_usuario(usuarios,'usuario1231')

def listar_usuarios(usuarios):
      for usuario in usuarios:
        print(usuario)

def login(usuarios , nome_usuario , senha_usuario):
    for usuario in usuarios:
        if usuario['usuario'] == nome_usuario and usuario['senha'] == senha_usuario:
            return True
    return False

#validar_usuario(usuarios , 'usuario123' , 'senha')

def validar_usuario_codigo(usuarios , nome_codigo):
    for usuario in usuarios:
        if usuario['usuario'] == nome_codigo or usuario['codigo'] == nome_codigo:
            return True
    return False

def validar_senha_adm(usuarios ,  senha):
    for usuario in usuarios:
        if usuario['senha'] == senha and usuario['administrador'] == 'True':
            return True
