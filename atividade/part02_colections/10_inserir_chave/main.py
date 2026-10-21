# dicionario 
usuario = {
    'nome': "fulano de tal",
    'idade': 18,
    'emai': "fulano@gmail.com"
}
#usuario informa o nome da nova chave
nova_chave = input("Informe o nome da sua chave:").strip().lower()
#usuario informa o valor da nova chave
usuario[nova_chave] = input("Informe o valor da nova chave: ").strip()

#exibe o dicionario
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}.")