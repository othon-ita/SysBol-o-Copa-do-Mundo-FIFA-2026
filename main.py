from funções.cadastrar_apostador import cadastrar
from funções.limpar import limpar
from funções.carregar_selecoes import carregarSelecoes
from funções.cadastrar_palpites import cadastrar_palpites
from funções.preencher_aleat import preencher_aleatoriamente
from funções.consultar_dados.consultar_dados import consultar_dados
from funções.eliminatorias import eliminatorias
from funções.cadastrar_gabarito import cadastrar_gabarito
from funções.relatorio_apostador.relatorio_apostador import relatorio_apostador
from funções.resultado_final import resultado_final

while True:
    """O arquivo 'main' é responsável por implementar o menu principal do sistema, permitindo ao usuário escolher entre diferentes opções, como; carregar as seleções, cadastrar apostadores, registrar palpites, completar palpites aleatoriamente, gerar a próxima fase, cadastrar gabarito, consultar pontuação de apostador, resultado final do bolão e consultar dados do sistema. O menu é exibido em um loop contínuo até que o usuário escolha a opção de sair."""
    
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

Digite a opção desejada: '''
                        ))
    
    if escolha == 1:
        carregarSelecoes()
    elif escolha == 2:
        cadastrar()
    elif escolha == 3:
        cadastrar_palpites()
    elif escolha == 4:
        preencher_aleatoriamente()
    elif escolha == 5:
        eliminatorias()
    elif escolha == 6:
        cadastrar_gabarito()
    elif escolha == 7:
        relatorio_apostador()
    elif escolha == 8:
        resultado_final()
    elif escolha == 9:
        consultar_dados()
    elif escolha == 10:
        break
