#tratamento de exeção
# try e o except funciona como um if e else
# se o try for interrompido é que ele que ele econtrou um erro e depois vai para o except
import os

os.system("cls")

try:
    nome = input("Informe seu nome: ").strip().title()
    idade = int(input("Informe sua idade: "))

    print(f"Nome do Usuário: {nome}")
    print(f"Idade do Usuário: {idade}")
except Exception as e:
    #O except Exception serve para vc vizualiar o erro
    print(f"Não foi possivel executar a ação! TU È MUITO BURRO KKKKKKKKKKKKKKKKKKKKKKKK {e}.")
finally:
    print("Programa finalizado com sucesso!")

# TODO: eu tenho que fazer essa merda 
# FIXME: a linha abaixo está errado
# REVIEW: a linha de codigo está funcionando mas precisa fazer de revisão