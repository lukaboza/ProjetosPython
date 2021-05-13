'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

sexo = str(input('informe seu sexo: ')).upper()

while sexo not in 'F' or 'M':
    sexo = str(input('Sexo invalido, tente novamente: '))
    
if sexo in 'F':
    print('Sexo Feminino.')
elif sexo in 'M':
    print('Sexo masculino.')