preco_unitario = 10
Desconto1 = 0.1
Desconto2 = 0.2
quantidade = int(input("Insira a quantidade que vai comprar: "))

if quantidade <= 10:
    valor_final = preco_unitario * quantidade
elif quantidade <= 20:
    valor_final = preco_unitario * quantidade * (1 - Desconto1)
else:
    valor_final = preco_unitario * quantidade * (1 - Desconto2)
print(f'o valor final da compra é: {valor_final}')
