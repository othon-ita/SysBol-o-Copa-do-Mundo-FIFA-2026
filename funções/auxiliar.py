def decisao():
    escolha = input('''1. Apostador
2. Gabarito''')
    if escolha == '1':
        nome = input('Digite o seu nome:')
        return f'./apostadores/palpites_{nome}.json'
    elif escolha == '2':
        return './jogos/gabarito.json'