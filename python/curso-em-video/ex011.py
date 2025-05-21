# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

# Apresentação do programa:
print('\nOlá, irei ajudar a calcular a quantidade necessária de tinta para sua obra\n'
      'Vamos considerar que 1L de tinta pinta 2m² de área da parede.\n')

#Variáveis:
print('me informe os seguintes valores da sua parede:')
l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))

#Cálculo e retorno ao usuário
print(f'Sua parede possui uma dimensão de {l} x {a} e uma área de {l*a:.1f}m².\n'
      f'Serão necessárias {l*a/2:.1f} latas para pinta-la')
