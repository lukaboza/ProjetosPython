'''
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''

n = float(input('Informe um valor: '))

if n > 0:
    print('O valor é positivo.')
elif n < 0:
    print('O valor é negativo.')
else:
    print('Você digitou 0, portanto não é positivo nem negativo.')