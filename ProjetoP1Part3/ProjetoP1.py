#Projeto de: Anthonyo Pedro de Oliveira Nóbrega
import menus
import filmes
import compras
import cadastros
usuarios = dict()
cadastro_film = dict()
ingressos_comprados = dict()
filmes_comprados = list()
user_ingressos = list()

cadastro_film[32] = ['top gun', 4, 22, 15, 100]
cadastro_film[25] = ['de volta para o futuro', 5, 21, 15, 100]
cadastro_film[77] = ['um tira da pesada', 6, 20, 15, 100]
usuarios['adm'] = ['adm', 2, '777']
usuarios['cliente'] = ['cliente', 1, '777']

while True:
    menus.menu_pricipal()

    opcao_pr_menu = int(input('\nDigite a opcao desejada:'))
    if opcao_pr_menu == 0:
        print('\n\033[7:49:91m-----PROGRAMA ENCERRADO-----\033[m\n')
        break

    elif opcao_pr_menu == 1:
        login = input('Digite seu login:')
        senha = input('Digite sua senha:')
        logado = cadastros.fazer_login(login, senha, usuarios, 2)
        if logado:
            print('\n\033[49:92m!!!Login Efetuado com Sucesso!!!\033[49:92m\n')
            while True:
                menus.menu_ger_filme()

                opcao_ger_menu = int(input('\ndigite a opcao desejada'))

                if opcao_ger_menu == 0:
                    break
                if (opcao_ger_menu == 1):
                    filmes.cadastrar_filme(cadastro_film)

                elif (opcao_ger_menu == 2):
                    filmes.buscar_filme(cadastro_film)

                elif(opcao_ger_menu == 3):
                    filmes.filmes_cadastrados(cadastro_film)

                elif(opcao_ger_menu == 4):
                    filmes.att_filme(cadastro_film)

                elif (opcao_ger_menu == 5):
                    filmes.excluir_filme(cadastro_film)

                elif (opcao_ger_menu == 6):
                    filmes.filmes_vendidos(filmes_comprados)

                elif (opcao_ger_menu == 7):
                    filmes.busc_filme_vendido(filmes_comprados)

                elif (opcao_ger_menu == 8):
                    compras.graficos_filmes(filmes_comprados)

        else:
            print('\n\033[49:91m !!!Cadastro invalido,  verifique seu login e senha!!!\033[m\n')

    elif(opcao_pr_menu == 2):
        login = input('Digite seu login:')
        senha = input('Digite sua senha:')
        logado_cliente = False
        for chave_clientes in usuarios:
            if (chave_clientes == login and usuarios[login][2] == senha and usuarios[login][1] == 1):
                logado_cliente = True
        if logado_cliente:
            print('\n\033[49:92m!!!Login Efetuado com sucesso!!!\033[m\n')

            while True:
              menus.menu_comp_filme()

              opcao_cli_menu = int(input('\nDigite a opcao desejada: '))

              if (opcao_cli_menu == 0):
                  break

              elif (opcao_cli_menu == 1):
                 compras.listar_filmes(cadastro_film)

              elif(opcao_cli_menu == 2):
                  compras.comprar_filme(cadastro_film, ingressos_comprados, login, filmes_comprados, user_ingressos)

              elif (opcao_cli_menu == 3):
                  compras.ingressos_comprados(user_ingressos, login)

        else:
            print('\n\033[49:91m !!!Cadastro invalido,  verifique seu login e senha!!!\033[m\n')

    elif(opcao_pr_menu == 3):
        cadastros.cadastrar(usuarios)