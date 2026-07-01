import json
#Depois colocar no menu inicial e adicionar partidas além da primeira fase

def cadastrar_gabarito():
    """
    Cadastro dos resultados oficiais de todas as partidas. Manipule diretamente o arquivo gabarito.json 
    ou utilize essa função para definir os gols de cada seleção.

    """
    with open("gabarito.json", "r", encoding="utf-8") as arquivo:
        partidas = json.load(arquivo)

    for partida in partidas:
        print(f"Id da partida: {partida["id"]}   \nFase: {partida["fase"]} \nPartida: {partida["selecao1"]} x {partida["selecao2"]}")
        print(f"Digite a quantidade de gols da primeira seleção: ({partida["selecao1"]})")
        partida["gols1"] = int(input())
        print(f"Digite a quantidade de gols da primeira seleção: ({partida["selecao2"]})")
        partida["gols2"] = int(input())

    with open("gabarito.json", "w", encoding="utf-8") as arquivo:
        json.dump(partidas, arquivo, indent=4, ensure_ascii=False)
