import usuarios as user
import produtos as prod

usuarios = user.carregar_usuarios()
produtos = prod.carregar_produtos()

def menu_principal(usuarios):
    while True:
        print('Sistema de Gestão')
        print('Escolha uma opção')
        print('1 - entrar no sistema')
        print('0 - sair')
        opcao = input('Opção: ')
        if opcao == '0':
            return
        if opcao == '1':
            usuario = input('Usuario: ')
            senha = input('Senha: ')
            if user.login(usuarios , usuario , senha):
                print('Login efetuado com sucesso')
                return sub_menu(usuarios)
            print('Usuario ou senha incorretos')
            return
        
        
def sub_menu(usuarios):
    print('1 - Manutenção de Usuarios')
    print('2 - Manutenção de Produtos')
    print('0 - sair')
    opcao = input('Opção: ')

    if opcao == '0':
        return
    
    if opcao == '1':
        return menu_usuario(usuarios)
    

def menu_usuario(usuarios):
    print('1 - Incluir Usuario')
    print('2 - Alterar Usuario')
    print('3 - Exluir Usuario')
    print('4 - Listar Usuario')
    print('5 - voltar')
    print('0 - sair')
    opcao = input('Opção: ')

    if opcao == '0':
        return
    if opcao == '5':
        return sub_menu(usuarios)
    
    if opcao == '1':
        nome_completo = input("Nome completo: ")
        usuario = input("usuario: ")
        senha = input("senha : ")
        administrador = (lambda adm:adm.lower() == 'sim')(input("administrador (sim/nao): "))
        funcionario = (lambda administrador: administrador == False)(administrador)
        user.criar_usuario(usuarios,nome_completo,usuario,senha,administrador,funcionario)

    if opcao == '2':
        print('Digite o nome ou codigo do usuario a ser alterado: ')
        nome_codigo = input("Usuario: ")
        print('Digite a senha atual do usuario ou uma senha de qualquer usuario ADM')
        senha_atual = input("Senha: ")
        if user.validar_senha_adm(usuarios ,  senha_atual) and user.validar_usuario_codigo(usuarios , nome_codigo):
            nome_completo = input("Novo nome completo: ")
            usuario = input("Novo usuario: ")
            senha = input("Nova senha : ")
            if user.validar_senha_adm(usuarios ,  senha_atual):
                administrador = (lambda adm:adm.lower() == 'sim')(input("administrador (sim/nao): "))
                funcionario = (lambda administrador: administrador == False)(administrador)
                user.alterar_usuario(usuarios,nome_codigo=nome_codigo,nome_completo=nome_completo,usuario=usuario,senha=senha,administrador=administrador,funcionario=funcionario)
            else:
                user.alterar_usuario(usuarios,nome_codigo=nome_codigo,nome_completo=nome_completo,usuario=usuario,senha=senha)


    if opcao == '3':
        print('Digite o nome ou codigo do usuario a ser alterado: ')
        nome_codigo = input("Usuario: ")
        print('Para confirmar a exclusão digite uma senha de ADM:')
        senha_adm = input('senha: ')
        if user.validar_senha_adm(usuarios ,  senha_adm):
            user.deletar_usuario(usuarios, nome_codigo)

    if opcao == '4':
        user.listar_usuarios(usuarios)

menu_principal(usuarios)