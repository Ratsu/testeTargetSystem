def inverter_string(texto):
    texto_invertido = texto[::-1]

    print(texto_invertido)




def main():

    texto = input("Digite o texto que será invertido: ")

    texto_invertido = texto[::-1]

    print(texto_invertido)


if __name__ == "__main__":
    main()