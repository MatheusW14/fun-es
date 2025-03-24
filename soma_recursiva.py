"""
Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro.
Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário.
Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N
"""


def soma_recursiva(num):
    """
    Calculates the sum of all integers from 1 to n using recursion.

    Args:
        n (int): The integer up to which the sum is calculated. Must be a positive integer.

    Returns:
        int: The sum of all integers from 1 to n.

    Raises:
        RecursionError: If the recursion depth is exceeded for very large values of n.
        ValueError: If n is not a positive integer.
    """
    if num == 1:
        return 1
    return num + soma_recursiva(num - 1)


n = int(input("Digite um número: "))
resultado = soma_recursiva(n)
print(f"A soma de todos os números de 1 até {n} é: {resultado}")
