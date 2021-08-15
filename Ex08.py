'''
Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
'''

graus_f = int(input('Informe a temperatura em Fahrenheit: '))
graus = 5 * ((graus_f - 32)/ 9)

print(f'{graus_f} Fahrenheit corresponde a {graus} graus.')