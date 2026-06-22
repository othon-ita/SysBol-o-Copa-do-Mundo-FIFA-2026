def carregarSelecoes():
    """
    Carrega seleções a partir de um arquivo selecoes.txt, agrupando-as de quatro em quatro nos grupos A até L com base nos critérios:
    - A quantidade de seleções é estritamente 48
    - Não pode haver alguma linha vazia no arquivo .txt
    - Nenhuma seleção pode estar repetida
    Após os grupos serem definidos, as partidas da primeira fase serão geradas automaticamente. Haverá 6 partidas por grupo.
    """

    #Todos os grupos serão adicionados nesse dicionário
    dicionarioSelecoes = {

    }

    #Lista das seleções que serão adicionadas em determinado grupo (A-L)
    grupo = []
    #Controle das seleções que já foram adicionadas, para evitar repetição
    selecoes_adicionadas = []
    #Verifica se o arquivo .txt atende os critérios ou não
    ok = True

    with open ("selecoes.txt", "r", encoding="utf-8") as selecoes:

        soma = 0
        #No padrão unicode, o número decimal 65 representa a letra A.
        letra_inicial = 65

        for linha in selecoes:
            #Verifica se tem alguma linha vazia
            if linha.strip() == "":
                print("Erro: linha vazia detectada! Carregamento de seleções cancelado.")
                dicionarioSelecoes.clear()
                ok = False
                break

            soma +=1

            #Verifica se há mais de 48 seleções
            if soma > 48:
                print("Erro: número incorreto de seleções participantes! Carregamento de seleções cancelado.")
                dicionarioSelecoes.clear()
                ok = False
                break

            #Verifica se há seleções repetidas
            if linha.strip() in selecoes_adicionadas:
                print(f"Erro: Seleção repetida! ({linha.strip()}) Carregamento de seleções cancelado.")
                dicionarioSelecoes.clear()
                ok = False
                break
            else:
                selecoes_adicionadas.append(linha.strip())
                grupo.append(linha.strip())

            #Agrupa 4 seleções em um Grupo A-L
            if len(grupo) == 4:
                #A função chr() converte um numero inteiro a seu caractere correspondente com base no padrão Unicode
                dicionarioSelecoes[f"Grupo {chr(letra_inicial)}"] = grupo
                #A variável letra_inicial será somada de 65(A) até 72(L)
                letra_inicial += 1
                grupo = []

        #Após todas as outras verificações, verifica se há menos que 48 seleções
        if soma < 48 and ok == True:
            ok = False
            print("Erro: número incorreto de seleções participantes! Carregamento de seleções cancelado.")
            dicionarioSelecoes.clear()


    #Lista que armazena os dicionários de partidas da primeira fase
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


