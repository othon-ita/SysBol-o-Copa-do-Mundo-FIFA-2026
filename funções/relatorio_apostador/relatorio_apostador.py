import json
from funções.relatorio_apostador.pontuação_apostador import pontuação_apostador
from funções.relatorio_apostador.placares_exatos import placares_exatos
from funções.relatorio_apostador.placares_parciais import placares_parciais
from funções.relatorio_apostador.resultados_corretos import resultados_corretos
from funções.relatorio_apostador.erros import erros
from funções.relatorio_apostador.sem_palpite import sem_palpite

def relatorio_apostador():
    while True:
        relatorio = ""
        nome = input("Digite o seu nome: ")
        pontos = pontuação_apostador(nome)
        if pontos == None:
            return
        
        print(8*"*", "Relatório do Apostador", 8*"*")
        relatorio += (8*"*") + "Relatório do Apostador" + (8*"*") + "\n"
        print(f"\nNome: {nome}")
        relatorio += f"\nNome: {nome}"
        print(f"Placares Exatos: {pontos[nome]['placar_exato']['vezes']}")
        relatorio += f"\nPlacares Exatos: {pontos[nome]['placar_exato']['vezes']}"
        print(f"Placares Parciais: {pontos[nome]['placar_parcial']['vezes']}")
        relatorio += f"\nPlacares Parciais: {pontos[nome]['placar_parcial']['vezes']}"
        print(f"Resultados Corretos: {pontos[nome]['resultado_correto']['vezes']}")
        relatorio += f"\nResultados Corretos: {pontos[nome]['resultado_correto']['vezes']}"
        print(f"Erros: {pontos[nome]['erros']['vezes']}")
        relatorio += f"\nErros: {pontos[nome]['erros']['vezes']}"
        print(f"Sem Palpite: {pontos[nome]['sem_palpite']['vezes']}")
        relatorio += f"\nSem Palpite: {pontos[nome]['sem_palpite']['vezes']}" + "\n"
        
        placares_exatos(nome)
        relatorio += placares_exatos(nome)
        
        placares_parciais(nome)
        relatorio += placares_parciais(nome)
        
        resultados_corretos(nome)
        relatorio += resultados_corretos(nome)
        
        erros(nome)
        relatorio += erros(nome)
        
        sem_palpite(nome)
        relatorio += sem_palpite(nome)
        
        print("\n" + 40*"=")
        relatorio += "\n" + (40*"=")
        print("TOTAL GERAL")
        relatorio += "\nTOTAL GERAL"
        print(40*"=")
        relatorio += "\n" + (40*"=") + "\n"
        
        print(f"\nPlacares Exatos: {pontos[nome]['placar_exato']['vezes']} x 10 = {pontos[nome]['placar_exato']['vezes']*10} pontos")
        relatorio += f"\nPlacares Exatos: {pontos[nome]['placar_exato']['vezes']} x 10 = {pontos[nome]['placar_exato']['vezes']*10} pontos"
        print(f"Placares Parciais: {pontos[nome]['placar_parcial']['vezes']} x 7 = {pontos[nome]['placar_parcial']['vezes']*7} pontos")
        relatorio += f"\nPlacares Parciais: {pontos[nome]['placar_parcial']['vezes']} x 7 = {pontos[nome]['placar_parcial']['vezes']*7} pontos"
        print(f"Resultados Corretos: {pontos[nome]['resultado_correto']['vezes']} x 5 = {pontos[nome]['resultado_correto']['vezes']*5} pontos")
        relatorio += f"\nResultados Corretos: {pontos[nome]['resultado_correto']['vezes']} x 5 = {pontos[nome]['resultado_correto']['vezes']*5} pontos"
        print(f"Erros: {pontos[nome]['erros']['vezes']} x 0 = 0 pontos")
        relatorio += f"\nErros: {pontos[nome]['erros']['vezes']} x 0 = 0 pontos" + "\n"
        
        print(f"\nPONTUAÇÃO FINAL: {pontos[nome]['pontos']} pontos")
        relatorio += f"\nPONTUAÇÃO FINAL: {pontos[nome]['pontos']} pontos" + "\n"
        
        while True:
            criar_arquivo = input("Deseja gravar o resultado em arquivo texto? (S/N): ")
            if criar_arquivo == "S" or criar_arquivo == "s":
                with open(f'relatorio_{nome}.txt', 'w', encoding = 'utf-8') as arquivo:
                    arquivo.write(relatorio)
                input(f"\nRelatório gravado em: ./relatorios/relatorio_{nome}.txt.\nPressione ENTER para continuar...")
                
            elif criar_arquivo == "N" or criar_arquivo == "n":
                break
            else:
                input("Opção inválida. Tente novamente!\nPressione ENTER para continuar...")        
        break
        