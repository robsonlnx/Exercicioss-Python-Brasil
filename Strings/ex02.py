nome = 'Robson Oliveira'.upper()

nome_invertido_por_letras = ''.join(reversed(nome))
nome_invertido_por_palavras = ' '.join(reversed(nome.split()))

print(f'Nome com letras em maiusculo: {nome}')
print(f'Nome com letras em maiusculo invertido por letras: {nome_invertido_por_letras}')
print(f'Nome com letras em maiusculo invertido por palavras: {nome_invertido_por_palavras}')