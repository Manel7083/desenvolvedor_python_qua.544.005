#bibliotecas
import os
import json

#lista
usuarios = []

os.system("cls" if os.name == "nt" else "clear")

#loop
while True:
    #menu
    print("1 - Cadastrar novo usuário")
    print("2 - Listar usuários cadastrados")
    print("3 - Alterar dados do usuários")
    print("4 - Excluir um usuário")
    print("5 - Gravar todos os usuários em um .json")
    print("6 - Abrir arquivo .json")
    print("7 - Sair do programa")
    opcao = input("Opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            #inicializar um novo dicionario
            usuario = {}

            #informar os dados
            usuario['nome'] = input("Informe o nome do usuario: ").strip().title()
            usuario['email'] = input("Informe o email do usuario: ").strip().lower()
            usuario['telefone'] = input("Informe o telefone do usuario: ").strip()
            usuario['cpf'] = input("Informe o cpf do usuario: ").strip()

            #adicionar o novo usuario no dicionarios
            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{usuario.get('nome')} Cadastrado com sucesso.")
            
            continue
        case "2":
            for i, usuario in enumerate(usuarios):
                print(f"ID: {i}")   
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()}: {valor}")
                print(f"{'-'*40}")
            continue
        case "3":
            try:
                indice = int(input(f"informe o índice do usuário a ser alterado"))
                for chave, valor in usuarios[indice].items():
                    print(f"{chave.capitalize()}: {valor}")
                chave = input(f"Qual a chave deseja alterar o valor?").strip().lower()
                usuarios[indice][chave] = input("Informe o novo valor: ").strip()
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Dados de {usuarios[indice][chave]} de {usuarios[indice].get('nome')} Alterado com sucesso!")            
                continue
            except Exception as e:
                print(f"Não foi possivel atualizar os dados. {e}.")
        case "4":
            try:
                indice = int(input("Informe o ID a ser excluido: "))
                del usuarios[indice]
                os.system("cls" if os.name == "nt" else "clear")
                print("Usuario excluido com sucesso!")
                continue                                                    
            except Exception as e:
                print(f"Não foi possivel excluir. {e}.")
        case "5":
            arquivo = input(f"Informe o nome do arquivo: ").strip()
            with open(f"ativ01/{arquivo}.json", "w", encoding="utf-8") as f: #aqui ele cria um arquivo expecificando com o nome q o user escolhe
                #e o W serve para mandar ele ele escrever os dados no json com a linguagem utf8
                json.dump(usuarios, f)
            os.system("cls" if os.name == "nt" else "clear")
            print("Dados gravados com sucesso!")
        case "6":
            try:
                arquivo = input("Informe o nome do arquivo que deseja abrir: ").strip()
                with open(f"ativ01/{arquivo}.json","r", encoding="utf-8") as f:
                     usuarios = json.load(f)
                os.system("cls" if os.name == "nt" else "clear")
                print("Dados importados com sucesso!")
            except Exception as e:
                print(f"Não foi possível abrir o arquivo. {e}.")
        case "7":
            break
        case _:
            print("Opção invalida")

"""

TODO: parte 2 atividade 01
Crie um programa que faça as seguintes operações:
Cadastra novo usuário (nome, email, telefone. cpf)
listar todos os usuarios cadastrados
alterar os dados de um usuário
excluir um usuário
gravar os dados de todos os usuários em um .json
abre arquivos .json e lista todos os usuários cadastrados nele

"""