'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
'''

altura = float(input('Informe sua altura: '))
sexo = str(input('Informe seu sexo [M/F]: ')).upper()
while sexo not in 'MmFf':
    sexo = str(input('Sexo fornecido não idendificado, tente novamente [M/F]: '))

if sexo == 'M':
    peso_ideal_masc = (72.7 * altura) - 58
    print(f'Peso ideal do homem mencionado {peso_ideal_masc} Kg.')
if sexo == 'F':
    peso_ideal_fem = (62.1 * altura) - 44.7
    print(f'Peso ideal da mulher mencionada {peso_ideal_fem} Kg.')
