from gerar_tabela_pontos_fase1 import gerar_tabela_pontos_fase1
from classificacao_fase_1 import classificacao_fase1
from partidas_fase32 import partidas_fase32
import json


#junção de todas as funções p gerar as partidas da fase de 32
def gerar_fase32(nome_arquivo):
    tabela = gerar_tabela_pontos_fase1(nome_arquivo)

    tabela = classificacao_fase1(tabela, nome_arquivo)

    partidas_32 = partidas_fase32(tabela)

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        partidas = json.load(arquivo)

    partidas.extend(partidas_32)

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(partidas, arquivo, indent=4, ensure_ascii=False)

    return partidas


gerar_fase32("gabarito.json")