def calcular_fibo(var):
    print('Sequência Fibonacci')

    sequence = [0, 1]
    for i in range(2, 1000):
        next_number = sequence[i - 1] + sequence[i - 2]
        if next_number > (var * 2):
            break
        sequence.append(next_number)


    if var in sequence:
        print("O seu número faz parte da sequência de Fibonacci.")
    else:
        print("Seu número não faz parte da sequência de Fibonacci.")

    print('Sequência gerada até o primeiro número maior que o inserido:', sequence)


def main():

    var = None
    while True:
        try:
            var = int(input('Qual número você deseja calcular? '))
            break  
        except ValueError:  
            print("Por favor, insira um número inteiro válido.")


    calcular_fibo(var)

if __name__ == "__main__":
    main()
