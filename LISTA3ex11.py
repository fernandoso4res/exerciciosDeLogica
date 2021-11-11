#Faça um algoritmo que leia uma sequência de números terminada 
# em zero e mostre para cada número lido se ele é primo ou não. 
num = int(input("Digite um número: "))
while num != 0:
    i = num
    primo = True
    for i in range(2, num):
        if (num % i) == 0:
            primo = False
            break
    if (primo):
        print(f"{num} é um número primo")
    else:
        print(f"{num} não é um número primo")
    num = int(input("Digite um número: "))