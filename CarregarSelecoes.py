#adicionar comentários, docstrings e corrigir lógica se necessário

def carregarSelecoes():
    dicionarioSelecoes = {

    }

    grupo = []
    selecoes_adicionadas = []
    ok = True

    with open ("Selecoes.txt", "r", encoding="utf-8") as selecoes:

        soma = 0
        letra_inicial = 65

        for linha in selecoes:
            if linha.strip() == "":
                print("Erro: linha vazia detectada! Carregamento de seleções cancelado.")
                dicionarioSelecoes.clear()
                ok = False
                break

            soma +=1

            if soma > 48:
                print("Erro: número incorreto de seleções participantes! Carregamento de seleções cancelado.")
                dicionarioSelecoes.clear()
                ok = False
                break

            if linha.strip() in selecoes_adicionadas:
                print(f"Erro: Seleção repetida! ({linha.strip()}) Carregamento de seleções cancelado.")
                dicionarioSelecoes.clear()
                ok = False
                break
            else:
                selecoes_adicionadas.append(linha.strip())
                grupo.append(linha.strip())

            if len(grupo) == 4:
                dicionarioSelecoes[f"Grupo {chr(letra_inicial)}"] = grupo
                letra_inicial += 1
                grupo = []

        if soma < 48 and ok == True:
            ok = False
            print("Erro: número incorreto de seleções participantes! Carregamento de seleções cancelado.")
            dicionarioSelecoes.clear()


    partidas = []
    id_partida = 0

    #Combinação de partidas de cada grupo
    for chaves, valores in dicionarioSelecoes.items():
        for i in range(len(valores)):
            for j in range(i+1, len(valores)):
                id_partida += 1
                dicionarioPartida = {
                    "id": id_partida,
                    "fase": 1,
                    "grupo": chaves,
                    "selecao1": valores[i],
                    "selecao2": valores[j],
                    "gols1": -1,
                    "gols2": -1
                }
                partidas.append(dicionarioPartida)
    
    return dicionarioSelecoes, ok, partidas






