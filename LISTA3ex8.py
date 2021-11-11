#Uma progressão aritmética é uma sequência numérica em que cada termo, 
# a partir do segundo, é igual a soma do termo anterior com uma constante. 
# A constante é calculada como sendo a diferença entre o segundo e o primeiro número. 
# Faça um algoritmo que receba dois números inteiros e, 
# a partir dessa informação, gere uma sequência em progressão aritmética.


num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segndo termo: "))
i = 0 # Variável de controle
cons = (num2 - num1) # Constante
print(f"Primeiro termo: {num1}, segundo termo: {num2}")
while i < 10:
    num2 = cons + num2
    print(f"Progressão: {num2}") 
    i = i + 1