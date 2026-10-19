#and = e EXIGE QUE TODAS AS CONDIÇÕES SEJAM VERDADEIRAS
#or = ou EXIGE QUE PELO MENOS UMA SEJA VERDADEIRAS
#not = não INVERTE O RESULTADO
from queue import PriorityQueue


nome = input("Informe seu nome: ").strip().title()
idade = int(input("informe sua idade: "))
altura = float(input("informe sua altura: ").replace(",",".")) #o replace vai pegar o primeiro valor e converte para o segundo (a virgula vai ser entendida como ponto)

if idade >= 12 and altura >= 1.5:
    print(f"{nome} está autorizado a entrar.")
else:
    print(f"{nome} não está autorizado")    