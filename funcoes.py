import os
import json
from time import sleep
def cadastrar ():
    grupos = {
    1 : 'A', 2: 'B', 3 : 'C', 4 : 'D', 5: 'E', 6: 'F', 7: 'G', 8 : 'H', 9 : 'I', 10 : 'J', 11 : 'K', 12: 'L' 

    }
    nome = input('''
------Digite o seu nome:''')
    with open ('apostadores.txt', 'r') as arquivo:
        leitura = arquivo.read()
        if nome in leitura:
            print('Esse nome ja esta cadastrado')
            sleep (2)
        else:
            lista = []
            contador = 0
            for  i in range(72):
                if contador < 13:
                    if i % 6 == 0:
                        contador += 1
                dados = {
                "id": i,
                "fase": 1,
                "grupo": grupos[contador],
                "selecao1": "",
                "selecao2": "",
                "gols1": -1, 
                "gols2": -1
                }
                lista.append(dados)
                conta = 0
                fasev2 = 1
            for i in range (31):
                id = 72 + i
                match fasev2:
                    case 1:
                        fase = 'fase de 32'
                        if (i + 1) % 16 == 0: 
                            fasev2 += 1  
                    case 2:
                        fase = 'oitavas'
                        if (i + 1 )% 8 == 0: 
                            fasev2 += 1  
                    case 3:
                        fase = 'quartas'
                        if (i + 1) % 4 == 0 :
                            fasev2 += 1  
                    case 4:
                        fase = 'semi finais'
                        if (i + 1) % 2 == 0:
                            fasev2 += 1  
                    case 5:
                        if (i + 1) == 31 :
                            fase = 'final'
                            
                dados = {
                "id": id ,
                "fase": fase,
                "selecao1": "",
                "selecao2": "",
                "gols1": -1, 
                "gols2": -1
                }
                lista.append(dados)
            with open ('apostadores.txt', 'a') as arquivo:
                arquivo.write(f'{nome}\n')     
            with open (f'palpites_{nome}.json ', 'w', encoding = 'utf-8') as arquivo:
                json.dump(lista, arquivo, indent = 4)
                print ('cadastrado com sucesso!')
                sleep (2)
def limpar():
    os.system ('cls')