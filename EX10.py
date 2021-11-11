#Faça um algoritmo que calcule o volume de uma caixa de água cilíndrica, sendo que
#os comprimentos do raio e a altura são informados pelo usuário. O volume é
#calculado multiplicando-se Pi, ao raio ao quadrado, a altura.

print("Faça um algoritmo que calcule o volume de uma caixa de água cilíndrica,")
print("sendo que os comprimentos do raio e a altura são informados pelo usuário.")
print("O volume é calculado multiplicando-se Pi, ao raio ao quadrado, a altura.")



import math

raiocilindro = float(input("Digite o raio do cilindro: "))
alturacilindro = float(input("Digite a altura do cilindro: "))
 
area = (raiocilindro ** 2) * (round(math.pi, 3 )) * alturacilindro

print(f"A área do cilindro é: {area}")  



input()













