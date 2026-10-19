#importa as bibliotecas
import os
import time

# limpar o terminal
os.system("cls")

#declaração de dados 
n = int(input("informe um número inteiros: "))

while n >= 0:
    os.system("cls")
    print(f"{n}...")
    time.sleep(1)
    n -= 1
#use o shift + tab para sair dar identação
print("BOMMMM!!!!!!!!")