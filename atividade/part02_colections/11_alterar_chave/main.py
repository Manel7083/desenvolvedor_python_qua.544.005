import os
# dicionario
usuario = {
    'nome': "thomas Anderson",
    'idade': 40,
    "email": "mranderson@gmail.com",
    'telefone': "(61) 9666-6666"
}
os.system("cls" if os.name == "nt" else "clear")

while True:
    #exibe o dicionario
    for chave, valor in usuario.items():
        print(f"{chave}: {valor}")

    #informe o nome da chave
    chave_escolhida = input("Informe o nome da chave que deseja alterar ou digite ou Enter para encerrar:").strip().lower()
    #verificar se a chave é valida

    if chave_escolhida in chave:
        #informe o novo valor
        usuario[chave_escolhida] = input("forme o novo valor: ").strip()
        continue
    else:
        break
