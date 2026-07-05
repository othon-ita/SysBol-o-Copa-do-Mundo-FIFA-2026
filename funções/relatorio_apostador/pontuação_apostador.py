from funções.consultar_dados import verificar_existencia

"""Função responsável por gerar a "tabela_pontuação", dicionário da pontuação de cada apostador indexado aos seus nomes. No dicionário de cada apostador, existem chaves como: pontos, placar_exato, placar_parcial, resultado_correto, erros e sem_palpite; representado, respectivamente a pontuação total e cada tipo de marcação de pontos. 

Cada chave possui um dicionário com as chaves "id", lista de ids das partidas de cada tipo de pontuação, e "vezes", quantidade de vezes que o apostador teve certo tipo de pontuação. A função retorna a tabela_pontuação."""
def pontuação_apostador(nome):
    #Verificação da existência dos seguintes arquivos
    gabarito = verificar_existencia("gabarito", "as seleções")
    if gabarito == None:
        return None
    
    palpites = verificar_existencia(f"./apostadores/palpites_{nome}", "os seus palpites")
    if palpites == None:
        return None

    #Declaração de dicionário para armazenar a pontuação do apostador
    tabela_pontuacao = {}
    if nome not in tabela_pontuacao:
        tabela_pontuacao[nome] = {}
        
    apostador = tabela_pontuacao[nome]
    
    #Declaração de chaves e valores para o dicionário
    apostador["pontos"] = 0
    apostador["placar_exato"] = {}
    apostador["placar_exato"]["id"] = list()
    apostador["placar_exato"]["vezes"] = 0
    
    apostador["placar_parcial"] = {}
    apostador["placar_parcial"]["id"] = list()
    apostador["placar_parcial"]["vezes"] = 0
    
    apostador["resultado_correto"] = {}
    apostador["resultado_correto"]["id"] = list()
    apostador["resultado_correto"]["vezes"] = 0
    
    apostador["erros"] = {}
    apostador["erros"]["id"] = list()
    apostador["erros"]["vezes"] = 0
    
    apostador["sem_palpite"] = {}
    apostador["sem_palpite"]["id"] = list()
    apostador["sem_palpite"]["vezes"] = 0

    for i in gabarito:
        #Somente casos em que o gabarito já possua o resultado da partida são contabilizados
        if i.get('gols1') == -1 or i.get('gols2') == -1:
            continue
        else:
            for j in palpites:
                if i.get('id') == j.get('id'):
                    if j.get('gols1') == -1 or j.get('gols2') == -1:
                        #Contabilização de jogos sem palpites
                        apostador["sem_palpite"]['id'].append(i.get('id'))
                        apostador["sem_palpite"]['vezes'] += 1
                        continue
                    else:
                        if i.get('selecao1') == j.get('selecao1') and i.get('selecao2') == j.get('selecao2'):
                            if i.get('gols1') == j.get('gols1') and i.get('gols2') == j.get('gols2'):
                                #Contabilização de jogos com placar exato
                                apostador["placar_exato"]["id"].append(i.get('id'))
                                apostador["placar_exato"]["vezes"] += 1
                                apostador["pontos"] += 10
                            elif i.get('gols1') == j.get('gols1') or i.get('gols2') == j.get('gols2'):
                                #Contabilização de jogos com placar parcial
                                apostador["placar_parcial"]["id"].append(i.get('id'))
                                apostador["placar_parcial"]["vezes"] += 1
                                apostador["pontos"] += 7
                            elif (i.get('gols1') > i.get('gols2') and j.get('gols1') > j.get('gols2')) or (i.get('gols1') < i.get('gols2') and j.get('gols1') < j.get('gols2')):
                                #Contabilização de jogos com resultado correto
                                apostador["resultado_correto"]['id'].append(i.get('id'))
                                apostador["resultado_correto"]['vezes'] += 1
                                apostador["pontos"] += 5
                            else:
                                #Contabilização de palpites incorretos
                                apostador['erros']['id'].append(i.get('id'))
                                apostador["erros"]['vezes'] += 1
    
    return tabela_pontuacao
                