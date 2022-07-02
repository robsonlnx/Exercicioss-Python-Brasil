area_a_ser_pintada = float(input('Informe a quantidade a ser pintada em m²: -> '))
cobertura_da_tinta = 3
capacidade_da_lata = 18
preco_da_lata = 80

litros_usados = area_a_ser_pintada / cobertura_da_tinta
latas_inteiras = int(litros_usados / capacidade_da_lata)

if litros_usados % capacidade_da_lata != 0:
    latas_inteiras += 1

valor_a_pagar = latas_inteiras * preco_da_lata

print(f'Serão necessario {litros_usados:.2f} litros de tinta.')
print(f'Será necessario {latas_inteiras} latas de tinta')
print(f'O valor a pagar será de R$ {valor_a_pagar:.2f}')