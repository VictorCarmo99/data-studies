# Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

print('Gerador de Tabuadas Automático.\n')

n = int(input('Informe um número para gerar a tabuada: '))

# Tabuada
print(f'\n','='*12,'\n'
      f' Tabuada do {n}\n',
      f'='*12,'\n'
      f'{n:2} X  1 = {n * 1:2}\n'
      f'{n:2} X  2 = {n * 2:2}\n'
      f'{n:2} X  3 = {n * 3:2}\n'
      f'{n:2} X  4 = {n * 4:2}\n'
      f'{n:2} X  5 = {n * 5:2}\n'
      f'{n:2} X  6 = {n * 6:2}\n'
      f'{n:2} X  7 = {n * 7:2}\n'
      f'{n:2} X  8 = {n * 8:2}\n'
      f'{n:2} X  9 = {n * 9:2}\n'
      f'{n:2} X 10 = {n * 10:2}\n',
      f'='*12)
