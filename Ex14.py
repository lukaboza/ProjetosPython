'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que:
são descontados 11% para o Imposto de Renda
8% para o INSS e 5% para o sindicato
faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:
'''

ganho_hora = float(input('Informe seu ganho por hora: '))
horas_trabalhadas = float(input('Informe as horas trabalhadas: '))
salario_total = ganho_hora * horas_trabalhadas

ir = 0.11 * salario_total
inss = 0.08 * salario_total
sindicato = 0.05 * salario_total

salario_liquido = salario_total - (ir + inss + sindicato)

print(f'''Informações gerais:
salário bruto: R$ {salario_total: .2f}
IR: R$ {ir: .2f}
INSS: R$ {inss: .2f}
Sindicato: R$ {sindicato: .2f}
Salário liquido: R$ {salario_liquido: .2f}
''')
