import json
from time import sleep
from funções.consultar_dados.verificar_existencia import verificar_existencia

"""na função cadastrar, é coletado a informação nome, com isso verifica se esse nome já existe no arquivo 'arquivo.txt' 
   se não tem esse nome nesse arquivo, então o programa segui adiante, fazendo um arquivo em json para os palpites do 
   apostador, categorizando eles em 6 partidas para cada grupo, 16 partidas paras os 32 finais, 8 partidas para as   
   oitavas, 4 partidas para as quartas, 2 para as semis, uma para final e adicionando o nome do apostador ao arquivo 
   'apostadores.txt' """

def cadastrar ():
    #referência para organizar os times em grupos 
    gruposLetras = {1 : 'A', 2: 'B', 3 : 'C', 4 : 'D', 5: 'E', 6: 'F', 7: 'G', 8 : 'H', 9 : 'I', 10 : 'J', 11 : 'K', 12: 'L' }
    #verifica se existe o arquivo 'apostadores.txt'
    try:
         #verifica a existência do gabarito
        partidas = verificar_existencia("gabarito","as seleções")
        if partidas == None:
            return
        
        nome = input('Digite o seu nome: ')
        with open ('./apostadores/apostadores.txt', 'r') as arquivo:
            leitura = arquivo.read()
            #verifica a existência no arquivo 'apostadores.txt', caso já exista, aparece a mensagem padrão e volta ao menu principal
            if nome in leitura:
                print('Esse nome ja esta cadastrado!')
                sleep (1)
            else:
                lista = []
                contador = 0
                #organiza as partidas sem os nomes da selecoes em 6 para cada grupo
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
                status = True
                try:  
                    with open (f'./apostadores/palpites_{nome}.json', 'r', encoding = 'utf-8') as arquivo:
                            leitura = json.load(arquivo)
                    for i in leitura:   
                        for j in partidas:
                            if not status:
                                status = True
                                break
                            if (i.get('id') == j.get('id')):
                                status = False
                                i.update({'selecao1' : j.get('selecao1'), 'selecao2' : j.get('selecao2')})
                    with open(f'./apostadores/palpites_{nome}.json', 'w', encoding = 'utf-8') as arquivo:
                        json.dump(leitura, arquivo, indent = 4)
                        print ('Cadastrado com sucesso!')
                        sleep (1)
                except:
                    return
    except FileNotFoundError:
        print("O arquivo de apostadores não existe. Criando um novo... Tente novamente.")
        input("Aperte ENTER para continuar")
        with open('./apostadores/apostadores.txt', 'w') as arquivo:
            arquivo.write("")            
    
    #caso não exista, mensagem padrão aparecera no sistema e criará o arquivo 
    
