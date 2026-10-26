# TODO: parte 02 atividade 01
"""
Crie um programa que faça as seguintes operações:
-Cadastra novo usuário (nome, email, telefone, cpf)
-Lista todos os usuários cadastrados
-Altere os dados de um usuário
-Exclui um usuário
-Grava os dados de todos os usuários em um .json
-Abre arquivo .json e lista todos os usuários cadastrados nele
"""

import os
import json

usuarios = []

os.system("cls" if os.name == "nt" else "clear")

while True:
    print("1 - Cadastrar novo usuário")
    print("2 - Listar os usuarios")
    print("3 - Altere os dados do usuário")
    print("4 - Excluir um usuário")
    print("5 - Gravar os dados de todos os usuários em um .json")
    print("6 - Abrir o Arquivo Json")
    opcao = input("Opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            usuario = {}
            usuario['nome'] = input("Informe seu nome: ").strip().title()
            usuario['email'] = input("Informe seu email: ").strip().lower()
            usuario['telefone'] = input("Informe seu telefone: ").strip()
            usuario['cpf'] = input("Informe seu CPF: ").strip()

            usuarios.append(usuario)
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{usuario.get('nome')} Cadastro realizado com sucesso!")