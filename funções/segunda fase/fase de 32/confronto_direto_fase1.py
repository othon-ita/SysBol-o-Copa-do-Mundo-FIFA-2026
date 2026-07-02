import json
import random
def confronto_direto(nome_arquivo, grupo, empatadas):
    #as seleções empatadas vão pro parâmetro empatadas ([selecao1, selecao2])

    """
    Função que é chamada na função que gera as classificações da fase 1 caso haja empate em pontos, 
    saldo de gols e gols marcados
    """

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        partidas = json.load(arquivo)

    #procura o confronto entre as seleções empatadas
    for partida in partidas:

        #APENAS PROCURA O GRUPO DAS SELEÇÕES Q TÃO EMPATADAS NO JSON
        if partida["grupo"] != grupo:
            continue

        selecao1 = partida["selecao1"]
        selecao2 = partida["selecao2"]

        if selecao1 in empatadas and selecao2 in empatadas:

            #seleção1 venceu
            if partida["gols1"] > partida["gols2"]:
                return [selecao1, selecao2]

            #seleção2 venceu
            elif partida["gols2"] > partida["gols1"]:
                return [selecao2, selecao1]

            #se ainda tiver empate, vai para o sorteio
            else:
                #retorna o sorteio da seleções empatadas random.shuffle([selecao1, selecao2]) caso ainda haja empate no confronto direto
                random.shuffle(empatadas)
                return empatadas

    #caso não encontre o confronto
    random.shuffle(empatadas)

    #retorna o sorteio da seleções empatadas random.shuffle([selecao1, selecao2]) caso ainda haja empate no confronto direto
    return empatadas