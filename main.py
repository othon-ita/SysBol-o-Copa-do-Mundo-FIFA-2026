from funcoes import cadastrar, limpar, registrar

while True:
    limpar()
    print ('MENU'.center(30, '='))
    escolha = int(input ('''[1] cadastrar apostador
[2] registrar palpite
[0] sair
'''))
    if escolha == 1:
        cadastrar()
    elif escolha == 2:
        limpar()
        print(30 * '-')
        escolha2 = int(input ("""[1] modo interativo
[2] modo em lote
"""))
        registrar(escolha2)
    if escolha == 0:
        break