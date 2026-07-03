import json
import random
from funções.auxiliar import decisao
from funções.segunda_fase.fase_de_32.gerar_fase_32 import gerar_fase32

def eliminatorias():
    ordem_chaveamento = []
    partidas = []
    nome_arquivo = decisao()
    
   #coleta de dados
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        leitura = json.load(arquivo)
    match len(leitura):
        
        case 72:
            gerar_fase32(nome_arquivo)
            return
            
        case 88:
            num = 72
            condicao = 'nomal'
            fase = 3
            id = 88
        case 96:
            num = 88
            condicao = 'normal'
            fase = 4
            id = 96
        case 100:
            condicao = 'normal'
            num = 96
            fase = 5
            id = 100
        case 102:
            condicao = 'semi'
            id = 102
    vencedores = []
    
   #Coleta de dados de uma partida, no caso os nome da seleções e gols
    for jogo in leitura[num:]:
        gols1 = jogo.get("gols1")
        gols2 = jogo.get("gols2")
        selecao1 = jogo.get("selecao1")
        selecao2 = jogo.get("selecao2")
        #Verifica quem ganhou, no caso de empate, é decidido na sorte (pênaltis)
        if condicao != 'semi':
            if gols1 > gols2:
                vencedores.append(selecao1)
            elif gols2 > gols1:
                vencedores.append(selecao2)
            else:
                vencedores.append(random.choice([selecao1, selecao2]))
        else:
            times = []
            if gols1 > gols2:
                times.append(selecao1)
                times.append(selecao2)
            elif gols2 > gols1:
                times.append(selecao2)
                times.append(selecao1)
            else:
                times.append(random.choice([selecao1, selecao2]))
                times.append(selecao2 if times[0] == selecao1 else selecao1 )
            for i in range(2):
                #Garante que tenha o par para formar a partida
                if i + 1 < len(vencedores_ordenados):
                    partidas.append({"id": '',
                    "fase": "",
                    "selecao1": times[i],
                    "selecao2": times[i+1],
                    "gols1": -1,
                    "gols2": -1 } )                             
            leitura.extend(partidas)
            with open (nome_arquivo, 'w', encoding = 'utf-8') as arquivo:
                json.dump(leitura, arquivo, indent = 4 )
           
   #Ordem dos chaveamento das oitavas de finals
    if fase == 3:
        ordem_chaveamento = [1, 4, 0, 2, 3, 5, 6, 7, 10, 11, 8, 9, 13, 15, 12, 14]
        mata_mata = 'oitavas de finais'
        #Ordem dos chaveamentos das quartas de finais
    elif fase == 4:
        ordem_chaveamento = [1, 2, 3, 4]
        mata_mata = 'quartas de finais'
        #Ordem dos chaveamentos das semi finais
    elif fase == 5:
        ordem_chaveamento = [1, 2]
        mata_mata = 'semi finais'
    
     
    #Cria uma lista com base na ordem de chaveamento (Garante que só tenta buscar se existirem)
    vencedores_ordenados = [vencedores[i-1] for i in ordem_chaveamento if (i-1) < len(vencedores)]
    conta = 0
    #Agrupamento dos jogos em duplas
    for i in range(0, len(vencedores_ordenados), 2):
        #Garante que tenha o par para formar a partida
        conta += 1
        if i + 1 < len(vencedores_ordenados):
            partidas.append({"id": (id + conta),
            "fase": mata_mata,
            "selecao1": vencedores_ordenados[i],
            "selecao2": vencedores_ordenados[i+1],
            "gols1": -1,
            "gols2": -1 } )                             
    leitura.extend(partidas)
    with open (nome_arquivo, 'w', encoding = 'utf-8') as arquivo:
        json.dump(leitura, arquivo, indent = 4 )
    return partidas
    