def cadastrar(usuarios):
    print('\n\033[7:49:37m--------------CADASTRO DO USUARIO e ADMINISTRADOR---------------\033[m\n')
    nome = input('Digite seu nome:')
    login = input('Digite seu login:')
    for chave_login in usuarios:
        while chave_login == login:
            print(f'\033[49:91mO login [{login}] ja existe , insira um novo login!\033[m')
            login = input('Digite seu login:')

    senha = input('Digite sua senha:')
    confir_senha = input('confirme sua senha:')

    while (senha != confir_senha):
        print('\n\033[49:91mSENHAS DIFERENTES\033[m')
        senha = input('Digite sua senha:')
        confir_senha = input('confirme sua senha:')
    perfil = int(input('Digite 1 para Cliente e Digite 2 para Administrador:'))
    while (perfil > 2):
        print('\n\033[49:91m!!!PERFIL INVALIDO , DIGITE NOVAMENTE!!!\033[m\n')
        perfil = int(input('Digite 1 para Cliente e Digite 2 para Administrador:'))
    usuarios[login] = [nome, perfil, senha]
    print('\n\033[49:92m!!!Cadastro realizado com sucesso!!!\n')

def fazer_login(login, senha, user , tipo):
    for chave_clientes in user:
        if (chave_clientes == login and user[login][2] == senha and user[login][1] == tipo):
            return True
        return False
