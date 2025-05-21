# Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('Olá! Vamos Calcular a Média das suas notas da escola?\n')

materia = input('Disciplina: ')

t1 = float(input('Primeiro Trimestre: '))
t2 = float(input('Segundo Trimestre: '))
t3 = float(input('Terceiro Trimestre: '))
t4 = float(input('Quarto Trimestre: '))

media = (t1 + t2 + t3 + t4) / 4

print(f'A média das suas notas esse ano em {materia} foi de: {media}')
