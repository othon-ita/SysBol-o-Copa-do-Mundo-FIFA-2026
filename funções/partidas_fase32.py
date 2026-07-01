import json
#a partir das classificações dos grupos, gera as partidas da fase de 32

def partidas_fase32(tabela_pontos):

    classificados = []
    terceiros = []

    #separa os classificados
    for grupo in tabela_pontos:

        selecoes = list(tabela_pontos[grupo]["selecoes"].items())

        classificados.append(selecoes[0])
        classificados.append(selecoes[1])

        terceiros.append(selecoes[2])

    # ordena os terceiros
    terceiros.sort(key=lambda item:(
            -item[1]["pontos"],
            -item[1]["saldo_gols"],
            -item[1]["gols_marcados"]
        )
    )

    #adiciona os 8 melhores terceiros
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