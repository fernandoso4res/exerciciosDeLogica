#Faça um algoritmo que leia dois números e mostre o maior número.

n1 = float(input("Digite o número: "))
n2 = float(input("Digite outro número: "))

if (n1 > n2):
    print(f"O número {n1} é maior que {n2}")
elif (n2 > n1):
    print(f"O número {n2} é maior que {n1}")
else:
    print(f"Os números {n1} e {n2} são iguais")
input()    