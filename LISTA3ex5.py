#Faça um algoritmo que leia uma sequência de números inteiros terminado por zero 
#e mostre a soma, média, o maior número e o menor número da sequência.
soma = 0
maior = 0
menor = 0
cont = 0
validar = 0
n = int(input("Quantos números deseja repetir ? "))
for i in range(n):
    numero = int(input("Digite um numero: "))
    if ((numero % 10) == 0):
            soma = soma + numero
            if ((menor == 0) and (maior == 0) and (cont < 1 )):
                menor = numero 
                maior = numero 
                cont = cont + 1
            if (numero < menor):
                menor = numero
            elif (numero > maior):
                maior = numero
            validar = validar + 1 
    else:
        print("Esse número não termina em zero")
        break
if (validar == n):
    media = (soma / n)
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")
    print(f"Soma: {soma}")  
    print(f"Média: {media}")