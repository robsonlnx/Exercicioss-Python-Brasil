
horas_trabalhadas = int(input('Informe a quantidade de horas trabalhadas: '))
valor_da_hora = float(input('Informe o valor da hora trabalhada: '))
salario_bruto = horas_trabalhadas * valor_da_hora
inss = (salario_bruto * 10 / 100)
fgts = (salario_bruto * 11 / 100)
sindicato = (salario_bruto * 3 / 100)

if salario_bruto <= 900:
    imposto_de_renda = 0.00

elif salario_bruto <= 1500:
    imposto_de_renda = (salario_bruto * 5 / 100)

elif salario_bruto <= 2500:
    imposto_de_renda = (salario_bruto * 10 / 100)

else:
    imposto_de_renda = (salario_bruto * 20 / 100)

descontos = inss + sindicato + imposto_de_renda
salario_liquido = salario_bruto - descontos

print(f'Salário Bruto:                  : R$  {salario_bruto:.2f}')
print(f'(-) IR                          : R$  {imposto_de_renda:.2f}')
print(f'(-) INSS ( 10%)                 : R$  {inss:.2f}')
print(f'FGTS (11%)                      : R$  {fgts:.2f}')
print(f'Sindicato (3%)                  : R$  {sindicato:.2f}')
print(f'Total de descontos              : R$  {descontos:.2f}')
print(f'Salário Liquido                 : R$  {salario_liquido:.2f}')





