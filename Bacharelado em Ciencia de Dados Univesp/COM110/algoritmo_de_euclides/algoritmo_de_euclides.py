#Escreva um programa que receba dois números inteiros positivos (A e B), calcule e mostre o valor do MDC entre eles. Para calcular o MDS utilize o Algoritmo de Euclides, cujo pseudo-código está a seguir.
#Dados A e B números inteiros e positivos
#Enquanto B for diferente de 0, repita:
    #resto = resto da divisão entre A e B;
    #A = B;
    #B = resto
#MDC = A

#Declaração de Váriaveis:
A = int(input("Valor de A: "))
B = int(input("Valor de B: "))

A_ori = A
B_ori = B

#Algoritmo de Euclides:
while B != 0:
    resto = A % B
    A = B
    B = resto
MDC = A

#Output em texto:
print(f'O MDC de {A_ori} e {B_ori} é: {MDC}')
