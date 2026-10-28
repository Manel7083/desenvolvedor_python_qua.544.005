import os
def boas_vindas(nome):
    print(f"{nome}, seja bem-vindo")

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

#limpa o algoritmo principal
limpar
nome = input("Digite o seu nome: ").strip().title()
boas_vindas(nome)