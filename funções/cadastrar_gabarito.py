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


    for partida in partidas:
        #se partida não for da fase atual, pula
        if len(partidas) > 102:
            if partida["fase"] != "final" and partida["fase"] != "terceiro lugar":
                continue
        elif partida["fase"] != fase_atual:
                continue
            
        #permite que altere ou cadastre os gols das seleçoes, na fase atual
        print(f"Id da partida: {partida['id']}   \nFase: {partida['fase']} \nPartida: {partida['selecao1']} x {partida['selecao2']}")

        #se a partida já foi cadastrada:
        if partida["gols1"] > -1 and partida["gols2"] > -1:
            print("Cadastro realizado anteriormente:")
            print(f"Gols da primeira seleção ({partida['selecao1']}): {partida['gols1']}")
            print(f"Gols da segunda seleção ({partida['selecao2']}): {partida['gols2']}")
            print("Altere o resultado abaixo:")

        print(f"Digite a quantidade de gols da primeira seleção: ({partida['selecao1']})")
        partida["gols1"] = int(input())
        #impede o cadastro de um número de gols inválido
        while partida["gols1"] < 0:
            partida["gols1"] = int(input("Cadastre um número válido de gols: "))

        print(f"Digite a quantidade de gols da segunda seleção: ({partida['selecao2']})")
        partida["gols2"] = int(input())
        while partida["gols2"] < 0:
            partida["gols2"] = int(input("Cadastre um número válido de gols: "))

    with open("gabarito.json", "w", encoding="utf-8") as arquivo:
        json.dump(partidas, arquivo, indent=4, ensure_ascii=False)
