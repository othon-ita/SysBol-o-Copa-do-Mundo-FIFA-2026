import json
import random
def confronto_direto(nome_arquivo, grupo, empatadas):
    #as seleções empatadas vão pro parâmetro empatadas, ex: ([selecao1, selecao2, seleção3])

    """
    Função que é chamada na função que gera as classificações da fase 1 caso haja empate em pontos, 
    saldo de gols e gols marcados.
    """

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        partidas = json.load(arquivo)

    dados_confronto_direto = {}
    
    for selecao in empatadas:
        dados_confronto_direto[selecao] = {
            "pontos": 0,
            "saldo_gols": 0,
            "gols_marcados": 0
        }
         
    #procura os confrontos entre as seleções empatadas
    #calcula os pontos, saldo de gols e gols marcados obtidos nesses confrontos
    for partida in partidas:

        #apenas percorre o grupo das seleções que estão empatadas
        if partida["grupo"] != grupo:
            continue
        

        selecao1 = partida["selecao1"]
        selecao2 = partida["selecao2"]

        if selecao1 in empatadas and selecao2 in empatadas:
                    #vitória ou empate (3 pontos ou 1 ponto)
                    #seleção1 venceu
                    if partida["gols1"] > partida["gols2"]:
                        dados_confronto_direto[selecao1]["pontos"] += 3

                    #seleção2 venceu
                    elif partida["gols2"] > partida["gols1"]:
                        dados_confronto_direto[selecao2]["pontos"] += 3
                    else:
                        dados_confronto_direto[selecao1]["pontos"] += 1
                        dados_confronto_direto[selecao2]["pontos"] += 1

                    #gols marcados
                    dados_confronto_direto[selecao1]["gols_marcados"] += partida["gols1"]
                    dados_confronto_direto[selecao2]["gols_marcados"] += partida["gols2"]

                    #saldo de gols
                    dados_confronto_direto[selecao1]["saldo_gols"] += partida["gols1"] - partida["gols2"]
                    dados_confronto_direto[selecao2]["saldo_gols"] += partida["gols2"] - partida["gols1"]


    itens_lista = list(dados_confronto_direto.items())

    #embaralha a lista
    random.shuffle(itens_lista)

    #ordena por pontos, saldo de gols e gols marcados de cada seleção
    itens_ordenados = sorted(
            itens_lista, 
            key=lambda item: (
                -item[1]["pontos"],
                -item[1]["saldo_gols"],
                -item[1]["gols_marcados"]
            )
        )

    #converte de volta para dicionário
    vitorias_ordenadas = dict(itens_ordenados)

    #pega as seleções do dicionário
    selecoes_ordenadas = list(vitorias_ordenadas.keys())


    #retorna a lista ordenada das seleções se não houver empate nos pontos, saldo de gols e gols marcados nos confrontos diretos
    #se ainda assim houver empate nos pontos, gols marcados e saldo de gols, retorna a lista embaralhada das seleções ordenadas
    return selecoes_ordenadas
