#Faça um algoritmo que leia uma sequência de caracteres terminada por um ponto e mostre o número de vogais da frase. Cada caractere deve ser digitado/lido separadamente.

#Exemplo:

#Entre com um caractere: a
#Entre com um caractere: @
#Entre com um caractere: x
#Entre com um caractere: 2
#Entre com um caractere: e
#Entre com um caractere: .
#Número de vogais: 2
caractere = input("Digite o caractere: ")
vogais = 0
while caractere != ".":
    if caractere =="a" or caractere =="e" or caractere =="i" or caractere =="o" or caractere =="u":
        vogais += 1
    caractere = input("Digite o caractere: ")
print("O numero de vogais eh", vogais)
