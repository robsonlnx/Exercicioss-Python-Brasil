populacao_a = 80_000
populacao_b = 200_000
taxa_crescimento_de_a = 1.03
taxa_crescimento_de_b = 1.015
anos = 0

while populacao_a < populacao_b:
    # print(f'###### Populações no ano {anos}')
    # print(f'População de A: {populacao_a}')
    # print(f'População de B: {populacao_b}')
    anos += 1

    populacao_a *= taxa_crescimento_de_a
    populacao_a = int(populacao_a)

    populacao_b *= taxa_crescimento_de_b
    populacao_b = int(populacao_b)
    

print(f'###### Populações no ano {anos}')
print(f'População de A: {populacao_a}')
print(f'População de B: {populacao_b}')
