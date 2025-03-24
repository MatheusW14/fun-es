"""
Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.
Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.
"""


def gerar_desconto(taxa_desconto):
    """
    Creates a discount function based on the given percentage.
    Args:
        porcentagem (float): The discount percentage to be applied.
    Returns:
        function: A function that takes a value as input and applies the discount.
    """

    def aplicar_desconto(preco):
        return preco * (1 - taxa_desconto / 100)

    return aplicar_desconto


porcentagem = float(input("Digite a porcentagem de desconto: "))
valor = float(input("Digite o valor da compra: "))

calcular_preco_final = gerar_desconto(porcentagem)
preco_final = calcular_preco_final(valor)

print(f"Preço final com desconto: R$ {preco_final:.2f}")


# def criar_desconto(porcentagem):
# def calcular_preco(valor):
# return valor - (valor * (porcentagem / 100))
# return calcular_preco

# desconto = float(input("Digite a porcentagem de desconto: "))

# calcular_preco_final = criar_desconto(desconto)

# valor = float(input("Digite o valor da compra: "))

# print(f"Preço final com desconto: {calcular_preco_final(valor)}")
