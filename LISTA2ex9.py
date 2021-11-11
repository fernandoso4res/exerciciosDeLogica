#Faça um algoritmo que receba um número inteiro, que representa um determinado mês do ano, 
#e mostre o nome do mês correspondente. 
#Por exemplo, se for informado o número 2, algoritmo deverá exibir fevereiro. 
#O algoritmo deve validar se a entrada está correta.

mes = int(input("Digite o número do mês: "))
if (mes == 1):
    print("Janeiro")
elif (mes == 2):
    print("Fevereiro")
elif (mes == 3):
    print("Março")
elif mes == 4:
    print("Abril")
elif (mes == 5):
    print("Maio")
elif (mes == 6):
    print("Junho")
elif (mes == 7):
    print("Julho")
elif (mes == 8):
    print("Agosto")
elif (mes == 9):
    print("Setembro")
elif (mes == 10):
    print("Outubro")
elif (mes == 11):
    print("Novembro")
elif (mes == 12):
    print("Dezembro")
else:
    print("Mês inválido")
input()