from funções.consultar_dados import verificar_existencia

def pontuação_apostador(nome):
    gabarito = verificar_existencia("gabarito", "as seleções")
    if gabarito == None:
        return None
    
    palpites = verificar_existencia(f"./apostadores/palpites_{nome}", "os seus palpites")
    if palpites == None:
        return None

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
        if i.get('gols1') == -1 or i.get('gols2') == -1:
            continue
        else:
            for j in palpites:
                if i.get('id') == j.get('id'):
                    if j.get('gols1') == -1 or j.get('gols2') == -1:
                        apostador["sem_palpite"]['id'].append(i.get('id'))
                        apostador["sem_palpite"]['vezes'] += 1
                        continue
                    else:
                        if i.get('selecao1') == j.get('selecao1') and i.get('selecao2') == j.get('selecao2'):
                            if i.get('gols1') == j.get('gols1') and i.get('gols2') == j.get('gols2'):
                                apostador["placar_exato"]["id"].append(i.get('id'))
                                apostador["placar_exato"]["vezes"] += 1
                                apostador["pontos"] += 10
                            elif i.get('gols1') == j.get('gols1') or i.get('gols2') == j.get('gols2'):
                                apostador["placar_parcial"]["id"].append(i.get('id'))
                                apostador["placar_parcial"]["vezes"] += 1
                                apostador["pontos"] += 7
                            elif (i.get('gols1') > i.get('gols2') and j.get('gols1') > j.get('gols2')) or (i.get('gols1') < i.get('gols2') and j.get('gols1') < j.get('gols2')):
                                apostador["resultado_correto"]['id'].append(i.get('id'))
                                apostador["resultado_correto"]['vezes'] += 1
                                apostador["pontos"] += 5
                            else:
                                apostador['erros']['id'].append(i.get('id'))
                                apostador["erros"]['vezes'] += 1
    
    return tabela_pontuacao
                