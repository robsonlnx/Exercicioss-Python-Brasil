salario_por_hora = float(input('Salário por hora: R$ -> '))
horas_trabalhas_no_mes = int(input('Total de horas tralhadas: R$ -> '))
salario_bruto = salario_por_hora * horas_trabalhas_no_mes
imposto_de_renda = (salario_bruto * 11 / 100)
inss = (salario_bruto * 8 / 100)
sindicato = (salario_bruto * 5 / 100)
salario_liquido = salario_bruto - imposto_de_renda - inss - sindicato

print(f'+ Salário Bruto............:R$ {salario_bruto:.2f}')
print(f'- IR (11%).................:R$ {imposto_de_renda:.2f}')
print(f'- INSS (8%)................:R$ {inss:.2f}')
print(f'- Sindicato( 5%)...........:R$ {sindicato:.2f}')
print(f'= Salário Liquido..........:R$ {salario_liquido:.2f}')

