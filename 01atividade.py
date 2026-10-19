# TODO: atividade 01
'''
Crie um programa que receba o nome, a massa em kg e a altura em metros do usuário, calcule seu IMC (índice de massa corporal) e finalize informado o diagnóstico do usuário com base no valor do IMC (se está magro, gordo, no peso ideal...)
'''
# NOTE: ATENÇÃO!!!! DIVIRTAM-SE!!!!

nome = input("Infome seu nome: ").strip().title()
peso = float(input("Infome seu peso em Kg: ").replace(",","."))
altura = float(input("Infome sua altura: ").replace(",","."))

imc = peso/(altura*altura)

print(f"{nome} seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você está abaixo do peso ideal.")
elif imc >= 18.5 and imc < 25:
    print("Você está no peso ideal.")
elif imc >= 25 and imc < 30:
    print("Você está acima do peso ideal.")
else:
    print("Você está obeso.")
    