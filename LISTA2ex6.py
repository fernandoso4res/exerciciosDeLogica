#Faça um algoritmo que leia um caractere e informe se o mesmo é uma vogal ou não.

lista = ["a", "e", "i", "o", "u"]
 
char = input("Digite um caractere: ")

if (char in lista):
    print(f"{char}, é uma vogal")
else:
    print(f"{char}, não é uma vogal")
input()