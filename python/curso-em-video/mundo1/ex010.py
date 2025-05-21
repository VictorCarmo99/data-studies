# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

print('\nConversor de Câmbio (Real → Dolar)\n')

valor = float(input('Valor disponível em Reais: R$'))
dolar = 6.2
convertido = valor / dolar

print(f'\nCotação do Dólar: U$1.00 = R${dolar:.2f}\n'
      f'Com R${valor:.2f} é possível comprar U${convertido:.2f}')
