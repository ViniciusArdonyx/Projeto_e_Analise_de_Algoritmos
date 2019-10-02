#
# ------------------------------------------------ #
# Autor: Vinicius Alves de Araujo - Mat.: 0011941
# ------------------------------------------------ #
#
# Nota: Divisao e Conquista

import random

# Dicionario das bases
bases = {1: 'X',
         2: 'P',
         3: 'E'}

#Para uma cadeia ser estável, ela não pode ter duas subsequências iguais adjacentes.
def generateSubGenoma(subEntrada, adjacente):
    pedacoGenoma = ""
    
    #Sorteia um dos elementos do dicionario
    id, base = random.choice(list(bases.items()))

    if(len(adjacente) > 0):
            
    else:
        pedacoGenoma += base

##############
    while(len(pedacoGenoma) < subEntrada):
        #Sorteia um dos elementos do dicionario
        id, base = random.choice(list(bases.items()))

        #Adiciona a base sorteada se a string estiver vazia ou for diferente da ultima base adicionada
        if((len(pedacoGenoma) == 0) or (pedacoGenoma[len(pedacoGenoma)-1] != base)):
            if((len(adjacente) > 0) and (len(pedacoGenoma) > 0)):
                if((pedacoGenoma[len(pedacoGenoma)-1]+base) != (adjacente[len(adjacente)-2]+adjacente[len(adjacente)-1]) and 
                    (adjacente[0] != base)):
                    pedacoGenoma += base
            else:
                pedacoGenoma += base

    return pedacoGenoma

def divideAndConquer(lentrada):
    lgenoma = []

    #Para cada valor de entrada na lista de entrada, faz-se:
    for e in range(0, len(lentrada), 1):
        #Primeiro ajusta o numero para que seja divisivel por 3, ja que sao tres tipos de "bases": {X,E,P}
        sobra = lentrada[e] % 3
        vezes = int((lentrada[e] - sobra) / 3)

        #print("V: ",vezes," S: ",sobra)

        genoma = ""
        subGenoma = ""
        aux = subGenoma

        for i in range(0, vezes, 1):
            subGenoma = generateSubGenoma(3, aux)
            aux = subGenoma
            genoma += subGenoma
            
        #Se o numero inicialmente nao era divisivel por 3, executa mais uma vez passando o tamanho que falta para completar o valor informado
        if(sobra != 0):
            subGenoma = generateSubGenoma(sobra, aux)
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