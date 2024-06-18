import usuarios as user
import produtos as prod
import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

usuarios = user.carregar_usuarios()
produtos = prod.carregar_produtos()


#------------------------ MENUS ------------------------------------------
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
            valido , usuario_logado  = user.login_usuario(usuarios, usuario, senha)
            if valido:
                print('Login efetuado com sucesso')
                return sub_menu(usuarios , produtos , usuario_logado)
            else:
                print('Usuário ou senha incorretos , tente novamente! \n')
        
def sub_menu(usuarios , produtos , usuario_logado):
    clear()
    while True:
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
        elif opcao == '1':
            return menu_usuario(usuarios , produtos , usuario_logado)
        elif opcao == '2':
            return menu_produto(produtos , usuarios , usuario_logado)
        else:
            clear() 
            print('Opção Invalida , tente novamente! \n')

#------------------------ USUARIO ------------------------------------------
def menu_usuario(usuarios , produtos , usuario_logado):
    adm = usuario_logado['administrador']
    clear()
    while True:
        print('####################################')
        print('#      Manutenção de Usuários      #')
        print('####################################')
        if adm == 'True':
            print('# 1 - Incluir Usuário              #')
        print('# 2 - Alterar Usuário              #')
        if adm == 'True':
            print('# 3 - Excluir Usuário              #') 
            print('# 4 - Listar Usuários              #')   
        print('# 5 - Voltar                       #')
        print('# 0 - Sair                         #')
        print('####################################')
        opcao = input('Opção: ')

        if opcao == '0':
            return
        
        if opcao == '5':
            return sub_menu(usuarios , produtos , usuario_logado)
        
        if opcao == '1' and adm == 'True':
            clear()
            inputs_incluir_usuario(usuarios)

        if opcao == '2':
            clear()
            inputs_alterar_usuario(usuarios , adm)

        if opcao == '3' and adm == 'True':
            clear()
            inputs_excluir_usuario(usuarios)

        if opcao == '4' and adm == 'True':
            clear()
            user.listar_usuarios(usuarios)

def inputs_incluir_usuario(usuarios):
    nome_completo = input("Nome completo: ")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    administrador = (lambda adm: adm.lower() == 'sim')(input("Administrador (sim/não): "))
    funcionario = not administrador
    clear()
    user.criar_usuario(usuarios, nome_completo, usuario, senha, administrador, funcionario)

def inputs_alterar_usuario(usuarios , adm):
    nome_codigo = input("Digite o nome ou código do usuário a ser alterado: ")
    if adm == 'False':
        senha_atual = input("Digite a senha atual do usuário: ")
        valido , dados_usuario = user.login_usuario(usuarios , nome_codigo , senha_atual)
        if not valido:
            print('Senha incorreta!')
            return
    if not user.validar_usuario_codigo(usuarios , nome_codigo):
        print("Usuario não encontrado")
        return
    nome_completo = input("Novo nome completo: ")
    usuario = input("Novo usuário: ")
    senha = input("Nova senha: ")
    if adm == 'True':
        administrador = (lambda adm: adm.lower() == 'sim')(input("Administrador (sim/não): "))
        funcionario = not administrador
        user.alterar_usuario(usuarios, nome_codigo=nome_codigo, nome_completo=nome_completo, usuario=usuario, senha=senha, administrador=administrador, funcionario=funcionario)
    else:
        user.alterar_usuario(usuarios, nome_codigo=nome_codigo, nome_completo=nome_completo, usuario=usuario, senha=senha)
        
def inputs_excluir_usuario(usuarios):
    nome_codigo = input("Digite o nome ou código do usuário a ser excluído: ")
    opcao = input("Realmente deseja exlcuir esse usuario (sim/nao): ")
    clear()
    if opcao.lower() == 'sim':
        user.deletar_usuario(usuarios, nome_codigo)


#------------------------ PRODUTO ------------------------------------------
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
            inputs_excluir_produto(produtos)
        if opcao == '4':
            clear()
            prod.listar_produto(produtos)

def inputs_incluir_produto(produtos):
    descricao = input("Descrição: ")
    unidade = input("Unidade: ")
    preco_custo = input("Preço de custo: ")
    preco_venda = input("Preço de venda: ")
    estoque = input("Quantidade de estoque: ")
    clear()
    prod.criar_produto(produtos, descricao, unidade, preco_custo, preco_venda, estoque)

def inputs_alterar_produto(produtos):
    codigo_descricao = input("Digite a descrição ou código do produto a ser alterado: ")
    descricao = input("Descrição: ")
    unidade = input("Unidade: ")
    preco_custo = input("Preço de custo: ")
    preco_venda = input("Preço de venda: ")
    estoque = input("Quantidade de estoque: ")
    clear()
    prod.alterar_produto(produtos, codigo_descricao, descricao=descricao, unidade=unidade, preco_custo=preco_custo, preco_venda=preco_venda, estoque=estoque)

def inputs_excluir_produto(produtos):
    codigo_descricao = input("Digite a descrição ou código do produto a ser excluído: ")
    opcao = input("Realmente deseja exlcuir esse produto (sim/nao): ")
    clear()
    if opcao.lower() == 'sim':
        prod.deletar_produto(produtos, codigo_descricao)


menu_principal(usuarios , produtos)

