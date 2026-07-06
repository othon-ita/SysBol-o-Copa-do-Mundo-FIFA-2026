from funções.segunda_fase.fase_de_32.gerar_tabela_pontos_fase1 import gerar_tabela_pontos_fase1
from funções.segunda_fase.fase_de_32.classificacao_fase_1 import classificacao_fase1
from funções.segunda_fase.fase_de_32.partidas_fase32 import partidas_fase32
import json


#junção de todas as funções pra gerar as partidas da fase de 32
def gerar_fase32(nome_arquivo):
    """
    Função que chama outras funções necessárias para gerar as partidas da fase de 32
    """

    #monta a tabela com os pontos, saldo de gol e gols marcados
    tabela = gerar_tabela_pontos_fase1(nome_arquivo)
    #verifica se palpites foram dados 
    if tabela == None:
        return

    #a mesma tabela agora é ordenada com as classificações das seleções baseada nos pontos, saldo de gols, gols marcados e confronto diretos (ou sorteio se ainda houver empate)
    tabela = classificacao_fase1(tabela, nome_arquivo)

    #gera as partidas da fase de 32 com base nas classificações
    partidas_32 = partidas_fase32(tabela)


    #manda as partidas pra um arquivo json
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        partidas = json.load(arquivo)

    partidas.extend(partidas_32)

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(partidas, arquivo, indent=4, ensure_ascii=False)

    return partidas