import json

def cadastrar_gabarito():
    """
    Cadastro dos resultados oficiais de todas as partidas. Manipule diretamente o arquivo gabarito.json 
    ou utilize essa função para definir os gols de cada seleção.

    """
    with open("gabarito.json", "r", encoding="utf-8") as arquivo:
        partidas = json.load(arquivo)

    #verifica qual a fase atual
    if len(partidas) == 72:
        fase_atual = 1

    elif len(partidas) == 88:
        fase_atual = "fase de 32"

    elif len(partidas) == 96:
        fase_atual = "oitavas de finais"

    elif len(partidas) == 100:
        fase_atual = "quartas de finais"
        
    elif len(partidas) == 102:
        fase_atual = "semi finais"

    elif len(partidas) == 103:
        fase_atual = "terceiro lugar"

    elif len(partidas) == 104:
        fase_atual = "final"
        

    for partida in partidas:
        #se partida não for da fase atual, pula
        if partida["fase"] != fase_atual:
            continue
        
        #permite que altere ou cadastre os gols das seleçoes, na fase atual
        print(f"Id da partida: {partida['id']}   \nFase: {partida['fase']} \nPartida: {partida['selecao1']} x {partida['selecao2']}")

        #se a partida já foi cadastrada:
        if partida["gols1"] > -1 and partida["gols2"] > -1:
            print("Cadastro realizado anteriormente:")
            print(f"Gols da primeira seleção ({partida['selecao1']}): {partida['gols1']}")
            print(f"Gols da segunda seleção ({partida['selecao2']}): {partida['gols1']}")
            print("Altere o resultado abaixo:")

        print(f"Digite a quantidade de gols da primeira seleção: ({partida['selecao1']})")
        partida["gols1"] = int(input())
        print(f"Digite a quantidade de gols da segunda seleção: ({partida['selecao2']})")
        partida["gols2"] = int(input())

    with open("gabarito.json", "w", encoding="utf-8") as arquivo:
        json.dump(partidas, arquivo, indent=4, ensure_ascii=False)
