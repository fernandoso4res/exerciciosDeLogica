n = int(input("Diigte quantos números você deseja repetir: "))
soma = 0
maior = 0
menor = 0
cont = 0
for i in range(n):
    numero = int(input("Digite um número: "))
    soma = soma + numero 
    if ((maior == 0) and (menor == 0) and (cont < 1)):
        menor = numero 
        maior = numero 
        cont = cont + 1
    if (numero > maior):
        maior = numero
    elif (numero < menor):
        menor = numero
print(f"A soma é: {soma}")
print(f"menor: {menor}")
print(f"maior: {maior}")
print(f"media: {soma / n}")

