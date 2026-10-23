usuario = {
    'nome': "Emanuel",
    'idade': 18,
    'altura': 1.84,
    'email': "emanueloliveirasousa7083@gmail.com",
    'cpf':"123.456.789-12",
    'telefone':"(61)9 93573406"
    #obrigatoriamente a string precisa está em aspas duplas
}
#exibe valor especificico 
print(f"Nome: {usuario['nome']}")#se eu for usar para alteração de valores 
print(f"E-mail: {usuario.get('email')}")#se eu for usar para exibição de valores

for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}")
#obrigatorio em bancos de dados

