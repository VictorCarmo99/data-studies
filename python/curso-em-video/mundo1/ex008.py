# Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('Conversor de Unidades de Medida de Comprimento\n')

metros = float(input('Digite o valor a converter EM METROS: '))
cent = metros * 100
mili = metros * 1000

print(f'{metros}m convertido equivale à:\n'
      f'Centrimetros: {cent:.0f}cm\n'
      f'Milimetros: {mili:.0f}mm')
