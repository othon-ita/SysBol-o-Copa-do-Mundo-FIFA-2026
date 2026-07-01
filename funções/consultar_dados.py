import json
from time import sleep
from funções.limpar import limpar

def verificar_existencia(caminho, tipo):
    try:
        with open (f'{caminho}.json', 'r', encoding = 'utf-8') as arquivo:
            leitura = json.load(arquivo)
        return leitura
    except: 
        print(f"Ops! Você esqueceu de carregar {tipo}. Volte aqui mais tarde!")
        sleep(5)
        return None
    
def mostrar_palpites(caminho, tipo):
    with open (f'{caminho}.json', 'r', encoding = 'utf-8') as arquivo:
        leitura = json.load(arquivo)
    
    if tipo == "todos":
        print("Palpites Atuais:")
        for i in leitura:
            if i.get('fase') == 1:
                print(f"{i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
    
    elif tipo == "sem palpites":
        print("Palpites Ausentes:")
        for i in leitura:
            if i.get('fase') == 1:
                if i.get('gols1') == -1 and i.get('gols2') == -1:
                    print(f"{i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
    input("\nPressione ENTER para continuar...")

def mostrar_jogos(caminho, filtro, valor):
    with open (f'{caminho}.json', 'r', encoding = 'utf-8') as arquivo:
        leitura = json.load(arquivo)
        print("\nJogos:")
        for i in leitura:
            if i.get(f'{filtro}') == valor:
                print(f"\nID: {i.get('id')}")
                print(f"Fase: {i.get('fase')}")
                print(f"Grupo: {i.get('grupo')}")
                print(f"Partida: {i.get('selecao1')} x {i.get('selecao2')}")
            
    input("\nPressione ENTER para continuar...")
    
def consultar_dados():
    while True:
        limpar()
        print(8*"*", "Consulta de Dados", 8*"*")
        print("1. Listar calendário completo de jogos")
        print("2. Listar jogos por fase")
        print("3. Listar jogos por grupo")
        print("4. Buscar jogo por ID")
        print("5. Visualizar palpites de um apostador")
        print("6. Visualizar apenas palpites pendentes de um apostador")
        print("7. Visualizar gabarito oficial")
        print("8. Visualizar resultados pendentes no gabarito")
        print("9. Voltar ao menu principal \n")
        opção = int(input("Digite a opção desejada: "))
        
        if opção == 2:
            fase = int(input("Digite a fase desejada (Ex: 1, 2,...,6): "))
            if fase == 1:
                leitura = verificar_existencia("./jogos/gabarito", "as seleções")
                if leitura == None:
                    return               
                mostrar_jogos("./jogos/gabarito", "fase", fase)  
                       
            else:
                print("Fase inválida. Por favor, digite uma fase válida (1, 2,...,6).")
        
        elif opção == 3:
            grupo = input("Digite o grupo desejado (Ex: A, B,..., L): ")
            if grupo in ["A", "B", "C", "D", "E", "F", "G", "H", "L"]:
                leitura = verificar_existencia("./jogos/gabarito", "as seleções")
                if leitura == None:
                    return
                mostrar_jogos("./jogos/gabarito", "grupo", f"Grupo {grupo}")
                
            else:
                print("Grupo inválido. Por favor, digite um grupo válido (A, B,..., L).")
                sleep(5)
        
        elif opção == 4:
            id = int(input("Digite o ID do jogo desejado: "))
            leitura = verificar_existencia("./jogos/gabarito", "as seleções")
            if leitura == None:
                return
            mostrar_jogos("./jogos/gabarito", "id", id)
        
        elif opção == 5:
            nome = input("Digite o seu nome: ")
            leitura = verificar_existencia(f'./apostadores/palpites_{nome}', "os palpites do apostador")
            if leitura == None:
                return
            mostrar_palpites(f'./apostadores/palpites_{nome}', "todos")
         
        elif opção == 6:
            nome = input("Digite o seu nome: ")
            leitura = verificar_existencia(f'./apostadores/palpites_{nome}', "os palpites do apostador")
            if leitura == None:
                return
            mostrar_palpites(f'./apostadores/palpites_{nome}', "sem palpites")
            
        elif opção == 9:
            break