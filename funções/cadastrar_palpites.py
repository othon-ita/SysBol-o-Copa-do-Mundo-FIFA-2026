import json
from time import sleep
from funções.limpar import limpar

def cadastrar_palpites():
    try:
        with open ('./jogos/gabarito.json', 'r', encoding = 'utf-8') as arquivo:
            partidas = json.load(arquivo)
    except: 
        print('Ops! Você esqueceu de carregar as selecoes. Volte aqui mais tarde!!')
        sleep(5)
        return
    
    status = True
    nome = input('Digite o seu nome:\n')
    
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
        escolha3 = int (input('''--------------------------------------------
1. Listar todos os jogos do bolão
2. Listar apenas jogos sem palpite
3. Cadastrar ou alterar o placar de um jogo
4. Sair
'''))

        match escolha3:
            case 1:
                for i in leitura:
                    print(f'{i}\n')
                espera = input ()
            case 2:
                for i in leitura:
                    if i.get('gols1') == -1 and i.get('gols1') == -1:
                        print (f'{i}\n')
                espera = input()
            case 3:
                escolha4 = int(input('--------------------------------------------\nQual id do jogo que desejar cadastrar ou alterar o placar:'))
                for i in leitura:
                    if i.get('id') == escolha4:
                        print(i)
                gols1 = int(input('digite a quantidade de gols para primeira selecao:'))
                gols2 = int(input('digite a quantidade de gols para segunda selecao:'))

                for i in leitura:
                    if i.get ('id') == escolha4:
                        i.update({'gols1': gols1, 'gols2' : gols2})

                with open (f'./apostadorespalpites_{nome}.json ', 'w', encoding = 'utf-8') as arquivo:
                    json.dump(leitura, arquivo, indent = 4)
            case 0 : 
                break
