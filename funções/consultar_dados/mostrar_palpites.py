import json

def mostrar_palpites(caminho, tipo):
    """Mostra os palpites de um apostador, podendo exibir todos os palpites ou apenas os que estão ausentes."""
    
    with open (f'{caminho}.json', 'r', encoding = 'utf-8') as arquivo:
        leitura = json.load(arquivo)
    
    if tipo == "todos":
        print("Palpites Atuais:")
        for i in leitura:
            try:
                print(f"\nID: {i.get('id')}")
                print(f"Fase: {i.get('fase')}")
                print(f"Grupo: {i.get('grupo')}")
                print(f"Partida: {i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
            except:
                print(f"\nID: {i.get('id')}")
                print(f"Fase: {i.get('fase')}")
                print(f"Partida: {i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
    
    elif tipo == "sem palpites":
        print("Palpites Ausentes:")
        for i in leitura:
            if i.get('gols1') == -1 or i.get('gols2') == -1:
                try:
                    print(f"\nID: {i.get('id')}")
                    print(f"Fase: {i.get('fase')}")
                    print(f"Grupo: {i.get('grupo')}")
                    print(f"Partida: {i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
                except:
                    print(f"\nID: {i.get('id')}")
                    print(f"Fase: {i.get('fase')}")
                    print(f"Partida: {i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
    input("\nPressione ENTER para continuar...")