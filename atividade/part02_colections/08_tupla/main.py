#git pull serve para atualizar seus arquivos locais com o arquivos do repositorio
import os
os.system("cls" if os.name == "nt" else "clear")
dias_da_semana = (
    "domingo",
    "segunda-feira",
    "terça-feira",
    "quarta-feira",
    "quinta-feira",
    "sexta-feira",
    "sabado"
)

for dia in dias_da_semana:
    print(dia)

#NOTE: se tentar alterar a tupla, o programa dá erro. Exemplo
try:
    dias_da_semana.sort()
    for dia in dias_da_semana:
        print(dia)
except Exception as e:
    print("nao foi possivel ordenar")
finally:
    print("programa encerrado")
