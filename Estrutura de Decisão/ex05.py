nota_1 = float(input('Digite a Primeira nota: '))
nota_2 = float(input('Digite a Segunda nota: '))
media = (nota_1 + nota_2) / 2

print(f'Sua média foi: {media}')

if media >= 10:
    print('Aprovado com distinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')
    