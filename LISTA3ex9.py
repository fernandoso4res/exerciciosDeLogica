#Faça um algoritmo que informe se um número é primo ou não. 
# Um número primo é aquele que é divisível por um e por ele mesmo. Por exemplo, 17 é um número primo.

num = int(input("Digite o número: "))
for i in range(2, num):
    if (num % i) == 0:
        print(f"Não é primo")
        break
else:
    print("É primo")
