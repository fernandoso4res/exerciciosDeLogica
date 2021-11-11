#Faça um algoritmo que calcule o novo valor de um salário a partir de um valor
#percentual de reajuste. O valor atual do salário e o valor percentual do reajuste
#devem ser informados pelo usuário como, por exemplo, 7,3%.

print("Faça um algoritmo que calcule o novo valor de um salário a partir de um valor percentual de reajuste.")
print("O valor atual do salário e o valor percentual do reajuste devem ser informados pelo usuário como, por exemplo, 7,3%.")


salario = float(input("Digite o seu salário: ")) 
ajustepercentual =float(input("Digite o percentual de reajuste: "))
calculoporcentagem = salario * (ajustepercentual / 100)
salarioatual = salario + calculoporcentagem



print(f"Salario atual: {salarioatual}")

input()