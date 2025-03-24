"""Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.
Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().
"""

lista_numeros = input("Digite os números separados por espaço: ").split()

numeros_pares = list(filter(lambda x: int(x) % 2 == 0, lista_numeros))

print("Numeros pares:", " ".join(numeros_pares))
