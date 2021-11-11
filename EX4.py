#Faça um algoritmo que calcule a gorjeta a ser paga de uma conta de restaurante. A
#gorjeta é calculada como sendo 10% do valor da conta, que deve ser informado pelo
#usuário

print("Faça um algoritmo que calcule a gorjeta a ser paga de uma conta de restaurante.")
print("A gorjeta é calculada como sendo 10 por cento do valor da conta,")
print("que deve ser informado pelo usuário")

valorConta = float(input("Valor da conta: "))
porcento = 10/100
gorjeta = valorConta * porcento
totalConta = valorConta + gorjeta   
print(f"O valor total da conta foi: {totalConta}")

input()