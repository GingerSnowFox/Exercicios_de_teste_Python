"""6 - Escreva uma função em Python que leia uma tupla contendo números inteiros, retorne uma lista contendo somente os números ímpares e uma nova tupla
contendo somente os elementos nas posições pares."""

tupla= []
print ('Informe 5 valores inteiros e diferentes para separarmos')
def lista_impar(tupla):
    impar=[]
    for i in range (5):
        tupla.append(int(input('Numero '+ str(i+1) + ':\n')))
        if tupla[i] % 2 != 0:
            impar.append(tupla[i])
    return (impar)
def tupla_pares(tupla):
    return [i for i in tupla if i % 2 == 0 ]

print(lista_impar(tupla))
print(tupla_pares(tupla))