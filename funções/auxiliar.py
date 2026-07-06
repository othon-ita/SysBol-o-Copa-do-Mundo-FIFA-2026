def decisao():
    '''verifica se você está acessando para apostador ou gabarito'''
    escolha = input('''1. Apostador
2. Gabarito

Digite a opção desejada: ''')
    if escolha == '1':
        nome = input('Digite o seu nome: ')
        return f'./apostadores/palpites_{nome}.json'
    elif escolha == '2':
        return 'gabarito.json'