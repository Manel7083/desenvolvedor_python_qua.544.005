
def limpar():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

def main():
    limpar()
    n = int(input("Digite um número inteiro positivo: "))
    print(fibonacci(n))

if __name__ == "__main__":
    main()