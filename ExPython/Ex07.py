'''
Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''

salario = float(input('Remuneração por hora: '))
horas = int(input('Horas trabalhadas no mês: '))

print(f'Seu salário no referido mês foi de: R$ {salario * horas}')