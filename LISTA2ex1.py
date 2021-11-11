# Faça um algoritmo que leia um número e mostre se o mesmo é positivo, negativo ou zero.

numero = int(input("Digite um número: "))
if (numero < 0):
    print(f"Esse número {numero} é negativo")
elif (numero > 0):
    print(f"O número {numero} é positivo")
elif (numero == 0):
    print("Esse é o número zero")
input()