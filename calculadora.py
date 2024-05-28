def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    return x / y

def menu():
    print("\nCalculadora Digital")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

while True:
    menu()
    escolha = input("Escolha uma operação (1/2/3/4/5): ")

    if escolha == '5':
        print("Saindo da calculadora. Até logo!")
        break

    if escolha in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")
            continue

        if escolha == '1':
            print("Resultado:", adicionar(num1, num2))
        elif escolha == '2':
            print("Resultado:", subtrair(num1, num2))
        elif escolha == '3':
            print("Resultado:", multiplicar(num1, num2))
        elif escolha == '4':
            print("Resultado:", dividir(num1, num2))
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")