# numero_1 = int(input('Digite um número: '))
# numero_2 = int(input('Digite outro número: '))
# numero_3 = int(input('Digite mais um número: '))

numeros = []

for n in range(1, 4):
    numeros.append(int(input(f'Digite o {n}º número. ')))

numeros.sort(reverse=True)   
print(numeros)

