# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# Apresentação do algoritmo
print('Olá! Eu sou Matemax, seu assistente pessoal de Matemática\n')

# Variaveis e calculos
n = int(input('Digite um Número: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print(f'\nPara {n}, temos as seguintes informações:'
      f'\nDobro: {d}'
      f'\nTriplo: {t}'
      f'\nRaiz Quadrada: {r:.2f}')
