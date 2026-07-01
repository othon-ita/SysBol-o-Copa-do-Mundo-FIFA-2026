import json
#gera a tabela de pontos da fase1, sem ordernar
def gerar_tabela_pontos_fase1(nome_arquivo):
    tabela_pontos = {}

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        partidas = json.load(arquivo)

        for partida in partidas:

            grupo_nome = partida["grupo"]

            if grupo_nome not in tabela_pontos:
                tabela_pontos[grupo_nome] = {
                    "selecoes": {}
                }

            grupo = tabela_pontos[grupo_nome]


            if partida["selecao1"] not in grupo["selecoes"]:
                grupo["selecoes"][partida["selecao1"]] = {
                    "pontos": 0,
                    "saldo_gols": 0,
                    "gols_marcados": 0
                }

            if partida["selecao2"] not in grupo["selecoes"]:
                grupo["selecoes"][partida["selecao2"]] = {
                    "pontos": 0,
                    "saldo_gols": 0,
                    "gols_marcados": 0
                }

            if partida["gols1"] > partida["gols2"]:
                grupo["selecoes"][partida["selecao1"]]["pontos"] += 3

            elif partida["gols1"] < partida["gols2"]:
                grupo["selecoes"][partida["selecao2"]]["pontos"] += 3

            else:
                grupo["selecoes"][partida["selecao1"]]["pontos"] += 1
                grupo["selecoes"][partida["selecao2"]]["pontos"] += 1

            grupo["selecoes"][partida["selecao1"]]["gols_marcados"] += partida["gols1"]
            grupo["selecoes"][partida["selecao2"]]["gols_marcados"] += partida["gols2"]

            grupo["selecoes"][partida["selecao1"]]["saldo_gols"] += partida["gols1"] - partida["gols2"]
            grupo["selecoes"][partida["selecao2"]]["saldo_gols"] += partida["gols2"] - partida["gols1"]

    return tabela_pontos