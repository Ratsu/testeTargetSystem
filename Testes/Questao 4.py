def calcular_faturamento_estados(faturamento_estados):

    total = sum(estado['valor'] for estado in faturamento_estados)
    
    for estado in faturamento_estados:
        porcentagem = (estado['valor'] / total) * 100
        print(f'A porcentagem do estado de {estado["estado"]} é de {porcentagem:.2f}%')
    
    return total

def main():

    faturamento_estados = [
        {"estado": "SP", "valor": 67836.43},
        {"estado": "RJ", "valor": 36678.66},
        {"estado": "MG", "valor": 29229.88},
        {"estado": "ES", "valor": 27165.48},
        {"estado": "Outros", "valor": 19849.53}
    ]

    total = calcular_faturamento_estados(faturamento_estados)

    print(f'O valor total é de R$: {total:.2f}')

if __name__ == "__main__":
    main()
