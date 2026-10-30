#limpesa

import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def peso_terra(peso):
    return peso * 9.81
def peso_lua(peso):
    return peso * 1.62
def peso_mercurio(peso):
    return peso * 3.70
def peso_venus(peso):
    return peso * 8.87
def peso_marte(peso):
    return peso * 3.71
def peso_jupiter(peso):
    return peso * 24.79
def peso_saturno(peso):
    return peso * 10.44
def peso_urano(peso):
    return peso * 8.69
def peso_netuno(peso):
    return peso * 11.15