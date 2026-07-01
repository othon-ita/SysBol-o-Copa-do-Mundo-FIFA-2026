from confronto_direto_fase1 import confronto_direto

#funçao q ordena as seleções de cada grupo por pontos, saldo de gols e gols marcados. se houver empate verifica os confrontos 
#diretos, se msm assim ainda houver empates, desempata por sorteio

def classificacao_fase1(tabela_pontos, nome_arquivo):

    #ordena por pontos, saldo de gols e gols marcados
    for grupo in tabela_pontos:

        tabela_pontos[grupo]["selecoes"] = dict(
            sorted(tabela_pontos[grupo]["selecoes"].items(), key=lambda item: (
                    -item[1]["pontos"],
                    -item[1]["saldo_gols"],
                    -item[1]["gols_marcados"]
                )
            )
        )

    #verifica empates
    for grupo in tabela_pontos:

        selecoes = list(tabela_pontos[grupo]["selecoes"].items())

        for i in range(len(selecoes) - 1):

            atual = selecoes[i]
            proxima = selecoes[i + 1]

            if (atual[1]["pontos"] == proxima[1]["pontos"] and
                atual[1]["saldo_gols"] == proxima[1]["saldo_gols"] and
                atual[1]["gols_marcados"] == proxima[1]["gols_marcados"]):

                classificacao = confronto_direto(nome_arquivo, grupo, [atual[0], proxima[0]])

                #se o confronto direto indicar que a próxima deve ficar na frente, troca as duas de posição
                if classificacao[0] == proxima[0]:
                    selecoes[i], selecoes[i + 1] = selecoes[i + 1], selecoes[i]

        #atualiza a classificação do grupo
        tabela_pontos[grupo]["selecoes"] = dict(selecoes)

    return tabela_pontos