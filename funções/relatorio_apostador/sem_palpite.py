#Nome e matrícula dos integrantes do grupo
#André Nicolas de Sousa Vieira - 605925
#Maria Eduarda da Silva Alves - 604390
#Othon Ítalo Nascimento de Moraes - 600006
import json
from funções.relatorio_apostador.pontuação_apostador import pontuação_apostador

"""A função sem_palpite(nome) retorna as informações do relatório referentes aos jogos em que o apostador não palpitou sobre. Além disso, a função imprime no terminal este mesmo trecho denotado anteriormente"""
def sem_palpite(nome):
    relatorio = ""
    pontos = pontuação_apostador(nome)
    sem_palpite = pontos[nome]['sem_palpite']
    with open ('gabarito.json', 'r', encoding = 'utf-8') as arquivo:
        gabarito = json.load(arquivo)
    
    print("\n" + 40*"=")
    relatorio += "\n" + (40*"=")
    print("SEM PALPITE")
    relatorio += "\nSEM PALPITE"
    print(40*"=")
    relatorio += "\n" + (40*"=") + "\n"
    
    #Estrutura de repetição para impressão e incremetação do relatório nos diferentes jogos com cumprem os requisitos da função
    for i in sem_palpite['id']:
        print(f"\nJogo {i}")
        relatorio += f"\nJogo {i}"
        for j in gabarito:
            if j.get('id') == i:
                print(f"{j.get('selecao1')} x [{j.get('selecao2')}")
                relatorio += f"\n{j.get('selecao1')} x [{j.get('selecao2')}" + "\n"
                print("\nPalpite não informado.")
                relatorio += "\nPalpite não informado." + "\n"
        
        if i != sem_palpite['id'][-1]:
            print("\n" + 40*"-")
            relatorio += "\n" + (40*"-")
            
    return relatorio