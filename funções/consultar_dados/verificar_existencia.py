import json

def verificar_existencia(caminho, tipo):
    """Verifica a existência de um arquivo JSON e retorna seu conteúdo se existir, caso contrário, exibe uma mensagem de erro e retorna None."""
    
    try:
        with open (f'{caminho}.json', 'r', encoding = 'utf-8') as arquivo:
            leitura = json.load(arquivo)
        return leitura
    except: 
        input(f"Ops! Você esqueceu de carregar {tipo}.\nPressione ENTER para continuar...")
        return None