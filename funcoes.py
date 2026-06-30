import os
import json
from time import sleep


"""na função cadastrar, é coletado a informação nome, com isso verifica se esse nome já existe no arquivo 'arquivo.txt' 
   se não tem esse nome nesse arquivo, então o programa segui adiante, fazendo um arquivo em json para os palpites do 
   apostador, categorizando eles em 6 partidas para cada grupo, 16 partidas paras os 32 finais, 8 partidas para as   
   oitavas, 4 partidas para as quartas, 2 para as semis, uma para final e adicionando o nome do apostador ao arquivo 
   'apostadores.txt' """
def cadastrar ():
    gruposLetras = {
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
                "id": i + 1,
                "fase": 1,
                "grupo": gruposLetras[contador],
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
"""na função registrar, existem dois modos, interativo, na qual o usuário terá um menu na qual escolher entre 3 opções para seguir, listar todoso os jogos, listar apenas os sem 
   palpites ou cadastrar ou alterar o placar de um jogo, dentro dessa última funcionalidade o usuário deverá digitar o id do jogo que quer 
   alterar ou cadastrar, o outro modo é o em lote... (volte aqui para adicionar mais)"""


def registrar(escolha2, partidas):
    lista = []
    jogos = []
    status = True
    nome = input('Digite o seu nome:\n')
    with open (f'palpites_{nome}.json', 'r', encoding = 'utf-8') as arquivo:
                    leitura = json.load(arquivo)
    if (not leitura[71].get('selecao1')) or (not leitura[71].get('selecao2')):
        try:
            for i in leitura:   
                for j in partidas:
                    if not status:
                        status = True
                        break
                    if (i.get('id') == j.get('id')):
                        status = False
                        i.update({'selecao1' : j.get('selecao1'), 'selecao2' : j.get('selecao2')})
            with open(f'palpites_{nome}.json', 'w', encoding = 'utf-8') as arquivo:
                json.dump(leitura, arquivo, indent = 4)
        except TypeError:
            print('ops! voce esqueceu de carregar as selecoes, volte aqui mais tarde ;)')
            sleep(2)
            return
        
        
    if escolha2 == 1:

        while True:
            limpar()
            escolha3 = int (input('''--------------------------------------------
[1] listar todos os jogos do bolão
[2] listar apenas jogos sem palpite
[3] cadastrar ou alterar o placar de um jogo
[0] sair
'''))

            match escolha3:
                case 1:
                    for i in leitura:
                        print(f'{i}\n')
                    espera = input ()
                case 2:
                    for i in leitura:
                        if i.get('gols1') == -1 and i.get('gols1') == -1:
                            print (f'{i}\n')
                    espera = input()
                case 3:
                    escolha4 = int(input('--------------------------------------------\nqual id do jogo que desejar cadastrar ou alterar o placar:'))
                    for i in leitura:
                        if i.get('id') == escolha4:
                            print(i)
                    gols1 = int(input('digite a quantidade de gols para primeira selecao:'))
                    gols2 = int(input('digite a quantidade de gols para segunda selecao:'))

                    for i in leitura:
                        if i.get ('id') == escolha4:
                            i.update({'gols1': gols1, 'gols2' : gols2})

                    with open (f'palpites_{nome}.json ', 'w', encoding = 'utf-8') as arquivo:
                        json.dump(leitura, arquivo, indent = 4)
                case 0 : 
                    break