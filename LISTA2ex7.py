#Faça um algoritmo que calcule e mostre o novo valor de um salário a partir das seguintes regras: 
#salários de até R$ 1.000,00 inclusive recebem 30% de aumento,
#salários de até R$ 2.000,00 inclusive recebem 25%, 
#salários de até R$ 3.000,00 inclusive recebem 20%, 
#salários de até R$ 4.000,00 inclusive recebem 15% e 
#salários acima de R$ 4.000,00 recebem apenas 10%.

salario_atual = float(input("Digite o seu salário atual: "))
print("-"*30)

if (salario_atual <= 1000):
    aumento = (salario_atual * (30/100))
    salario_aumento = (salario_atual + aumento)
    print(f"O seu salário com aumento de 30% é: {salario_aumento}")
    print("-"*30)

elif (salario_atual <= 2000):
    aumento = (salario_atual * (25/100))
    salario_aumento = (salario_atual + aumento)
    print(f"O seu salário com 25% de aumento é: {salario_aumento}")
    print("-"*30)

elif (salario_atual <= 3000):
    aumento = salario_atual * (20/100)
    salario_aumento = (salario_atual + aumento)
    print(f"O seu salpario com 20% de aumento é: {salario_aumento}")
    print("-"*30)

elif (salario_atual <= 4000):
    aumento = (salario_atual * (15/100))
    salario_aumento = (salario_atual + aumento)
    print(f"O seu salário com 15% de aumento é: {salario_aumento}")

elif (salario_atual > 4000):
    aumento = (salario_atual * (10/100))
    salario_aumento = (salario_atual + aumento)
    print(f"O seu salário com 10% de aumento é: {salario_aumento}")
    print("-"*30)
input()