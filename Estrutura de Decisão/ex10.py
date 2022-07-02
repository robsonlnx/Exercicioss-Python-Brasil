print('''Digite em qual turno você estuda. 
[ M ] Manhã
[ V ] Vespertino
[ N ] Noite''')

turno = input('Escolha sua opção: ').lower()

if turno == 'm':
    print('Bom dia!')

elif turno == 'v':
    print('Boa tarde!')

elif turno == 'n':
    print('Boa noite!')

else:
    print('Valor inválido!')