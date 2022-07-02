produto_1 = float(input('Informe o preço do primeiro produto R$ '))
produto_2 = float(input('Informe o preço do segundo produto R$ '))
produto_3 = float(input('Informe o preço do terceiro produto R$ '))

if produto_1 < produto_2 and produto_1 < produto_3:
    print(f'Você deve comprar o produto que custa R$ {produto_1:.2f}')

elif produto_2 < produto_1 and produto_2 < produto_3:
    print(f'Você deve comprar o produto que custa R$ {produto_2:.2f}')

else:
    print(f'Você deve comprar o produto que custa R$ {produto_3:.2f}')
    

