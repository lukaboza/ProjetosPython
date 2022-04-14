'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    - o produto do dobro do primeiro com metade do segundo.
    - a soma do triplo do primeiro com o terceiro.
    - o terceiro elevado ao cubo.
'''

n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe um número inteiro: '))
n3 = float(input('Informe um número real: '))

primeira_conta = ((n1*2) * (n2/2))
segunda_conta = ((n1 * 3) + n3)
terceira_conta = (n3**3)

print(f'o produto do dobro do primeiro com metade do segundo: {primeira_conta}')
print(f'a soma do triplo do primeiro com o terceiro: {segunda_conta}')
print(f'o terceiro elevado ao cubo: {terceira_conta}')