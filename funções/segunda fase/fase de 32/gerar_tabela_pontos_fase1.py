import json

def gerar_tabela_pontos_fase1(nome_arquivo):
    """
    Contabiliza os pontos, saldo de gols e gols marcados de cada seleção na fase 1
    """
    tabela_pontos = {}
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        partidas = json.load(arquivo)

        for partida in partidas:

            #coloca os grupos no dicionário tabela_pontos
            grupo_nome = partida["grupo"]

            #verifica se o grupo já tá no dicionário
            if grupo_nome not in tabela_pontos:
                tabela_pontos[grupo_nome] = {
                    "selecoes": {}
                }

            #só pra n ter q ficar repetindo tabela_pontos[grupo_nome] nas linhas abaixo
            grupo = tabela_pontos[grupo_nome]

            #verifica se a seleção tá no dicionário ou não
            if partida["selecao1"] not in grupo["selecoes"]:
                #adiciona ela na chave "seleçoes" do grupo
                grupo["selecoes"][partida["selecao1"]] = {
                    "pontos": 0,
                    "saldo_gols": 0,
                    "gols_marcados": 0
                }

            #mesma coisa
            if partida["selecao2"] not in grupo["selecoes"]:
                grupo["selecoes"][partida["selecao2"]] = {
                    "pontos": 0,
                    "saldo_gols": 0,
                    "gols_marcados": 0
                }


            #CONTAGEM DOS PONTOS
            #VITÓRIA OU EMPATE (3 PONTOS OU 1 PONTO)
            if partida["gols1"] > partida["gols2"]:
                grupo["selecoes"][partida["selecao1"]]["pontos"] += 3

            elif partida["gols1"] < partida["gols2"]:
                grupo["selecoes"][partida["selecao2"]]["pontos"] += 3

            else:
                grupo["selecoes"][partida["selecao1"]]["pontos"] += 1
                grupo["selecoes"][partida["selecao2"]]["pontos"] += 1

            #GOLS MARCADOS
            grupo["selecoes"][partida["selecao1"]]["gols_marcados"] += partida["gols1"]
            grupo["selecoes"][partida["selecao2"]]["gols_marcados"] += partida["gols2"]


            #SALDO DE GOLS
            grupo["selecoes"][partida["selecao1"]]["saldo_gols"] += partida["gols1"] - partida["gols2"]
            grupo["selecoes"][partida["selecao2"]]["saldo_gols"] += partida["gols2"] - partida["gols1"]

    return tabela_pontos