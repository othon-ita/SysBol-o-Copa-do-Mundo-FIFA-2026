from funções.cadastrar_apostador import cadastrar
from funções.limpar import limpar
from funções.carregar_selecoes import carregarSelecoes

while True:
    limpar()
    print ('MENU'.center(30, '='))
    escolha = int(input (
                        '''
1. Carregar Seleções
2. Cadastrar Apostador
3. Registrar Palpites
4. Completar Palpites Aleatoriamente
5. Gerar Próxima Fase
6. Cadastrar Gabarito
7. Consultar Pontuação de Apostador
8. Resultado Final do Bolão
9. Consultar Dados do Sistema
10. Sair

'''
                        ))
    
    if escolha == 1:
        carregarSelecoes()
    if escolha == 2:
        cadastrar()
    if escolha == 0:
        break