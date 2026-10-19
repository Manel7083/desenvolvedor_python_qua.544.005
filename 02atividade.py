# TODO: atividade 02
'''
Crie um programa em que o usuário informe uma única vez o nome e a idade, e em seguida, o programa exibe uma lista de filmes do cinema e suas respectivas salas e classificações indicativas.
O usuário deverá escolher a sala do filme desejado. Se tiver a idade mínima, o programa imprime o ingresso e encerra. Senão, o programa impede a entrada do usuário e retorna a lista para que o mesmo possa escolher outro filme.
'''
nome = input("Infome seu nome: ").strip().title()
idade = int(input("Infome sua idade: "))

while True:
    print(f"\nOlá {nome}, escolha um filme da lista abaixo:")
    print("1 - Vingadores: Ultimato (Sala 1) - Classificação: 12 anos")
    print("2 - Coringa (Sala 2) - Classificação: 18 anos")
    print("3 - Frozen 2 (Sala 3) - Classificação: Livre")

    escolha = int(input("Digite o número do filme que deseja assistir: "))
    
    if escolha == 1:
        if idade >= 12:
            print(f"\nIngresso para Vingadores: Ultimato (Sala 1) - Classificação: 12 anos")
            break
        else:
            print("\nDesculpe, você não tem idade suficiente para assistir a este filme. Por favor, escolha outro filme.")
    elif escolha == 2:
        if idade >= 18:
            print(f"\nIngresso para Coringa (Sala 2) - Classificação: 18 anos")
            break
        else:
            print("\nDesculpe, você não tem idade suficiente para assistir a este filme. Por favor, escolha outro filme.")
    elif escolha == 3:
        if idade >= 0:
            print(f"\nIngresso para Frozen 2 (Sala 3) - Classificação: Livre")
            break
        else:
            print("\nDesculpe, você não tem idade suficiente para assistir a este filme. Por favor, escolha outro filme.")
