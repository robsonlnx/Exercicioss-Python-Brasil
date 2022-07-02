salario = float(input('Informe seu salário: R$: '))

if salario <= 280:
    novo_salario = (salario * 20 / 100) + salario
    valor_aumento = salario * 20 / 100
    print(f'Salário antes do reajuste: R$ {salario}')
    print(f'O percentual de aumento foi de 20%')
    print(f'O valor do aumento foi de R$ {valor_aumento}')
    print(f'Novo salário é de R$ {novo_salario}')
   
elif salario <= 700:
    novo_salario = (salario * 15 / 100) + salario
    valor_aumento = salario * 15 / 100
    print(f'Salário antes do reajuste: R$ {salario:.2f}')
    print(f'O percentual de aumento foi de 15%')
    print(f'O valor do aumento foi de R$ {valor_aumento:.2f}')
    print(f'Novo salário é de R$ {novo_salario:.2f}')
   
elif salario <= 1500:
    novo_salario = (salario * 10 / 100) + salario
    valor_aumento = salario * 10 / 100
    print(f'Salário antes do reajuste: R$ {salario:.2f}')
    print(f'O percentual de aumento foi de 10%')
    print(f'O valor do aumento foi de R$ {valor_aumento:.2f}')
    print(f'Novo salário é de R$ {novo_salario:.2f}')
    
elif salario > 1500:
    novo_salario = (salario * 5 / 100) + salario 
    valor_aumento = salario * 5 / 100
    print(f'Salário antes do reajuste: R$ {salario:.2f}')
    print(f'O percentual de aumento foi de 5%')
    print(f'O valor do aumento foi de R$ {valor_aumento:.2f}')
    print(f'Novo salário é de R$ {novo_salario:.2f}')