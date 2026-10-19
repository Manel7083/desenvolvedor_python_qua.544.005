import os

os.system("cls" if os.name == "nt" else"clear")

nome = input("informe seu nome: ").strip().title()
idade = int(input("informe sua idade: "))
idade_minina = None

while True:
    print(f"\nOlá {nome}, escolha um filme da lista abaixo:")
    print("1 - Vingadores: Ultimato (Sala 1) - Classificação: 12 anos")
    print("2 - Coringa (Sala 2) - Classificação: 18 anos")
    print("3 - Frozen 2 (Sala 3) - Classificação: Livre")

    sala = input("Sala Desejada: ").strip()

    #atribui a idade minima do filme
    match sala:
        case "1":
            idade_minina = 12
        case "2":
            idade_minina = 18
        case "3":
            idade_minina = 0
    #verifica a idade
    if idade >= idade_minina:
        print(f"Ingresso impresso para {nome}")
        print("tenha um bom filme")
        break
    else:
        os.system("cls" if os.name == "nt" else"clear") 
        print(f"Houve um problema você não tem idade minima para assistir o filme")
        print("Por Favor, escolha outro filme:")
        continue