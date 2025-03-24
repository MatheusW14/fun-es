"""
Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento.
Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.
"""


def calculo_idade(ano_nascimento, ano_atual):
    """
    Calculates the age based on the year of birth and the current year.

    Args:
        ano_nascimento (int): The year of birth.
        ano_atual (int): The current year.

    Returns:
        int: The calculated age.
    """
    return ano_atual - ano_nascimento


nascimento = int(input("Digite o ano de nascimento: "))

atual = int(input("Digite o ano atual: "))

idade = calculo_idade(nascimento, atual)

print(f"A idade atual é: {idade} anos.")
