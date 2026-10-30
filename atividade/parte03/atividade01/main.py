#importa o módulo de limpeza
from atividade.parte03.atividade01.modulo import limpar, peso_terra, peso_lua, peso_mercurio, peso_venus, peso_marte, peso_jupiter, peso_saturno, peso_urano, peso_netuno

peso = float(input("Digite o seu peso (kg): ").replace(",","."))

while True:
    limpar()
    print("Menu de opções")
    print("1 - Terra Padrão")
    print("2 - Lua")
    print("3 - Mercúrio")
    print("4 - Venus")
    print("5 - marte")
    print("6 - jupiter")
    print("7 - saturno")
    print("8 - urano")
    print("9 - netuno")
    
    match input("Escolha uma opção: "):
        case "1":

            print("Você escolheu a Terra")
            print(f"Seu peso na Terra é: {peso_terra(peso)} N")
        case "2":

            print("Você escolheu a Lua")
            print(f"Seu peso na Lua é: {peso_lua(peso)} N")
            
        case "3":

            print("Você escolheu Mercúrio")
            print(f"Seu peso em Mercúrio é: {peso_mercurio(peso)} N")
        case "4":
          
            print("Você escolheu Venus")
            print(f"Seu peso em Venus é: {peso_venus(peso)} N")
        case "5":
          
            print("Você escolheu Marte")
            print(f"Seu peso em Marte é: {peso_marte(peso)} N")
        case "6":
            limpar()
            print("Você escolheu Terra")
            print(f"Seu peso na Terra é: {peso_terra(peso)} N")
        case "7":
            limpar()
            print("Você escolheu Júpiter")
            print(f"Seu peso em Júpiter é: {peso_jupiter(peso)} N")
        case "8":
            limpar()
            print("Você escolheu Saturno")
            print(f"Seu peso em Saturno é: {peso_saturno(peso)} N")
        case "9":
            limpar()
            print("Você escolheu Urano")
            print(f"Seu peso em Urano é: {peso_urano(peso)} N")
        case "10":
            limpar()
            print("Você escolheu Netuno")
            print(f"Seu peso em Netuno é: {peso_netuno(peso)} N")
        case _:
            limpar()
            break
    input("\nPressione ENTER para continuar...")