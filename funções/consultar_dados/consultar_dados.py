#Nome e matrícula dos integrantes do grupo
#André Nicolas de Sousa Vieira - 605925
#Maria Eduarda da Silva Alves - 604390
#Othon Ítalo Nascimento de Moraes - 600006
import json
from funções.limpar import limpar
from funções.consultar_dados.verificar_existencia import verificar_existencia
from funções.consultar_dados.mostrar_palpites import mostrar_palpites
from funções.consultar_dados.mostrar_jogos import mostrar_jogos

def consultar_dados():
    """Submenu para a consulta de diferentes dados, permitindo ao usuário listar o calendário completo de jogos, jogos por fase, grupo, ID. Visualizar palpites pendentes, ou não, de um apostador, o gabarito oficial e os resultados pendentes no gabarito."""
    
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
        
        try:
            opção = int(input("Digite a opção desejada: "))
        except:
            print("Digite um dígito válido!")
            opção = int(input("Digite a opção desejada: "))
        
        if opção == 1:
            leitura = verificar_existencia("gabarito", "as seleções")
            if leitura == None:
                return
                
            print("\n Calendário Completo:")
            for i in leitura:
                if i.get('fase') == 1:
                    print(f"\nID: {i.get('id')}")
                    print(f"Fase: {i.get('fase')}")
                    print(f"Grupo: {i.get('grupo')}")
                    print(f"Partida: {i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
                else:
                    print(f"\nID: {i.get('id')}")
                    print(f"Fase: {i.get('fase')}")
                    print(f"Partida: {i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
            input("\nPressione ENTER para continuar...")
                    
        elif opção == 2:
            while True:
                fase = input("Digite a fase desejada (Ex: 1, fase de 32, oitavas de finais, quartas de finais, semi finais, terceiro lugar, final):\n")
                if fase in ["1", "fase de 32", "FASE DE 32", "oitavas de finais", "OITAVAS DE FINAIS", "quartas de finais", "QUARTAS DE FINAIS", "semi finais", "SEMI FINAIS", "terceiro lugar", "TERCEIRO LUGAR", "final", "FINAL"]:
                    leitura = verificar_existencia("gabarito", "as seleções")
                    if leitura == None:
                        return       
                    if fase == "1":
                        fase = 1
                    mostrar_jogos("gabarito", "fase", fase)
                    break
                else:
                    print("Fase inválida. Por favor, digite uma fase válida.")
        
        elif opção == 3:
            grupo = input("Digite o grupo desejado (Ex: A, B,..., L): ")
            if grupo in ["A", "B", "C", "D", "E", "F", "G", "H", "L"]:
                leitura = verificar_existencia("gabarito", "as seleções")
                if leitura == None:
                    return
                mostrar_jogos("gabarito", "grupo", f"Grupo {grupo}")
                
            else:
                print("Grupo inválido. Por favor, digite um grupo válido (A, B,..., L).")
                input("Pressione ENTER para continuar...")
        
        elif opção == 4:
            id = int(input("Digite o ID do jogo desejado: "))
            leitura = verificar_existencia("gabarito", "as seleções")
            if leitura == None:
                return
            mostrar_jogos("gabarito", "id", id)
        
        elif opção == 5:
            nome = input("Digite o seu nome: ")
            leitura = verificar_existencia(f'./apostadores/palpites_{nome}', "os seus palpites")
            if leitura == None:
                return
            mostrar_palpites(f'./apostadores/palpites_{nome}', "todos")
         
        elif opção == 6:
            nome = input("Digite o seu nome: ")
            leitura = verificar_existencia(f'./apostadores/palpites_{nome}', "os seus palpites")
            if leitura == None:
                return
            mostrar_palpites(f'./apostadores/palpites_{nome}', "sem palpites")
        
        elif opção == 7:
            leitura = verificar_existencia ("gabarito", "as seleções")
            if leitura == None:
                return
            with open ("gabarito.json", 'r', encoding = 'utf-8') as arquivo:
                leitura = json.load(arquivo)
                
            print("\n Gabarito Oficial:")
            for i in leitura:
                if i.get('gols1') >= 0 and i.get('gols2') >= 0:
                    if i.get('fase') == 1:
                        print(f"\nID: {i.get('id')}")
                        print(f"Fase: {i.get('fase')}")
                        print(f"Grupo: {i.get('grupo')}")
                        print(f"Partida: {i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
                    else:
                        print(f"\nID: {i.get('id')}")
                        print(f"Fase: {i.get('fase')}")
                        print(f"Partida: {i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
                else: 
                    input('Desculpe, mas você ainda não deu os seus palpites completamente!\nPressione ENTER para continuar')
                    break
            input("\nPressione ENTER para continuar...")
        
        elif opção == 8:
            leitura = verificar_existencia ("gabarito", "as seleções")
            if leitura == None:

                return
            with open ("gabarito.json", 'r', encoding = 'utf-8') as arquivo:
                leitura = json.load(arquivo)
                
            print("\n Resultados Pendentes:")
            for i in leitura:
                if i.get('gols1') < 0 or i.get('gols2') < 0:
                    if i.get('fase') == 1:
                        print(f"\nID: {i.get('id')}")
                        print(f"Fase: {i.get('fase')}")
                        print(f"Grupo: {i.get('grupo')}")
                        print(f"Partida: {i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
                    else:
                        print(f"\nID: {i.get('id')}")
                        print(f"Fase: {i.get('fase')}")
                        print(f"Partida: {i.get('selecao1')} {i.get('gols1')} x {i.get('gols2')} {i.get('selecao2')}")
            input("\nPressione ENTER para continuar...")
        
        elif opção == 9:
            break
        else:
            input("\nDigito inválido!\nPressione ENTER para continuar...")