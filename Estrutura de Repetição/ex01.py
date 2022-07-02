while True:

    try:
        numero = int(input('Digite um valor entre 0 e 10: '))

    except ValueError:

        print('Deve ser fornecido um valor inteiro')

    else:
        if 0 <= numero <= 10:
            print(f'Número informado é: {numero}')
            break

        else:
            print('O número informado deve estar entre 0 e 10')



