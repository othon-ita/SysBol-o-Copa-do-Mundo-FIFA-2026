import json
import random
from funções.auxiliar import decisao
from funções.segunda_fase.fase_de_32.gerar_fase_32 import gerar_fase32

def eliminatorias():

    ordem_chaveamento = []
    partidas = []
    nome_arquivo = decisao()
    num = 0
    condicao = 0
    fase = 0
    id = 0
    #coleta de dados
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        leitura = json.load(arquivo)
    match len(leitura):
        #analisa em qual fase está atualmente
        case 72:
            gerar_fase32(nome_arquivo)
            return
            
        case 88:
            num = 72
            condicao = 'normal'
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
            num = 100
            id = 102
    vencedores = []
    
#Coleta de dados de uma partida, no caso os nome da seleções e gols
     

    for jogo in leitura[num:]:
        gols1 = jogo.get("gols1")
        gols2 = jogo.get("gols2")
        selecao1 = jogo.get("selecao1")
        selecao2 = jogo.get("selecao2")
        if gols1 < 0 or gols2 < 0:
            input('Desculpe, mas você ainda não deu os seus palpites!\nPressione ENTER para continuar')
            return
        elif selecao1 == '' or selecao2 == '':
            input('Desculpe, mas você ainda não carregou as seleções no seu arquivo! \n Pressione ENTER para continuar ')
        #Verifica quem ganhou, no caso de empate, é decidido na sorte (pênaltis)
        if condicao != 'semi':
            if gols1 > gols2:
                vencedores.append(selecao1)
            elif gols2 > gols1:
                vencedores.append(selecao2)
            else:
                vencedores.append(random.choice([selecao1, selecao2]))
        else:
            #após identificar que condicao == 'semi'
            vencedores_semi = []
            perdedores_semi = []

            #Primeiro, separa todos os vencedores e perdedores das duas semis
            for jogo in leitura[num:]:
                s1, s2 = jogo.get("selecao1"), jogo.get("selecao2")
                g1, g2 = jogo.get("gols1"), jogo.get("gols2")
                
                if g1 > g2:
                    vencedores_semi.append(s1)
                    perdedores_semi.append(s2)
                elif g2 > g1:
                    vencedores_semi.append(s2)
                    perdedores_semi.append(s1)
                else:
                    # Empate: decide na sorte
                    escolhido = random.choice([s1, s2])
                    vencedores_semi.append(escolhido)
                    perdedores_semi.append(s2 if escolhido == s1 else s1)

            
            
            partidas.append({
                "id": id + 1,
                "fase": "terceiro lugar",
                "selecao1": perdedores_semi[0],
                "selecao2": perdedores_semi[1],
                "gols1": -1, "gols2": -1
            })

            partidas.append({
                "id": id + 2,
                "fase": "final",
                "selecao1": vencedores_semi[0],
                "selecao2": vencedores_semi[1],
                "gols1": -1, "gols2": -1
            })

            #Salva tudo de uma vez após o loop
            leitura.extend(partidas)
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(leitura, arquivo, indent=4)
            return
        
        
        #Ordem dos chaveamento das oitavas de finals
    if fase == 3:
        ordem_chaveamento = [1, 4, 0, 2, 3, 5, 6, 7, 10, 11, 8, 9, 13, 15, 12, 14]
        mata_mata = 'oitavas de finais'
        #Ordem dos chaveamentos das quartas de finais
    elif fase == 4:
        ordem_chaveamento = [1, 2, 5, 6, 3, 4, 7, 8]
        mata_mata = 'quartas de finais'
        #Ordem dos chaveamentos das semi finais
    elif fase == 5:
        ordem_chaveamento = [1, 2, 3, 4]
        mata_mata = 'semi finais'
        
    if len(leitura) == 72:
        input("Fase de 16 avos gerada com sucesso!\nPressione ENTER para continuar...")
    elif len(leitura[num:]) == 16:
        input("Fase de oitavas gerada com sucesso!\nPressione ENTER para continuar...")
    elif len(leitura[num:]) == 8:
        input("Fase de quartas gerada com sucesso!\nPressione ENTER para continuar...")
    elif len(leitura[num:]) == 4:
        input("Fase de semifinais gerada com sucesso!\nPressione ENTER para continuar...")
    elif len(leitura) == 102:
        input("Fase final e terceiro lugar gerada com sucesso!\nPressione ENTER para continuar...")
        
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
    