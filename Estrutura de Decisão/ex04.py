letras = input('Digite uma letra: ').lower()

if letras in 'a e i o u':
    print(f'A letra {letras} é uma vogal')

elif letras in 'bcdfghjlmnpqrstvxzkyw':
    print(f'A letra {letras} é uma consoante')

else:
    print('Você digitou uma palavra')
