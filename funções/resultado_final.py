import json
from funções.limpar import limpar
from funções.consultar_dados.verificar_existencia import verificar_existencia
from funções.relatorio_apostador.pontuação_apostador import pontuação_apostador

def resultado_final():
    while True:
        limpar()
        try:
            with open ('./apostadores/apostadores.txt', 'r', encoding = 'utf-8') as arquivo:
                leitura = arquivo.read()
                
            for i in leitura.split():
                tabela = pontuação_apostador(i)
            print(tabela)
            input()
            break
        except: 
            input("Ops! Parece que o arquivo 'apostadores.txt' não existe.\nPressione ENTER para voltar ao menu principal...")
            return