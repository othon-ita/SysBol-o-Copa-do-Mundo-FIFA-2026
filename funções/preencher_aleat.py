#Nome e matrícula dos integrantes do grupo
#André Nicolas de Sousa Vieira - 605925
#Maria Eduarda da Silva Alves - 604390
#Othon Ítalo Nascimento de Moraes - 600006
import json
from random import randint
from funções.auxiliar import decisao

def preencher_aleatoriamente():
    
    """Esta função preenche aleatoriamente, números de 0 a 7, todas as partidas possíveis em que não hajam palpites definidos por um apostador em específico. Podendo haver palpites de empate somente na fase de grupos, ou seja, primeira fase."""
    
    
    try:
        nome_arquivo = decisao()
        with open (nome_arquivo, 'r', encoding="utf-8") as arquivo:
            leitura = json.load(arquivo)
            
            for i in leitura:
                if (i.get('fase') == 1) and (i.get('gols1') == -1 or i.get('gols2') == -1):
                    if (i.get('gols1') == -1):
                        i['gols1'] = randint(0, 7)
                    if (i.get('gols2') == -1):
                        i['gols2'] = randint(0, 7)
                elif (i.get('fase') != 1) and (i.get('gols1') == -1 or i.get('gols2') == -1):
                    if (i.get('gols1') == -1):
                        while True:
                            i['gols1'] = randint(0, 7)
                            if (i['gols1'] != i['gols2']):
                                break
                    if (i.get('gols2') == -1):
                        while True:
                            i['gols2'] = randint(0, 7)
                            if (i['gols1'] != i['gols2']):
                                break
        with open (nome_arquivo, 'w') as arquivo:
            json.dump(leitura, arquivo, indent=4)
        input("Palpites preenchidos aleatoriamente com sucesso!\nPressione Enter para continuar...")
    except FileNotFoundError:
        input('Desculpe, mas você ainda não está cadastrado no sistema\n Pressione ENTER para continuar...')
        return