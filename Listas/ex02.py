
lista = []

for _ in range(10):
    numero = float(input('Digite um número: '))
    lista.append(numero)
lista.sort(reverse=True)
print(lista)

