#Faça um algoritmo que leia uma opção de um menu sendo [1] Soma, [2] Subtração, [3] Multiplicação e [4] Divisão. 
# Se a opção for válida, o programa deverá ler os operandos, realizar a operação e mostrar o resultado. 
# Caso contrário, o programa deverá exibir uma mensagem de operação inválida. 
# O programa termina quando o usuário digita 0.
print("O que deseja fazer ?")
print("*"*30)
print("[1] SOMA")
print("[2] SUBTRAÇÃO")
print("[3] MULTIPLICAÇÃO")
print("[4] DIVISÃO")
print("PARA SAIR DIGITE [0]")
opcao = int(input("Digite a opção: "))
while (opcao != 0):
    if (opcao == 1):
        parcela1 = float(input("Digite o 1º prdouto: "))
        parcela2 = float(input("Digite o 2º produto: "))
        soma = (parcela1 + parcela2)
        print(f"A soma é: {soma} ")
    elif (opcao == 2):
        minuendo = float(input("Digite o minuendo: "))
        subtraendo = float(input("Digite o subtraendo: "))
        diferenca = (minuendo - subtraendo)
        print(f"A diferença é: {diferenca}")
    elif (opcao == 3):
        fator1 = float(input("Digite o 1º fator: "))
        fator2 = float(input("Digite o 2º fator: "))
        produto = (fator1 * fator2)
        print(f"O produto é: {produto}")
    elif (opcao == 4):
        dividendo = float(input("Digite o dividendo: "))
        divisor = float(input("Digite o divisor: "))
        quociente = (dividendo / divisor)
        print(f"O quociente é: {quociente}")
    print("*"*30)
    print("O que deseja fazer ?")
    print("*"*30)
    print("[1] SOMA")
    print("[2] SUBTRAÇÃO")
    print("[3] MULTIPLICAÇÃO")
    print("[4] DIVISÃO")
    opcao = int(input("Digite a opção: "))