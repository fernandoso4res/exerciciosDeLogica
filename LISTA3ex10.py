num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
contador = 0
for i in range(num1, (num2+1)):
    primo = True
    if (i == 1):
        continue
    for j in range(2,i):
        if (i % j == 0):
            primo = False
            break
    if primo == True:
        print(f"{i} é um número primo")
        contador = contador + 1
print("*"*30)
print(f"Existem {contador} números primos")