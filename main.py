from funções.cadastrar_apostador import cadastrar
from funções.limpar import limpar

while True:
    limpar()
    print ('MENU'.center(30, '='))
    escolha = int(input ('''[1] cadastrar apostador
                            [0] sair
                        '''))
    
    if escolha == 1:
        cadastrar()
    if escolha == 0:
        break