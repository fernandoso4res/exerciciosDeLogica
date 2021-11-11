dia = int(input("Digite o dia do mês: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

data_ok = False

if((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11)):
    if((dia < 0) or (dia > 30)):
        data_ok = False
    else:
        data_ok = True
elif ((mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12)):
    if ((dia < 0) or (dia > 31)):
        data_ok = False
    else:
        data_ok = True
elif (mes == 2):
        if((ano % 4) == 0):
            if  dia < 0 or dia > 29:
                data_ok = False
            else:
                if dia < 0 or dia > 28:
                    data_ok = False
                else:
                    data_ok = True
else:
    data_ok = False
if (data_ok == True):
    print("Data válida")
else:
    print("Data inválida")