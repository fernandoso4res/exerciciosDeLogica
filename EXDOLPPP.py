data = input("Entre com a data: ") # 13/3/1963
data = data.split("/") # [13, 3, 1963]
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])
meses30 = (4, 6, 9, 11) # tupla
meses31 = (1, 3, 5, 7, 8, 10, 12)
data_ok = False
if (mes in meses30):
    if ((dia < 1) or (dia > 30)):
        data_ok = False
    else:
        data_ok = True
elif (mes in meses31):
    if ((dia < 1) or (dia > 31)):
        data_ok = False
    else:
        data_ok = True
elif (mes == 2):
    if ((ano % 4) == 0):
        if ((dia < 1) or (dia > 29)):
            data_ok = False
        else:
            data_ok = True
    else:
        if ((dia < 1) or (dia > 28)):
            data_ok = False
        else:
            data_ok = True
else:
    data_ok = False
if (data_ok):
    print("Data válida")
else:
    print("Data inválida")