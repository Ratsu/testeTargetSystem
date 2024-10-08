
import json

# Abre o arquivo JSON
with open("dados.json") as file:
    dados = json.load(file)

lista = []
auxDia = 0
maiorValor = 0
diaMaiorValor = 0
menorValor = None
diaMenorValor = 0
valorMedio = 0


for i in dados:
    valorMedio += i['valor']

    if i['valor'] != 0:

        if i['valor'] > maiorValor:
            maiorValor = i['valor']
            diaMaiorValor = i['dia']
        
        if menorValor is None or i['valor'] < menorValor:
            menorValor = i['valor']
            diaMenorValor = i['dia']
    
    lista.append((i['dia'], i['valor']))
    
    if i['valor'] == 0:
        auxDia -= 1

ultimo_dia = lista[-1][0]
auxDia = ultimo_dia + auxDia

valorMedio = valorMedio / auxDia


if diaMenorValor is not None:
    print(f'O valor medio é R$: {valorMedio:.2f}')

if diaMaiorValor is not None:
    print(f"O maior valor é R$: {maiorValor:.2f} e ocorreu no dia {diaMaiorValor}.")

if diaMenorValor is not None:
    print(f"O menor valor é R$: {menorValor:.2f} e ocorreu no dia {diaMenorValor}.")




