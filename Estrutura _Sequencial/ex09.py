temperatura_fahrenheit = float(input('Qual a temperatura a converter? -> '))
temperatura_celsius = 5 * (temperatura_fahrenheit - 32) / 9

print(f'{temperatura_fahrenheit} ºF é igual a {temperatura_celsius:.2f} ºC')