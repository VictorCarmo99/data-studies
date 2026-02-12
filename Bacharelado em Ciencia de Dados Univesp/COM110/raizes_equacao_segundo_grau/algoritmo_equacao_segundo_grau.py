#Algoritmo para calcular as raízes de uma equação de segundo Grau tipo Ax²+Bx+C, utilizando a fórmula de Bhaskara

#Inicio

#Variaveis
A = int(input("Valor de A: "))
B = int(input("Valor de B: "))
C = int(input("Valor de C: "))

#É uma equação do segundo grau?
if A == 0:
    print("Não é uma equação do 2º grau")
else: #Calcule o Delta
    D = B**2 - 4 * A * C
    if D <0:
        print("Não existem raízes reais!")
    else: #Calcule as Raizes
        r1 = (-B+D**(1/2))/(2*A)
        r2 = (-B-D**(1/2))/(2*A)
        print(f"As raízes da Equação são: {r1}, {r2}")

#Fim
