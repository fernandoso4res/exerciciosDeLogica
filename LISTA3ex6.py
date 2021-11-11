#Faça um algoritmo para mostrar a tabuada de 1 a 10.

for i  in range(1, 11):
    print("********"*10)
    print(f"Essa é a tabuada do {i}")
    for j in range(0, 11):
        print(f"{j} X {i} = {i * j}")