def cadastrar_palpites():
    while True:
        apostador = input(f'Nome do apostador(a): ')
        print("\n", 8*"*", " ", f"Palpites de {apostador}", " ", 8*"*")
        print("1. Listar todos os jogos do bolão")
        print("2. Listar apenas jogos sem palpite")
        print("3. Cadastrar ou alterar placar de um jogo")
        print("4. Voltar ao menu principal \n")
        opção = input("Digite a opção desejada: ")
        
        if opção == 3:
            id = input("Digite o ID do jogo: ")
            print("\n Jogo encontrado:")
            
            print("\n Palpite atual:")
            
            print("\n Palpite cadastrado com sucesso!")
        break