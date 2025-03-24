"""
Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços.
Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço.
"""

produtos = list(input("Digite os produtos separados por vírgula: ").split(","))

valores = list(input("Digite os preços separados por vírgula: ").split(","))

for produto, valor in zip(produtos, valores):
    print(f"{produto.strip()}: {valor.strip()}")
