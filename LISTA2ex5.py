#Faça um algoritmo que leia uma opção de um menu sendo 
#[1] Soma, [2] Subtração, [3] Multiplicação e [4] Divisão. 
#Se a opção for válida, o programa deverá ler os operandos, realizar a operação e mostrar o resultado. 
#Caso contrário, o programa deverá exibir uma mensagem de operação inválida.


print("Digite uma das opções abaixo: ")
print("[1] SOMA")
print("[2] SUBTRAÇÃO")
print("[3] MULTIPLICAÇÃO")
print("[4] DIVISÃO")
menu = int(input("Qual operação deseja realizar ?"))
print("-"*30)

if (menu == 1):
    parcela1 = float(input("Digite a primeira parcela: "))
    parcela2 = float(input("Digite a segunda parcela: "))
    soma = (parcela1 + parcela2)
    print("-"*30)
    print(f"O resultado da soma é: {soma} ")

    print("-"*30)
    

elif (menu == 2):
    minuendo = float(input("Digite o minuendo: "))
    subtraendo = float(input("Digite o subtraendo: "))
    resto = (minuendo - subtraendo)
    print("-"*30)
    print(f"O resto da divisão é: {resto}")

    print("-"*30)

elif (menu == 3):
    fator1 = float(input("Digite o primeiro fator: "))
    fator2 = float(input("Digite o segundo fator: "))
    produto = (fator1 * fator2)
    print("-"*30)
    print(f"O produto da multiplicação é: {produto}")
    print("-"*30)

elif (menu == 4):
    dividendo = float(input("Digite o dividendo: "))
    divisor = float(input("Digite o divisor: "))
    quociente = (dividendo / divisor)
    print("-"*30)
    print(f"O quociente da divisão é: {quociente}")
    print("-"*30)

else:
    print("Opção inválida!!")
    print("-"*30)
input()    