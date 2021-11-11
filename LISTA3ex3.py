#Faça um algoritmo que leia uma sequência de 20 números inteiros 
#e mostre a soma, média, o maior número e o menor número da sequência
soma = 0
maior = 0
menor = 0
cont = 0
for i in range(3):
    numero = int(input("Digite um número: "))
    soma = soma + numero
    if ((menor == 0) and (maior == 0) and (cont < 1)):
        maior = numero
        menor = numero 
        cont = cont + 1
    if (numero < menor):
        menor = numero
    elif (numero > maior):
        maior = numero
media = (soma / 3)
print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}")
print(f"A soma é: {soma}")
print(f"A média é: {media}")