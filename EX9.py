#Faça um algoritmo que calcule a área de uma esfera, sendo que o comprimento do
#raio é informado pelo usuário. A área da esfera é calculada multiplicando-se 4 vezes
#Pi ao raio ao quadrado.

print("Faça um algoritmo que calcule a área de uma esfera,")
print("sendo que o comprimento do raio é informado pelo usuário.")
print("A área da esfera é calculada multiplicando-se 4 vezes Pi ao raio ao quadrado.")


raioesfera = float(input("Informe o raio da esfera: "))
pi = (3.14 * 4)
calculoesfera = (raioesfera ** 2) * pi

print(f"A área da esfera é: {calculoesfera}")

input()