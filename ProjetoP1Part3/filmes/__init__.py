def cadastrar_filme(cadastro_film):
    print('\n\033[7:49:37m--------Cadastrar Filme--------\033[m\n')

    cod_filme = int(input('Digite um codigo para o filme:'))
    for chave_filmes in cadastro_film:
        while chave_filmes == cod_filme:
            print(f' codigo [{chave_filmes}] ja existe , insira um novo codigo!')
            cod_filme = int(input('Digite um codigo para o filme:'))

    nome_film = input('Digite o nome do filme:')

    sala_film = int(input('Digite a sala do filme:'))
    for chave_filmes in cadastro_film:
        while cadastro_film[chave_filmes][1] == sala_film:
            print(f'A sala [{cadastro_film[chave_filmes][1]}] ja esta ocupada , insira uma nova sala!')
            sala_film = int(input('Digite a sala do filme:'))

    hora_film = float(input('Digite o horario do filme:'))
    valor_film = int(input('digite o valor do filme:'))
    qte_ingressos = int(input('Digite a quantidade de ingressos:'))

    cadastro_film[cod_filme] = [nome_film, sala_film, hora_film, valor_film, qte_ingressos]
    print('\n\033[49:92m!!!Filme cadastrado com sucesso!!!\033[49:92m\n')

def buscar_filme(cadastro_film):
    print('\n\033[7:49:37m--------Buscar Filme--------\033[m\n')
    buscar = input('Digite qual filme quer buscar:')
    for chave in cadastro_film:
        if (buscar in cadastro_film[chave][0]):
            print(f'Filme: {cadastro_film[chave][0]}, Sala: {cadastro_film[chave][1]} , Horario: {cadastro_film[chave][2]}h , Valor: {cadastro_film[chave][3]}R$ , Ingressos: {cadastro_film[chave][4]}\n')

def filmes_cadastrados(cadastro_film):
    print('\n\033[7:49:37m------Filmes Cadastrados------\033[m\n')

    for chave in cadastro_film:
        print(f'filme: {cadastro_film[chave][0]}, sala: {cadastro_film[chave][1]} , Horario: {cadastro_film[chave][2]}h , valor: {cadastro_film[chave][3]}R$, Ingressos: {cadastro_film[chave][4]} \n')

def att_filme(cadastro_film):
    print('\n\033[7:49:37m------Atualizar Filme------\033[m\n')

    for chave in cadastro_film:
        print(f'Cod: {chave}, Filme: {cadastro_film[chave][0]}, Sala: {cadastro_film[chave][1]} , Horario: {cadastro_film[chave][2]}h , Valor: {cadastro_film[chave][3]}R$ , Ingressos: {cadastro_film[chave][4]} \n')

    cod = int(input('Infome o codigo do filme que deseja atualizar:'))
    nome_film = input('Digite o nome do filme:')
    sala_film = int(input('Digite a sala do filme:'))
    for chave_filmes in cadastro_film:
        while cadastro_film[chave_filmes][1] == sala_film:
            print(f'A sala [{cadastro_film[chave_filmes][1]}] ja esta ocupada , insira uma nova sala!')
            sala_film = int(input('Digite a sala do filme:'))

    hora_film = int(input('Digite o horario do filme:'))
    valor_film = int(input('Digite o valor do filme:'))
    qte_ingressos = int(input('Digite a quantidade de ingressos:'))
    cadastro_film[cod][0] = nome_film
    cadastro_film[cod][1] = sala_film
    cadastro_film[cod][2] = hora_film
    cadastro_film[cod][3] = valor_film
    cadastro_film[cod][4] = qte_ingressos
    print('\n\033[49:92m!!!Filme Atualizado com Sucesso!!!\033[49:92m\n')


def excluir_filme(cadastro_film):
    print('\n\033[7:49:37m--------Excluir Filme--------\033[m\n')
    busca = input('Digite o filme o nome do filme:')
    for chave in cadastro_film:
        if busca in cadastro_film[chave][0]:
            print(f'\n{chave} - {cadastro_film[chave][0]}')
    sala_rem = int(input('\nDigite o codigo do filme que deseja remover:'))
    if sala_rem in cadastro_film:
        cadastro_film.pop(sala_rem)
        print('\n\033[49:92m!!! Filme excluido com sucesso !!!\033[m\n')
    else:
        print('\n \033[49:91mCodigo invalido!!!\033[m')

def filmes_vendidos(filmes_comprados):
    print('\n\033[7:49:37m-----Filmes Vendidos-----\033[m\n')
    for i in range(len(filmes_comprados)):
        print(f'{filmes_comprados[i]["filme"]} - ingressos vendidos: {filmes_comprados[i]["qteing"]}\n')

def busc_filme_vendido(filmes_comprados):
    print('\n\033[7:49:37m--------Buscar Filme--------\033[m\n')
    buscar = input('Digite qual filme quer buscar:')
    for i in range(len(filmes_comprados)):
        if filmes_comprados[i]["filme"].count(buscar):
            print(f'{filmes_comprados[i]["filme"]} - ingressos vendidos: {filmes_comprados[i]["qteing"]}')
        else:
            print('\n \033[49:91m!!!Filme nao cadastrado ou nao vendeu ingressos!!!\033[m')


