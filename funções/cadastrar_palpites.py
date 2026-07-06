import json
from time import sleep
from funções.limpar import limpar
from funções.consultar_dados.verificar_existencia import verificar_existencia


"""Cadastra os palpites de um apostador de acordo com as partidas existentes no gabarito. Permite listar todos os jogos, listar apenas jogos sem palpite, 
   cadastrar ou alterar o placar de um jogo e voltar ao menu principal. Além disso, verifica se as seleções já estão carregadas."""
def cadastrar_palpites():
    #verifica a existência do gabarito
    partidas = verificar_existencia("gabarito","as seleções")
    if partidas == None:
        return
    
    status = True
    nome = input('Digite o seu nome: ')
    try:
        with open (f'./apostadores/palpites_{nome}.json', 'r', encoding = 'utf-8') as arquivo:
                        leitura = json.load(arquivo)
    except FileNotFoundError:
        input('Desculpe, mas você ainda não está cadastrado no sistema\n Pressione ENTER para continuar...')
        return
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
                        while gols1 < 0:
                            gols1 = int(input(f"\nDigite um número de gols válido!: "))

                        gols2 = int(input(f"Digite o número de gols do(a) {i.get('selecao2')}: "))
                        while gols2 < 0:
                            gols2 = int(input(f"\nDigite um número de gols válido!: "))

                        print("\nPalpite cadastrado com sucesso!")
                        
                        i.update({'gols1': gols1, 'gols2' : gols2})
                        print(f"\n{i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
                        
                input("\nPressione ENTER para continuar...")
                with open (f'./apostadores/palpites_{nome}.json ', 'w', encoding = 'utf-8') as arquivo:
                    json.dump(leitura, arquivo, indent = 4)
            case 4 : 
                break
