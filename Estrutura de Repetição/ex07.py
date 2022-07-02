maximo = float(input('Digite uma número: '))

for _ in range(4):
    maximo = max(maximo, float(input('Digite um número: ')))
    print(f'Número maximo encontrado até agora é: {maximo}')
