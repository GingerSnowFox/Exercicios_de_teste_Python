"""Escreva um programa em Python que leia um vetor de 5 números inteiros e o apresente na ordem inversa. Imprima o vetor no final. Use listas.
Exemplo: se a entrada for [4, 3, 5, 1, 2], o resultado deve ser [2, 1, 5, 3, 4]."""

lista_cinco = []
print ('Informe os cinco numeros inteiros que irão para o mundo invertido')
for i in range(5):
    lista_cinco.append(int(input('Numero '+ str(i+1) + ':\n')))
lista_cinco.reverse()
print (lista_cinco)

