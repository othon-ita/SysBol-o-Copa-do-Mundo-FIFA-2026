import json
from funções.gerar_tabela_pontos_fase1 import gerar_tabela_pontos_fase1
def fases32():
    #Coleta as informações do usuário e usa a função para gera a tabela de pontos
    nome = input('Digite o seu nome:')
    nome_arquivo = f'./apostadores/palpites_{nome}.json'
    tabelas_de_pontos = gerar_tabela_pontos_fase1(nome_arquivo)
    print('Primeiro e Segundos colocados'.center(100, '='))
    terceiroes = []
    primeiros = []
    segundos = []
    
    with open(f'./apostadores/palpites_{nome}.json', 'r', encoding = 'utf-8') as arquivo:

        leitura = json.load(arquivo)
    for grupo in tabelas_de_pontos.values():
        
        #Coleta todos os times do grupo em uma lista para podermos ordenar
        times_do_grupo = []
        
       #coloca todos os times de um grupo junto com seus dados, no formato de dicionário e mm uma lista 
        for time, dados in grupo['selecoes'].items():
            times_do_grupo.append({
                
                'time': time,
                'pontos': dados['pontos'],
                'saldo_gols': dados['saldo_gols'],
                'gols_marcados': dados['gols_marcados']
            })
            
        #Função interna que aplica os 4 critérios de desempate
        def decidir_confronto(time1, time2):
            # Critério pontos
            if time1['pontos'] != time2['pontos']:
                return time1['pontos'] > time2['pontos']
            
            # Critério saldo de gols
            if time1['saldo_gols'] != time2['saldo_gols']:
                return time1['saldo_gols'] > time2['saldo_gols']
            
            # Critério gols marcados
            if time1['gols_marcados'] != time2['gols_marcados']:
                return time1['gols_marcados'] > time2['gols_marcados']
            
            # Critério confronto direto 
            for jogo in leitura:
                if jogo.get('selecao1') == time1['time'] and jogo.get('selecao2') == time2['time']:
                    return jogo.get('gols1', 0) > jogo.get('gols2', 0)
                if jogo.get('selecao1') == time2['time'] and jogo.get('selecao2') == time1['time']:
                    return jogo.get('gols2', 0) > jogo.get('gols1', 0)
            
        def ordenar_crescente(lista_times):
                tam = len(lista_times)
                for i in range(tam):
                    for j in range(i + 1, tam):
                        # Se o time I for MELHOR que o time J, eles trocam, empurrando o melhor time para cima e o pior consequentemente para tras
                        
                        if decidir_confronto(lista_times[i], lista_times[j]):
                            lista_times[i], lista_times[j] = lista_times[j], lista_times[i]
                return lista_times
        #O motorzin que verifica de dois em dois times os critérios, usando a função interna
        n = len(times_do_grupo)
        
        for i in range(n):
            for j in range(i + 1, n):
                if decidir_confronto(times_do_grupo[j], times_do_grupo[i]):
                    # Se o time J for melhor que o time I, eles trocam de posição
                    times_do_grupo[i], times_do_grupo[j] = times_do_grupo[j], times_do_grupo[i]

        primeiros.append(times_do_grupo[0])
        segundos.append(times_do_grupo[1])
        terceiroes.append(times_do_grupo[2])

        primeiros = ordenar_crescente(primeiros)
        segundos = ordenar_crescente(segundos)
        terceiros = ordenar_crescente(terceiroes)
        

        # Agora temos o 1º, 2º e o 3º lugar que passaram para próxima fase
        terceiros  = terceiroes[:8]
        
        
    
    for i in range(len(primeiros)):
        print(f"1º {primeiros[i]['time']} | 2º: {segundos[i]['time']}")
    print('Terceiros colocados'.center(50, '='))
    for i in terceiros:
        print(i.get('time'))

    espera = input ()