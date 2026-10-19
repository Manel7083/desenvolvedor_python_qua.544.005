# Declaração de variaveis
nome = input("infome seu nome: ").strip().title()
idade = int(input("informe sua idade: "))
#o stip ignora o espaço que o usario colar
#o title ele coloca as credenciais em maiusculas

#operador ternario
print(f"{nome} {'é maior de idade' if idade >= 18 else 'é menor de idade'}.")
