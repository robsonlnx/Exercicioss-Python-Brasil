s1 = input('Digite uma String: ')
s2 = input('Digite outra String: ')

tamanho1 = len(s1)
tamanho2 = len(s2)

print(f'{s1}: {tamanho1} caracteres')
print(f'{s2}: {tamanho2} catarcteres')

comapracao_de_tamanho = 'diferentes'
comapracao_de_conteudo = 'diferente'

if s1 == s2:
    comapracao_de_tamanho = 'iguais'
    comapracao_de_conteudo = 'igual'
    
elif tamanho1 == tamanho2:
    comapracao_de_tamanho = 'iguais'


print(f'As duas strings são de tamanhos {comapracao_de_tamanho}')

print(f'As duas strings possuem conteudo {comapracao_de_conteudo}')