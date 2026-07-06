import json

def gerar_tabela_pontos_fase1(nome_arquivo):
    """
    Contabiliza os pontos, saldo de gols e gols marcados de cada seleção na fase 1
    """
    tabela_pontos = {}
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        partidas = json.load(arquivo)
        for partida in partidas:
            if (partida.get('gols1')) <= 0 or (partida.get('gols2') <= 0)  :
                input('Desculpe, mas você ainda não deu os seus palpites!\nPressione ENTER para continuar...')
                return None
            elif (partida.get('selecao1') == '') or (partida.get('selecao2') == '') :
                input('Desculpe, mas você ainda não carregou as seleções no seu arquivo!\nPressione ENTER para continuar...')
                return None
            #coloca os grupos no dicionário tabela_pontos
            grupo_nome = partida["grupo"]

            #verifica se o grupo já tá no dicionário
            if grupo_nome not in tabela_pontos:
                tabela_pontos[grupo_nome] = {
                    
                }

            #só pra não ter que ficar repetindo tabela_pontos[grupo_nome] nas linhas abaixo
            grupo = tabela_pontos[grupo_nome]

            #verifica se a seleção tá no dicionário ou não
            if partida["selecao1"] not in grupo:
                #adiciona ela na chave "seleçoes" do grupo
                grupo[partida["selecao1"]] = {
                    "pontos": 0,
                    "saldo_gols": 0,
                    "gols_marcados": 0
                }

            #mesma coisa
            if partida["selecao2"] not in grupo:
                grupo[partida["selecao2"]] = {
                    "pontos": 0,
                    "saldo_gols": 0,
                    "gols_marcados": 0
                }


            #contagem dos pontos
            #vitória ou empate (3 pontos ou 1 ponto)
            if partida["gols1"] > partida["gols2"]:
                grupo[partida["selecao1"]]["pontos"] += 3

            elif partida["gols1"] < partida["gols2"]:
                grupo[partida["selecao2"]]["pontos"] += 3

            else:
                grupo[partida["selecao1"]]["pontos"] += 1
                grupo[partida["selecao2"]]["pontos"] += 1

            #gols marcados
            grupo[partida["selecao1"]]["gols_marcados"] += partida["gols1"]
            grupo[partida["selecao2"]]["gols_marcados"] += partida["gols2"]


            #saldo de gols
            grupo[partida["selecao1"]]["saldo_gols"] += partida["gols1"] - partida["gols2"]
            grupo[partida["selecao2"]]["saldo_gols"] += partida["gols2"] - partida["gols1"]

    return tabela_pontos