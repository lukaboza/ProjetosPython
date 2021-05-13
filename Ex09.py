'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''

graus_c = int(input('Informe a temperatura em graus: '))
graus_f = (graus_c * (9 / 5)) + 32

print(f'{graus_c} graus corresponde a {graus_f} fahrenheit')