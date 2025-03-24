"""
Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes estão armazenados como strings.
No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.
Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções,
uma que converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são inteiros:
"""


def converter_telefones(lista):
    """
    Converts a list of phone numbers from strings to integers.

    Args:
        lista (list): A list of phone numbers represented as strings.

    Returns:
        list: A list of phone numbers converted to integers.
    """
    return [int(telefone) for telefone in lista]


def verifica_tipos(lista):
    """
    Verifies if all elements in the given list are integers.
    Args:
        lista (list): A list of elements to be checked.
    Returns:
        str: A message indicating whether all elements are integers or if there was an error in the conversion.
    """

    for num in lista:

        if not isinstance(num, int):

            return "Erro na conversão."

    return "Todos os números foram convertidos corretamente!"


telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]

telefones_convertidos = converter_telefones(telefones)

print(verifica_tipos(telefones_convertidos))
