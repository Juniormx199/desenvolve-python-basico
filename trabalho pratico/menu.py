import usuarios as user
import produtos as prod
import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
linha = lambda: print("-----------------------------------------")

usuarios = user.carregar_usuarios()
produtos = prod.carregar_produtos()


def menu_principal(usuarios , produtos):
    clear()
    while True:
        print('####################################')
        print('#         Sistema de Gestão        #')
        print('####################################')
        print('# 1 - Entrar no sistema            #')
        print('# 0 - Sair                         #')
        print('####################################')
        opcao = input('Opção: ')
        if opcao == '0':
            return
        if opcao == '1':
            usuario = input('Usuário: ')
            senha = input('Senha: ')
            clear()
            entrou , usuario_logado  = user.login(usuarios, usuario, senha)
            if entrou:
                print('Login efetuado com sucesso')
                return sub_menu(usuarios , produtos , usuario_logado)
            else: 
                print('Usuário ou senha incorretos')
                return
        
def sub_menu(usuarios , produtos , usuario_logado):
    while True:
        clear()
        print('####################################')
        print('#          Menu Principal          #')
        print('####################################')
        print('# 1 - Manutenção de Usuários       #')
        print('# 2 - Manutenção de Produtos       #')
        print('# 0 - Sair                         #')
        print('####################################')
        opcao = input('Opção: ')
        if opcao == '0':
            return
        if opcao == '1':
            return menu_usuario(usuarios , produtos , usuario_logado)
        if opcao == '2':
            return menu_produto(produtos , usuarios , usuario_logado)

def menu_usuario(usuarios , produtos , usuario_logado):
    adm = usuario_logado['administrador']
    clear()
    while True:
        print('####################################')
        print('#      Manutenção de Usuários      #')
        print('####################################')
        if adm == 'True':
            print('# 1 - Incluir Usuário              #')
            print('# 2 - Excluir Usuário              #')
            print('# 3 - Listar Usuários              #')
        print('# 4 - Alterar Usuário              #')    
        print('# 5 - Voltar                       #')
        print('# 0 - Sair                         #')
        print('####################################')
        opcao = input('Opção: ')

        if opcao == '0':
            return
        
        if opcao == '5':
            return sub_menu(usuarios , produtos , usuario_logado)
        
        if opcao == '1' and adm == 'True':
            inputs_incluir_usuario(usuarios)

        if opcao == '2' and adm == 'True':
            inputs_excluir_usuario(usuarios)

        if opcao == '3' and adm == 'True':
            clear()
            linha()
            user.listar_usuarios(usuarios)
            linha()

        if opcao == '4':
            inputs_alterar_usuario(usuarios)
    

def inputs_incluir_usuario(usuarios):
    clear()
    nome_completo = input("Nome completo: ")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    administrador = (lambda adm: adm.lower() == 'sim')(input("Administrador (sim/não): "))
    funcionario = not administrador
    clear()
    linha()
    user.criar_usuario(usuarios, nome_completo, usuario, senha, administrador, funcionario)
    linha()

def inputs_alterar_usuario(usuarios):
    clear()
    nome_codigo = input("Digite o nome ou código do usuário a ser alterado: ")
    senha_atual = input("Digite a senha atual do usuário ou uma senha de qualquer usuário ADM: ")
    if user.validar_senha_adm(usuarios, senha_atual) and user.validar_usuario_codigo(usuarios, nome_codigo):
        nome_completo = input("Novo nome completo: ")
        usuario = input("Novo usuário: ")
        senha = input("Nova senha: ")
        if user.validar_senha_adm(usuarios, senha_atual):
            administrador = (lambda adm: adm.lower() == 'sim')(input("Administrador (sim/não): "))
            funcionario = not administrador
            clear()
            linha()
            user.alterar_usuario(usuarios, nome_codigo=nome_codigo, nome_completo=nome_completo, usuario=usuario, senha=senha, administrador=administrador, funcionario=funcionario)
            linha()
        else:
            clear()
            linha()
            user.alterar_usuario(usuarios, nome_codigo=nome_codigo, nome_completo=nome_completo, usuario=usuario, senha=senha)
            linha()

def inputs_excluir_usuario(usuarios):
    clear()
    nome_codigo = input("Digite o nome ou código do usuário a ser excluído: ")
    senha_adm = input('Para confirmar a exclusão, digite uma senha de ADM: ')
    if user.validar_senha_adm(usuarios, senha_adm):
        clear()
        linha()
        user.deletar_usuario(usuarios, nome_codigo)
        linha()
    else:
        print("Senha incorreta")


def menu_produto(produtos , usuarios , usuario_logado):
    clear()
    adm = usuario_logado['administrador']
    while True:
        print('####################################')
        print('#      Manutenção de Produtos      #')
        print('####################################')
        print('# 1 - Incluir Produto              #')
        print('# 2 - Alterar Produto              #')
        if adm == 'True':
            print('# 3 - Excluir Produto              #')
        print('# 4 - Listar Produto               #')
        print('# 5 - Voltar                       #')
        print('# 0 - Sair                         #')
        print('####################################')
        opcao = input('Opção: ')
        if opcao == '0':
            return
        if opcao == '5':
            return sub_menu(usuarios , produtos , usuario_logado)
        if opcao == '1':
            clear()
            inputs_incluir_produto(produtos)
        if opcao == '2':
            clear()
            inputs_alterar_produto(produtos)
        if opcao == '3' and adm == 'True':
            clear()
            inputs_excluir_produto(produtos , usuarios)
        if opcao == '4':
            clear()
            linha()
            prod.listar_produto(produtos)
            linha()


def inputs_incluir_produto(produtos):
    descricao = input("Descrição: ")
    unidade = input("Unidade: ")
    preco_custo = input("Preço de custo: ")
    preco_venda = input("Preço de venda: ")
    estoque = input("Quantidade de estoque: ")
    clear()
    linha()
    prod.criar_produto(produtos, descricao, unidade, preco_custo, preco_venda, estoque)
    linha()

def inputs_alterar_produto(produtos):
    codigo_descricao = input("Digite a descrição ou código do produto a ser alterado: ")
    descricao = input("Descrição: ")
    unidade = input("Unidade: ")
    preco_custo = input("Preço de custo: ")
    preco_venda = input("Preço de venda: ")
    estoque = input("Quantidade de estoque: ")
    clear()
    linha()
    prod.alterar_produto(produtos, codigo_descricao, descricao=descricao, unidade=unidade, preco_custo=preco_custo, preco_venda=preco_venda, estoque=estoque)
    linha()

def inputs_excluir_produto(produtos , usuarios):
    codigo_descricao = input("Digite a descrição ou código do produto a ser excluído: ")
    senha_adm = input('Para confirmar a exclusão, digite uma senha de ADM: ')
    if user.validar_senha_adm(usuarios, senha_adm):
        clear()
        linha()
        prod.deletar_produto(produtos, codigo_descricao)
        linha()
    else:
        print("Senha incorreta")


menu_principal(usuarios , produtos)


