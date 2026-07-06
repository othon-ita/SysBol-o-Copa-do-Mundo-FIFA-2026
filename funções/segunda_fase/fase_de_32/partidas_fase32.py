#Nome e matrícula dos integrantes do grupo
#André Nicolas de Sousa Vieira - 605925
#Maria Eduarda da Silva Alves - 604390
#Othon Ítalo Nascimento de Moraes - 600006
import json
#a partir das classificações dos grupos, gera as partidas da fase de 32

def partidas_fase32(tabela_pontos):
    """
    Separa o primeiro e segundo colocado de cada grupo, assim como os 8 melhores terceiros no geral, ordenando-os e
    gera partidas com base na classificação das seleções, como o exemplo abaixo:
    J73: 1º melhor classificado x 32º melhor classificado
    J74: 2º melhor classificado x 31º melhor classificado
    J75: 3º melhor classificado x 30º melhor classificado
    ...
    J88: 16º melhor classificado x 17º melhor classificado
    
    """
    classificados = []
    terceiros = []

    #separa os classificados
    for grupo in tabela_pontos:

        #.items pega o par chave (nome da seleção) valor (pontos, saldo de gols e gols marcados)
        selecoes = list(tabela_pontos[grupo].items())
        #pega o primeiro e segundo lugar, lembrando q os grupos já estão ordenados
        classificados.append(selecoes[0])
        classificados.append(selecoes[1])

        #pega o terceiro
        terceiros.append(selecoes[2])

    #ordena os terceiros
    terceiros.sort(key=lambda item:(
            -item[1]["pontos"],
            -item[1]["saldo_gols"],
            -item[1]["gols_marcados"]
        )
    )

    #adiciona os 8 melhores terceiros
    #.extend adiciona os elementos de uma lista no final de outra
    classificados.extend(terceiros[:8])

    #classificação geral dos 32 classificados
    classificados.sort(key=lambda item:(
            -item[1]["pontos"],
            -item[1]["saldo_gols"],
            -item[1]["gols_marcados"]
        )
    )

    #gera as partidas da fase de 32
    partidas_fase32 = []

    for i in range(16):

        partidas_fase32.append({
            "id": 73 + i,
            "fase": "fase de 32",
            "selecao1": classificados[i][0],
            "selecao2": classificados[31 - i][0],
            "gols1": -1,
            "gols2": -1
        })

    return partidas_fase32