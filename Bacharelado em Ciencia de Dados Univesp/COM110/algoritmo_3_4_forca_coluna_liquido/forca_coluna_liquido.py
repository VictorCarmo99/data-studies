#Algoritmo 3.4 Algoritmo para calcular a força exercida pela coluna de um líquido.
#Início
#1. Ler os valores h, d e gama.
#2. Calcular F pi* gama * sqr(d) *h/4.
#3. Exibir o valor de F.
#Fim


#Declaração das variáveis:
from math import pi
h = float(input("Insira a Altura h (m): "))
d = float(input("Insira o Diâmetro d (m): "))
gama = float(input("Insira o Peso Específico do Líquido gama (N/m^3): "))

#Cálculo de F:
F = pi * gama * d**2 * h / 4

#Output de F
print(f'A Força Exercída pela coluna de líquido é: {F:.2f}')
