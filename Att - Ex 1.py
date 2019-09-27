"""Usando o Thonny, escreva um programa em Python que leia uma tupla contendo 3 números inteiros, (n1, n2, n3) e os imprima em ordem crescente."""

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro: '))
n3 = int(input('Digite outro: '))

lista = (n1,n2,n3)
numeros_crescentes = sorted(lista)
print(numeros_crescentes)