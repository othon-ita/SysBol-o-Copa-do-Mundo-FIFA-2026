#Nome e matrícula dos integrantes do grupo
#André Nicolas de Sousa Vieira - 605925
#Maria Eduarda da Silva Alves - 604390
#Othon Ítalo Nascimento de Moraes - 600006
from funções.segunda_fase.fase_de_32.confronto_direto_fase1 import confronto_direto


def classificacao_fase1(tabela_pontos, nome_arquivo):
    """
    Função que ordena as seleções de cada grupo por pontos, saldo de gols e gols marcados. 
    Se houver empate verifica os confrontos diretos pela função confronto_direto,
    se mesmo assim ainda houver empates, desempata por sorteio.
    """
    
    #ordena por pontos, saldo de gols e gols marcados
    for grupo in tabela_pontos:

        tabela_pontos[grupo] = dict(
            sorted(tabela_pontos[grupo].items(), key=lambda item: (
                    -item[1]["pontos"],
                    -item[1]["saldo_gols"],
                    -item[1]["gols_marcados"]
                )
            )
        )

    #verifica empates
    for grupo in tabela_pontos:

        selecoes = list(tabela_pontos[grupo].items())
        
        #lista com todos os empates de um grupo, por ex: [[Brasil, França], [Espanha, Argentina]]
        todos_empates = []
        #lista com seleções empatadas entre si, ex: [Brasil, França]
        subgrupos_empates = []

        for i in range(len(selecoes) - 1):

            atual = selecoes[i]
            proxima = selecoes[i + 1]

            if (atual[1]["pontos"] == proxima[1]["pontos"] and
                atual[1]["saldo_gols"] == proxima[1]["saldo_gols"] and
                atual[1]["gols_marcados"] == proxima[1]["gols_marcados"]):

                if atual[0] not in subgrupos_empates:
                    subgrupos_empates.append(atual[0])

                if proxima[0] not in subgrupos_empates:
                    subgrupos_empates.append(proxima[0])
            else:
                    #quando sequência de empates acaba e há seleções no subgrupo de empates, elas são adicionadas
                    #à lista todos_empates
                    if len(subgrupos_empates) > 0:
                        todos_empates.append(subgrupos_empates)
                        subgrupos_empates = []

        #caso o grupo termine em seleções empatadas (ex: as duas últimas) adiciona o subgrupo
        #à lista todos_empates após o loop acabar         
        if len(subgrupos_empates) > 0:
                todos_empates.append(subgrupos_empates)


        #desempata as seleções empatadas a partir do confronto direto ou sorteio
        for subgrupo in todos_empates:
            selecoes_desempatadas = confronto_direto(nome_arquivo, grupo, subgrupo)

            #acha onde começa o empate
            for i in range(len(selecoes)):

                if selecoes[i][0] == subgrupo[0]:
                    
                    #reorganiza a tabela
                    for j in range(len(selecoes_desempatadas)):
                        nome = selecoes_desempatadas[j]
                        selecoes[i+j] = (nome, tabela_pontos[grupo][nome])

                    break

        #atualiza a classificação do grupo
        tabela_pontos[grupo] = dict(selecoes)

    return tabela_pontos