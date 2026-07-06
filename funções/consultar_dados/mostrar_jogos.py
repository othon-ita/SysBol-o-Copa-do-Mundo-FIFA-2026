import json

"""Mostra todos os jogos de acordo com o filtro e valor fornecidos, exibindo informações como ID, fase, grupo e partida."""
def mostrar_jogos(caminho, filtro, valor):
    with open (f'{caminho}.json', 'r', encoding = 'utf-8') as arquivo:
        leitura = json.load(arquivo)
        print(f"\nJogos:")
        for i in leitura:
            try:
                if (i.get(f'{filtro}') == valor) and i.get('grupo') != None:
                    print(f"\nID: {i.get('id')}")
                    print(f"Fase: {i.get('fase')}")
                    print(f"Grupo: {i.get('grupo')}")
                    print(f"Partida: {i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
                elif i.get(f'{filtro}') == valor:
                    print(f"\nID: {i.get('id')}")
                    print(f"Fase: {i.get('fase')}")
                    print(f"Partida: {i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
            except:
                continue
            
    input("\nPressione ENTER para continuar...")