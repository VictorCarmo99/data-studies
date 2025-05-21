# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ')
# print('O tipo primitivo desse valor é ', type(a))
# print('Só tem espaços? ', a.isspace())
# print('É um número? ', a.isnumeric())
# print('É alfabético? ', a.isalpha())
# print('É alfanumérico? ', a.isalnum())
# print('Está em maiusculas? ', a.isupper())
# print('Esta em minusculas? ', a.islower())
# print('Está capitalizada? ', a.istitle())

#Professor Guanabara desafiou a usar .format para refazer o código:
print(f'O tipo primitivo desse valor é: {type(a)}\n'
      f'Só tem espaços? {a.isspace()}\n'
      f'É um número? {a.isnumeric()}\n'
      f'É alfabético? {a.isalpha()}\n'
      f'É alfanumérico? {a.isalnum()}\n'
      f'Está em maiusculas? {a.isupper()}\n'
      f'Está em minúsculas? {a.islower()}\n'
      f'Está capitalizada? {a.istitle()}')
