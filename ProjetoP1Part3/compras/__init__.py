import matplotlib.pyplot as plt
def listar_filmes(cadastro_film):
    print('\n\033[7:49:37m-----Filmes em Cartaz-----\n\033[m')
    for chave in cadastro_film:
        print(
            f'filme: {cadastro_film[chave][0]}, Sala: {cadastro_film[chave][1]} , Horario: {cadastro_film[chave][2]}h ,Ingressos: {cadastro_film[chave][4]} ,Valor: {cadastro_film[chave][3]}R$ \n')

def comprar_filme(cadastro_film,ingressos_comprados,login,filmes_comprados,user_ingressos):
    print('\n\033[7:49:37m-----Comprar Ingressos----\033[m\n')
    for chave in cadastro_film:
        print(f'Codigo:{chave} - filme: {cadastro_film[chave][0]}, sala: {cadastro_film[chave][1]} , horario: {cadastro_film[chave][2]}h , valor: {cadastro_film[chave][3]}R$ , ingressos: {cadastro_film[chave][4]}\n')
    cod_filme_desej = int(input('Digite o Cod do filme que deseja comprar:'))

    if cod_filme_desej in cadastro_film:
        qte_ingressos_desej = int(input(f'Digite a quantidade de Ingressos do filme {cadastro_film[cod_filme_desej][0]} que deseja comprar:'))
        while (qte_ingressos_desej > cadastro_film[cod_filme_desej][4]):
            print('\n\033[49:91mQuantidade de ingressos indisponivel!\033[m')
            print(f'\n\033[49:92mDisponivel {cadastro_film[cod_filme_desej][4]} ingressos!')
            qte_ingressos_desej = int(input(f'Digite a quantidade de Ingressos do filme {cadastro_film[cod_filme_desej][0]} que deseja comprar:'))
        cadastro_film[cod_filme_desej][4] = cadastro_film[cod_filme_desej][4] - qte_ingressos_desej
        ingressos_comprados[login] = {'filme': cadastro_film[cod_filme_desej][0], 'qteing': qte_ingressos_desej,'hora': cadastro_film[cod_filme_desej][2],'sala': cadastro_film[cod_filme_desej][1], 'cod': cadastro_film[cod_filme_desej]}
        filmes_comprados.append({'filme': cadastro_film[cod_filme_desej][0], 'qteing': qte_ingressos_desej})
        user_ingressos.append({'login': login, 'filme': cadastro_film[cod_filme_desej][0], 'qteing': qte_ingressos_desej,'hora': cadastro_film[cod_filme_desej][2], 'sala': cadastro_film[cod_filme_desej][1],'cod': cadastro_film[cod_filme_desej]})
        with open('listar_filmes.txt', 'a') as arquivo:
            arquivo.write(' Filme: ' + str(cadastro_film[cod_filme_desej][0]) +' - ' + 'Ingressos:' + str(qte_ingressos_desej) + ' ' + 'Hora: '+ str(cadastro_film[cod_filme_desej][2]) + ' sala: ' + str(cadastro_film[cod_filme_desej][1])+'\n')


        nome_arq = login +'.txt'
        with open(nome_arq,'a') as arq:
            arq.write(' Filme: ' + str(cadastro_film[cod_filme_desej][0]) +' - ' + 'Ingressos:' + str(qte_ingressos_desej) + ' ' +'Hora: '+ str(cadastro_film[cod_filme_desej][2]) + ' ' 'sala: ' + str(cadastro_film[cod_filme_desej][1])+'\n')

        print('\n\033[49:92m!!!INGRESSO COMPRADO COM SUCESSO!!!\033[m')

    else:
        print('\n\033[49:91m!!!CODIGO INVALIDO!!!\033[m')

def ingressos_comprados(user_ingressos, login):
    print('\n\033[7:49:37m-----Ingressos Comprados-----\033[m\n')
    for i in range(len(user_ingressos)):
        if login in user_ingressos[i]["login"]:
            print(f'Filme: {user_ingressos[i]["filme"]}, Ingressos: {user_ingressos[i]["qteing"]}')

def graficos_filmes(filmes_comprados):
    plt.figure(figsize=(5, 5))
    filmes = [film['filme'] for film in filmes_comprados]
    ingressos = [ing['qteing'] for ing in filmes_comprados]

    plt.bar(filmes, ingressos, color='red')
    plt.title('Ingressos Vendidos por Filme')
    plt.xlabel('Filme')
    plt.ylabel('Ingressos Vendidos')
    plt.show()





