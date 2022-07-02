
peso_de_peixes = float(input('Informe a quantidade de peixe pescados: -> '))
excesso_peso = peso_de_peixes - 50
multa = excesso_peso * 4

if peso_de_peixes < 50:
    print(f'Você pescou {peso_de_peixes}kg de peixe. Está dentro da quantidade permitida,e não tem multa a pagar. ')
else:
    print(f'Você pescou {peso_de_peixes:.1f}kg de peixe. Houve um excesso de {excesso_peso:.1f}kg, e terá que pagar uma multa de R$ {multa:.2f}')


