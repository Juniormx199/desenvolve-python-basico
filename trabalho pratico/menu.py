import usuarios as user
import produtos as prod
import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
def resposta_estilo(resposta):
    print("-----------------------------------------")
    print(resposta)
    print("-----------------------------------------")
#------------------------ MENUS ------------------------------------------
def menu_principal():
    usuarios = user.carregar_usuarios()
    produtos = prod.carregar_produtos()
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
                resposta_estilo('Login efetuado com sucesso')
                return sub_menu(usuarios , produtos , usuario_logado)
            else:
                resposta_estilo('Usuário ou senha incorretos , tente novamente!')
        else:
            clear()
            resposta_estilo("Opção invalida , tente novamente!")
        
def sub_menu(usuarios , produtos , usuario_logado):
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
            clear()
            return menu_usuario(usuarios , produtos , usuario_logado)
        elif opcao == '2':
            clear()
            return menu_produto(produtos , usuarios , usuario_logado)
        else:
            clear()
            resposta_estilo('Opção Invalida , tente novamente!') 
##MENUS PRONTOS
#------------------------ USUARIO ------------------------------------------
def menu_usuario(usuarios , produtos , usuario_logado):
    adm = usuario_logado['administrador']
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
            clear()
            return
        if opcao == '5':
            clear()
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
            resposta_estilo(user.listar_usuarios(usuarios))

def inputs_incluir_usuario(usuarios):
    nome_completo = input("Nome completo: ")
    usuario = input("Usuário: ")
    if user.validar_existencia_usuario_codigo(usuarios , usuario):
        clear()
        resposta_estilo("Usuario ja existe")
        return
    senha = input("Senha: ")
    administrador = (lambda x: x.lower() == 'sim')(input("Administrador (sim/não): "))
    funcionario = not administrador
    clear()
    resposta_estilo(user.criar_usuario(usuarios, nome_completo, usuario, senha, administrador, funcionario))

def inputs_alterar_usuario(usuarios , adm):
    usuario_codigo = input("Digite o nome ou código do usuário a ser alterado: ")
    if not user.validar_existencia_usuario_codigo(usuarios , usuario_codigo):
        resposta_estilo("Usuario não encontrado")
        return
    if adm == 'False':
        senha_atual = input("Digite a senha atual do usuário: ")
        valido , dados_usuario = user.login_usuario(usuarios , usuario_codigo , senha_atual)
        if not valido:
            resposta_estilo('Senha incorreta!')
            return
    nome_completo = input("Novo nome completo: ")
    usuario = input("Novo usuário: ")
    senha = input("Nova senha: ")
    if adm == 'True':
        administrador = (lambda x: x.lower() == 'sim')(input("Administrador (sim/não): "))
        funcionario = not administrador
        clear()
        resposta_estilo(user.alterar_usuario(usuarios, usuario_codigo=usuario_codigo, nome_completo=nome_completo, usuario=usuario, senha=senha, administrador=administrador, funcionario=funcionario))
    else:
        clear()
        resposta_estilo(user.alterar_usuario(usuarios, usuario_codigo=usuario_codigo, nome_completo=nome_completo, usuario=usuario, senha=senha))
        
def inputs_excluir_usuario(usuarios):
    usuario_codigo = input("Digite o nome ou código do usuário a ser excluído: ")
    if not user.validar_existencia_usuario_codigo(usuarios , usuario_codigo):
        resposta_estilo("Usuario não encontrado")
        return
    opcao = input("Realmente deseja exlcuir esse usuario (sim/nao): ")
    clear()
    if opcao.lower() == 'sim':
        resposta_estilo(user.deletar_usuario(usuarios, usuario_codigo))
##Usuario pronto
#------------------------ PRODUTO ------------------------------------------
def menu_produto(produtos , usuarios , usuario_logado):
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
        print('# 5 - Buscar Produto               #')
        print('# 6 - Voltar                       #')
        print('# 0 - Sair                         #')
        print('####################################')
        opcao = input('Opção: ')
        if opcao == '0':
            clear()
            return
        if opcao == '6':
            clear()
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
            listar_produtos(produtos)
        if opcao== '5':
            clear()
            descricao = input('Digite a descricao do produto: ')
            clear()
            resposta_estilo(prod.buscar_produto(produtos , descricao))

def inputs_incluir_produto(produtos):
    descricao = input("Descrição: ")
    if prod.validar_existencia_descricao(produtos , descricao):
        clear()
        resposta_estilo("Produto ja existe")
        return
    unidade = input("Unidade: ")
    preco_custo = input("Preço de custo: ")
    preco_venda = input("Preço de venda: ")
    estoque = input("Quantidade de estoque: ")
    clear()
    resposta_estilo(prod.criar_produto(produtos, descricao, unidade, preco_custo, preco_venda, estoque))

def inputs_alterar_produto(produtos):
    codigo_descricao = input("Digite a descrição ou código do produto a ser alterado: ")
    if not prod.validar_existencia_descricao(produtos , codigo_descricao):
        clear()
        resposta_estilo("Produto não encontrado")
        return
    descricao = input("Descrição: ")
    if prod.validar_existencia_descricao(produtos , descricao):
        clear()
        resposta_estilo("Descrição ja existe")
        return
    unidade = input("Unidade: ")
    preco_custo = input("Preço de custo: ")
    preco_venda = input("Preço de venda: ")
    estoque = input("Quantidade de estoque: ")
    clear()
    resposta_estilo(prod.alterar_produto(produtos, codigo_descricao, descricao=descricao, unidade=unidade, preco_custo=preco_custo, preco_venda=preco_venda, estoque=estoque))

def inputs_excluir_produto(produtos):
    codigo_descricao = input("Digite a descrição ou código do produto a ser excluído: ")
    if not prod.validar_existencia_descricao(produtos , codigo_descricao):
        clear()
        resposta_estilo("Produto não encontrado")
        return
    opcao = input("Realmente deseja exlcuir esse produto (sim/nao): ")
    clear()
    if opcao.lower() == 'sim':
        resposta_estilo(prod.deletar_produto(produtos, codigo_descricao))

def listar_produtos(produtos):
    print("1- ordernar pela descrição")
    print("2- ordernar pelo preço venda")
    opcao = input('Opção: ')
    clear()
    if opcao == '1':
        resposta_estilo(prod.listar_produto(produtos , 'descricao'))
    elif opcao == '2':
        resposta_estilo(prod.listar_produto(produtos , 'preco_venda'))
    else:
        print('Opção invalida')


menu_principal()
