import json
from random import randint

"""Esta função preenche aleatoriamente, números de 0 a 7, todas as partidas possíveis em que não hajam palpites definidos por um apostador em específico. Podendo haver palpites de empate somente na fase de grupos, ou seja, primeira fase."""
def preencher_aleatoriamente():
    nome = input('Digite o seu nome:\n')
    with open (f'./apostadores/palpites_{nome}.json', 'r') as arquivo:
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
    with open (f'./apostadores/palpites_{nome}.json', 'w') as arquivo:
        json.dump(leitura, arquivo, indent=4)