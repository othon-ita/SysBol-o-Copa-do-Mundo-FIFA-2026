#Nome e matrícula dos integrantes do grupo
#André Nicolas de Sousa Vieira - 605925
#Maria Eduarda da Silva Alves - 604390
#Othon Ítalo Nascimento de Moraes - 600006
import json
from funções.limpar import limpar
from funções.relatorio_apostador.pontuação_apostador import pontuação_apostador

def resultado_final():
    """Função responsável por retornar o resultado final do bolão, ou seja, a classificação dos apostadores. Exibindo a pontuação de todos os registrados no arquivo "apostadores.txt, a função gera uma tabela que usar como ordenação o maior ao menor acúmulo de pontos por participante. Em caso de empates na pontuação, o sistema se baseia, em ordem decrescente, nos seguintes atributos: número de placares exatos, placares parciais e resultados corretos; além de usar, em ordem crescente, os atributos de número de erros e ordem alfabética.

    Por fim, a função resultado_final questiona se o usuário deseja a gravação do relatório em arquivo de texto, para visualização posterior."""
    
    try:
        #Aquisição dos apostadores registrados
        with open ('./apostadores/apostadores.txt', 'r', encoding = 'utf-8') as arquivo:
            leitura = arquivo.read()
        
        #Declaração de dicionário para armazenar a pontuação dos apostadores
        tabela = {}
        for i in leitura.split():
            tabela.update(pontuação_apostador(i))
        
        #Ordenação da tabela por atributos
        tabela = dict(
        sorted(tabela.items(), key=lambda item: (
                -item[1]["pontos"],
                -item[1]["placar_exato"]["vezes"],
                -item[1]["placar_parcial"]["vezes"],
                -item[1]["resultado_correto"]["vezes"],
                item[1]["erros"]["vezes"],
                item[0]
            )))
        
        #Declaração da string que vai registrar os resultado final do bolão
        resultado_bolao = ""
        
        print(10*"*", "RESULTADO FINAL DO BOLÃO", 10*"*" + "\n")
        resultado_bolao += f"{10*'*'} RESULTADO FINAL DO BOLÃO {10*'*'}\n\n"
        
        print("Posição | Apostador | Pontos | Placar Exato | Placar Parcial | Resultado Correto | Erros\n")
        resultado_bolao += "Posição | Apostador | Pontos | Placar Exato | Placar Parcial | Resultado Correto | Erros\n\n"
        
        #Geração de linhas referentes à pontuação de cada apostador
        for i in range(len(tabela)):
            posição = f"{i+1}"
            if len(posição) == 1:
                print(f"{i+1}º   | {list(tabela.keys())[i]}   | {tabela[list(tabela.keys())[i]]['pontos']}   | {tabela[list(tabela.keys())[i]]['placar_exato']['vezes']}   | {tabela[list(tabela.keys())[i]]['placar_parcial']['vezes']}   | {tabela[list(tabela.keys())[i]]['resultado_correto']['vezes']}   | {tabela[list(tabela.keys())[i]]['erros']['vezes']}")
                resultado_bolao += f"{i+1}º   | {list(tabela.keys())[i]}   | {tabela[list(tabela.keys())[i]]['pontos']}   | {tabela[list(tabela.keys())[i]]['placar_exato']['vezes']}   | {tabela[list(tabela.keys())[i]]['placar_parcial']['vezes']}   | {tabela[list(tabela.keys())[i]]['resultado_correto']['vezes']}   | {tabela[list(tabela.keys())[i]]['erros']['vezes']}\n"
            elif len(posição) == 2:
                print(f"{i+1}º  | {list(tabela.keys())[i]}   | {tabela[list(tabela.keys())[i]]['pontos']}   | {tabela[list(tabela.keys())[i]]['placar_exato']['vezes']}   | {tabela[list(tabela.keys())[i]]['placar_parcial']['vezes']}   | {tabela[list(tabela.keys())[i]]['resultado_correto']['vezes']}   | {tabela[list(tabela.keys())[i]]['erros']['vezes']}")
                resultado_bolao += f"{i+1}º  | {list(tabela.keys())[i]}   | {tabela[list(tabela.keys())[i]]['pontos']}   | {tabela[list(tabela.keys())[i]]['placar_exato']['vezes']}   | {tabela[list(tabela.keys())[i]]['placar_parcial']['vezes']}   | {tabela[list(tabela.keys())[i]]['resultado_correto']['vezes']}   | {tabela[list(tabela.keys())[i]]['erros']['vezes']}\n"
            elif len(posição) == 3:
                print(f"{i+1}º | {list(tabela.keys())[i]}   | {tabela[list(tabela.keys())[i]]['pontos']}   | {tabela[list(tabela.keys())[i]]['placar_exato']['vezes']}   | {tabela[list(tabela.keys())[i]]['placar_parcial']['vezes']}   | {tabela[list(tabela.keys())[i]]['resultado_correto']['vezes']}   | {tabela[list(tabela.keys())[i]]['erros']['vezes']}")
                resultado_bolao += f"{i+1}º | {list(tabela.keys())[i]}   | {tabela[list(tabela.keys())[i]]['pontos']}   | {tabela[list(tabela.keys())[i]]['placar_exato']['vezes']}   | {tabela[list(tabela.keys())[i]]['placar_parcial']['vezes']}   | {tabela[list(tabela.keys())[i]]['resultado_correto']['vezes']}   | {tabela[list(tabela.keys())[i]]['erros']['vezes']}\n"
        
        #Verificação de desejo, ou não, da gravação do relatório final do bolão em arquivo texto
        while True:
            criar_arquivo = input("\nDeseja gravar o resultado em arquivo de texto? (S/N): ")
            if criar_arquivo == "S" or criar_arquivo == "s":
                with open(f'resultado_bolao.txt', 'w', encoding = 'utf-8') as arquivo:
                    arquivo.write(resultado_bolao)
                input(f"\nRelatório gravado em: /resultado_bolao.txt.\nPressione ENTER para continuar...")
                break
            elif criar_arquivo == "N" or criar_arquivo == "n":
                break
            else:
                input("Opção inválida. Tente novamente!\nPressione ENTER para continuar...")    
    #Para o caso de o arquivo "apostadores.txt" não estiver disponível
    except: 
        input("Ops! Parece que o arquivo 'apostadores.txt' não existe.\nPressione ENTER para voltar ao menu principal...")
        return
