'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
import math

metros = float(input('Informe o tamanho da area a ser pintada: '))
litros_usados = metros / 3

if litros_usados <= 18:
    print('1 Litro de tinta é sufuciente.')

latas = litros_usados / 18
latas = math.ceil(latas)
preco_final = latas * 80
print(f'Você precisa de {latas} latas')
print(f'Você pagará R${preco_final: .2f} ')
