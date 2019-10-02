#
# ------------------------------------------------ #
# Autor: Vinicius Alves de Araujo - Mat.: 0011941
# ------------------------------------------------ #
#
# Nota: 
## Utiliza o random para sortear uma das combinacoes possiveis das bases de tamanho 3.
## Utiliza o product para realizar as combinacoes e permutacoes de palavras de tamanho 3 usando as bases.
## O paradigma escolhido, foi o de Divisao e Conquista, quebrando o problema de gerar um genoma de tamanho n
## em um subgenoma de tamanho 3, quando n nao e divisivel por 3, realiza a operacao ate o maximo de divisoes
## possiveis com o 3 e realiza mais um passo com o restante que sobrou da divisao.

import random
from itertools import product

#Gera as possibilidades das 3 bases sem repetir um elemento consecutivo
def triplePossibilities():
    bases = ['X', 'P', 'E']
    permutacoes = []

    gerado = product(bases, repeat=3)

    for sub in gerado:
        if((sub[0] != sub[1]) and (sub[1] != sub[2])):
            permutacoes.append(sub)

    return permutacoes

#Gera um subgenoma(otimo local) onde nao ocorra duas subsequencias iguais adjacentes
def generateSubGenoma(subEntrada, adjacente, combinacoes):
    #Sorteia uma das combinacoes
    opc = random.choice(combinacoes)

    if(len(adjacente) > 0):
        while((opc[0] + opc[1]) == (adjacente[len(adjacente)-2] + adjacente[len(adjacente)-1]) or (opc[0] == adjacente[len(adjacente)-1])
            or ((adjacente[len(adjacente)-3] + adjacente[len(adjacente)-2]) == (adjacente[len(adjacente)-1] + opc[0]))):     
            opc = random.choice(combinacoes)
    
    pedacoGenoma = ""

    #O pedaco do genoma sera do tamanho da subEntrada passada e nao da opc escolhida
    for i in range(0, subEntrada, 1):
        pedacoGenoma += opc[i]

    return pedacoGenoma

def divideAndConquer(lentrada):
    lgenoma = []

    #Gera as possibilidades de combinacoes das 3 bases
    combinacoes = triplePossibilities()

    #Para cada valor de entrada na lista de entrada, faz-se:
    for e in range(0, len(lentrada), 1):
        #Primeiro ajusta o numero para que seja divisivel por 3, ja que sao tres tipos de "bases": {X,E,P}
        sobra = lentrada[e] % 3
        vezes = int((lentrada[e] - sobra) / 3)

        genoma = ""
        subGenoma = ""
        aux = subGenoma

        for i in range(0, vezes, 1):
            subGenoma = generateSubGenoma(3, aux, combinacoes)
            aux = subGenoma
            genoma += subGenoma
            
        #Se o numero inicialmente nao era divisivel por 3, executa mais uma vez passando o tamanho que falta para completar o valor informado
        if(sobra != 0):
            subGenoma = generateSubGenoma(sobra, aux, combinacoes)
            aux = subGenoma
            genoma += subGenoma

        lgenoma.append(genoma)
    
    return lgenoma

def main():
    lentrada = []

    while True:
        entrada = input()

        if(int(entrada) == 0):
            break

        if((int(entrada) >= 1) and (int(entrada) <= 5000)):
            lentrada.append(int(entrada))
        else:
            print("\n\t*ERRO: A entrada deve ser entre 1 e 5000.")
            break
    
    print("GENOMA: ", divideAndConquer(lentrada))

main()