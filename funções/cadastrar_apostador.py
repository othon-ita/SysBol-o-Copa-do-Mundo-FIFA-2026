import json
from time import sleep

"""na função cadastrar, é coletado a informação nome, com isso verifica se esse nome já existe no arquivo 'arquivo.txt' 
   se não tem esse nome nesse arquivo, então o programa segui adiante, fazendo um arquivo em json para os palpites do 
   apostador, categorizando eles em 6 partidas para cada grupo, 16 partidas paras os 32 finais, 8 partidas para as   
   oitavas, 4 partidas para as quartas, 2 para as semis, uma para final e adicionando o nome do apostador ao arquivo 
   'apostadores.txt' """

def cadastrar ():
    gruposLetras = {1 : 'A', 2: 'B', 3 : 'C', 4 : 'D', 5: 'E', 6: 'F', 7: 'G', 8 : 'H', 9 : 'I', 10 : 'J', 11 : 'K', 12: 'L' }
    nome = input('''Digite o seu nome: ''')
    with open ('./apostadores/apostadores.txt', 'r') as arquivo:
        leitura = arquivo.read()
        if nome in leitura:
            print('Esse nome ja esta cadastrado!')
            sleep (5)
        else:
            lista = []
            contador = 0
            for  i in range(72):
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
            with open ('./apostadores/apostadores.txt', 'a') as arquivo:
                arquivo.write(f'{nome}\n')     
            with open (f'./apostadores/palpites_{nome}.json ', 'w', encoding = 'utf-8') as arquivo:
                json.dump(lista, arquivo, indent = 4)
                print ('Cadastrado com sucesso!')
                sleep (2)