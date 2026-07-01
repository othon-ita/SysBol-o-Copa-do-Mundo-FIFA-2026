from funcoes import cadastrar, limpar, registrar
from carregarSelecoes import carregarSelecoes
from time import sleep
grupos = {}
status = False
partidas = None



while True:
    limpar()
    print ('MENU'.center(30, '='))
    escolha = int(input ('''[1] cadastrar apostador
[2] registrar palpite
[3] carregar selecoes
[4] sair
'''))
    match escolha:

        case 1:
            cadastrar()

        case 2:
            limpar()
            print(70 * '-')
        
            registrar(partidas)
        case 3:
            grupos, status, partidas = carregarSelecoes()
            for i in grupos.items():
                print(f'{i}\n')
            espera = input()
            print('Fase de grupos'.center(100, '='))
            for i in partidas:
                print(f'{i}\n')
            espera = input()
        case 0:
            break 