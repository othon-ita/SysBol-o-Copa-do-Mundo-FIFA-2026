import json
from time import sleep
from funções.limpar import limpar

def cadastrar_palpites():
    try:
        with open ('./jogos/gabarito.json', 'r', encoding = 'utf-8') as arquivo:
            partidas = json.load(arquivo)
    except: 
        print('Ops! Você esqueceu de carregar as seleções. Volte aqui mais tarde!')
        sleep(5)
        return
    
    status = True
    nome = input('Digite o seu nome: ')
    
    with open (f'./apostadores/palpites_{nome}.json', 'r', encoding = 'utf-8') as arquivo:
                    leitura = json.load(arquivo)
    if (not leitura[71].get('selecao1')) or (not leitura[71].get('selecao2')):
        for i in leitura:   
            for j in partidas:
                if not status:
                    status = True
                    break
                if (i.get('id') == j.get('id')):
                    status = False
                    i.update({'selecao1' : j.get('selecao1'), 'selecao2' : j.get('selecao2')})
        with open(f'./apostadores/palpites_{nome}.json', 'w', encoding = 'utf-8') as arquivo:
            json.dump(leitura, arquivo, indent = 4)

    while True:
        limpar()
        print(8*"*", f"Palpites de {nome}", 8*"*")
        escolha3 = int(input(
'''1. Listar todos os jogos do bolão
2. Listar apenas jogos sem palpite
3. Cadastrar ou alterar o placar de um jogo
4. Voltar ao menu principal

Digite a opção desejada: '''))

        match escolha3:
            case 1:
                print("\nJogos:")
                for i in leitura:
                    if i.get('fase') == 1:
                        print(f"\nID: {i.get('id')}")
                        print(f"Fase: {i.get('fase')}")
                        print(f"Grupo: {i.get('grupo')}")
                        print(f"Partida: {i.get('selecao1')} x {i.get('selecao2')}")
                        
                        print("\nPalpite Atual:")
                        print(f"{i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
                        
                input("\nPressione ENTER para continuar...")
            case 2:
                print("\nJogos sem palpite:")
                for i in leitura:
                    if i.get('gols1') == -1 and i.get('gols1') == -1:
                        print(f"\nID: {i.get('id')}")
                        print(f"Fase: {i.get('fase')}")
                        print(f"Grupo: {i.get('grupo')}")
                        print(f"Partida: {i.get('selecao1')} x {i.get('selecao2')}")
                        
                        print("\nPalpite Atual:")
                        print(f"{i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
                        
                input("\nPressione ENTER para continuar...")
            case 3:
                escolha4 = int(input("\nDigite o ID do jogo: "))
                for i in leitura:
                    if i.get('id') == escolha4:
                        print("\nJogo encontrado:")
                        print(f"\nID: {i.get('id')}")
                        print(f"Fase: {i.get('fase')}")
                        print(f"Grupo: {i.get('grupo')}")
                        print(f"Partida: {i.get('selecao1')} x {i.get('selecao2')}")
                        
                        print("\nPalpite Atual:")
                        print(f"{i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
                        
                        gols1 = int(input(f"\nDigite o número de gols do(a) {i.get('selecao1')}: "))
                        gols2 = int(input(f"Digite o número de gols do(a) {i.get('selecao2')}: "))

                        print("\nPalpite cadastrado com sucesso!")
                        
                        i.update({'gols1': gols1, 'gols2' : gols2})
                        print(f"\n{i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
                        
                input("\nPressione ENTER para continuar...")
                with open (f'./apostadores/palpites_{nome}.json ', 'w', encoding = 'utf-8') as arquivo:
                    json.dump(leitura, arquivo, indent = 4)
            case 4 : 
                break
