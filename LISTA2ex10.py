#Faça um algoritmo que valide uma data, 
#formada por dia, mês e ano. Por exemplo, a data 30/2 é inválida,
#porém a data 29/2/2012 é válido.

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
data_ok = False
if ((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11)):
    if((dia < 1) or (dia > 30 )):
        data_ok = False
    else:
        data_ok = True
elif((mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12)):
    if(dia < 1 or (dia > 31)):
        data_ok = False
    else:
        data_ok = True
elif((mes == 2)):
    if((ano % 4 == 0)):
        if((dia < 1) or (dia >29)):
            data_ok = False
        else:
            data_ok = True
    elif((dia < 1) or (dia > 28)):
            data_ok = False
    else:
         data_ok = True
else:
    data_ok = False
if(data_ok == False):
    print("Data inválida")
else: 
    print("Data válida")
    
input()