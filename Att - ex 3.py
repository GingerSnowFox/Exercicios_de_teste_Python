"""3 -Usando o Thonny, escreva uma função em Python chamada potencia.
Esta função deve obter como argumentos dois números inteiros, A e B, e calcular AB usando multiplicações sucessivas
(não use a função de python math.pow) e retornar o resultado da operação.
Depois, crie um programa em Python que obtenha dois números inteiros do usuário e indique o resultado de AB usando a função."""


a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
potencia = 1
i   = 0
while i < b:
    potencia = potencia * a
    i   = i + 1 

print("O valor da potência é", potencia)

     