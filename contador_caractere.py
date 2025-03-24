"""
Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.
Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.
"""


def contador_caracteres(palavra):
    """
    Calculates the number of characters in a given word.

    Args:
        palavra (str): The word whose characters are to be counted.

    Returns:
        int: The total number of characters in the word.
    """
    return len(palavra)


texto = str(input("Digite uma palavra: "))

contar_caracteres = contador_caracteres(texto)

print(f"Essa palavra tem: {contar_caracteres} caracteres.")
