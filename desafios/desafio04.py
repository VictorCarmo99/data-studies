#Desafio 04#
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

#Receber o input do Usuário#
entrada = input('Digite Algo: ')

#Analisar e Retornar na Tela#
print('\nPara: {}. Temos:\n'.format(entrada))
print('Contém alguma entrada de Dados?', bool(entrada))
print('Tipo Primitivo: ', type(entrada))
print('Só tem espaços?', entrada.isspace())
print('É Numérico? ', entrada.isnumeric())
print('É Alfabético? ', entrada.isalpha())
print('É Alfanumérico? ', entrada.isalnum())
print('Está em MAIUSCULAS? ', entrada.isupper())
print('Está em minúculas? ', entrada.islower())
print('Está Capitalizada? ', entrada.istitle())
