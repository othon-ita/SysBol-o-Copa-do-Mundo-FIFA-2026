import json
import random
#funçao usada na funçao q gera as classificaçoes da fase 1, se houver empate em pontos, saldo de gols e gols marcados essa funçao é usada
def confronto_direto(nome_arquivo, grupo, empatadas):

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        partidas = json.load(arquivo)

    #procura o confronto entre as seleções empatadas
    for partida in partidas:

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
                random.shuffle(empatadas)
                return empatadas

    #caso não encontre o confronto
    random.shuffle(empatadas)

    return empatadas