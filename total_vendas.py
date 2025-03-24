"""
Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia.
As vendas são informadas em uma única linha separadas por espaços.
Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.
"""


def soma_vendas(lista_vendas):
    """
    Calculates the total sum of sales from a list of sales values.
    Args:
        vendas (list): A list of sales values, where each value is expected to be
                       convertible to an integer.
    Returns:
        int: The total sum of the sales values.
    """

    return sum(int(valor) for valor in lista_vendas)


vendas = input("Digite os valores das vendas(separada por espaço): ").split(" ")

soma_total = soma_vendas(vendas)

print(f"O total de vendas foi: {soma_total}")


# valores = input("Digite os valores das vendas: ").split()
# total = sum(map(float, valores))
# print(f"O total de vendas foi: {total}")
