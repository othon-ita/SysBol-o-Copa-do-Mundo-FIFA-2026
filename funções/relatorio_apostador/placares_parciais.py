import json
from funções.relatorio_apostador.pontuação_apostador import pontuação_apostador

def placares_parciais(nome):
    relatorio = ""
    pontos = pontuação_apostador(nome)
    placar_parcial = pontos[nome]['placar_parcial']
    with open ('gabarito.json', 'r', encoding = 'utf-8') as arquivo:
        gabarito = json.load(arquivo)
    with open (f'./apostadores/palpites_{nome}.json', 'r', encoding = 'utf-8') as arquivo:
        palpites = json.load(arquivo)
    
    print("\n" + 40*"=")
    relatorio += "\n" + (40*"=")
    print(f"PLACARES PARCIAIS ({placar_parcial['vezes']*7} pontos)")
    relatorio += f"\nPLACARES PARCIAIS ({placar_parcial['vezes']*7} pontos)"
    print(40*"=")
    relatorio += "\n" + (40*"=") + "\n"
    
    for i in placar_parcial['id']:
        print(f"\nJogo {i}")
        relatorio += f"\nJogo {i}"
        for j in gabarito:
            if j.get('id') == i:
                print(f"{j.get('selecao1')} {j.get('gols1')} x {j.get('gols2')} {j.get('selecao2')}")
                relatorio += f"\n{j.get('selecao1')} {j.get('gols1')} x {j.get('gols2')} {j.get('selecao2')}" + "\n"
                print(f"\nGabarito: {j.get('selecao1')} {j.get('gols1')} x {j.get('gols2')} {j.get('selecao2')}")
                relatorio += f"\nGabarito: {j.get('selecao1')} {j.get('gols1')} x {j.get('gols2')} {j.get('selecao2')}"
        
        for z in palpites:
            if z.get('id') == i:
                print(f"Palpite: {z.get('selecao1')} {z.get('gols1')} x {z.get('gols2')} {z.get('selecao2')}")
                relatorio += f"\nPalpite: {z.get('selecao1')} {z.get('gols1')} x {z.get('gols2')} {z.get('selecao2')}" + "\n"
        if i != placar_parcial['id'][-1]:
            print("\n" + 40*"-")
            relatorio += "\n" + (40*"-")
            
    return relatorio