numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
numero_3 = int(input('Digite mais um número: '))

if numero_1 > numero_2 and numero_1 > numero_3:
    print(f'Número: {numero_1} é maior')

elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f'Número: {numero_2} é maior')

else:
    print(f'Número: {numero_3} é maior')

