#Os endereços IP versão 4 são divididos em cinco classes: 
#A, B, C, D e E. 
#Os endereços no intervalo de 0 à 127 são classe A, 
#de 128 à 191 são classe B, de 192 à 223 são classe C, 
#de 224 à 239 são classe D e a partir de 240 são classe E. 
#Faça um algoritmo que leia o primeiro octeto, no formato decimal, de um endereço IP e informe a sua classe.

ip = int(input("Digite o primeiro octeto do IP: "))

if ((ip >= 0) and (ip <= 127)):
    print(f"O IP {ip}, pertence a classe A.")

elif ((ip >= 128) and (ip <= 191)):
    print(f"O IP {ip}, pertence a classe B.")

elif ((ip >= 192) and (ip <= 223)):
    print(f"O IP {ip}, pertence a classe C.")

elif ((ip >= 224) and (ip <= 239)):
    print(f"O IP {ip}, pertence a classe D.")

elif (ip >= 240):
    print(f"O IP {ip}, pertence a classe E.")

else:
    print("Não existe esse IP.")
input()