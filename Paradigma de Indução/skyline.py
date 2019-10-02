#
# ------------------------------------------------ #
# Autor: Vinicius Alves de Araujo - Mat.: 0011941
# ------------------------------------------------ #
#
# Nota:
## Utiliza o matplotlib para plotar os graficos, caso nao queira,
## basta comentar todos os procedimentos e chamadas de procedimentos iniciados em "plota...".

import matplotlib.pyplot as plt

def plotaGraficosR(R):
    xBar = []
    yBar = []
    xSkyline = []
    ySkyline = [0]
    widthBars = []

	#Pega os valores para as listas X
    for i in range(0, len(R)-1, 2):
        xBar.append(R[i])
		#Para desenhar a linha do horizonte sobre o grafico de barras,
		#necessita de duas vezes as coordenadas de X
        xSkyline.append(R[i])
        xSkyline.append(R[i])

		#Calcula a largura das barras
        if(i != len(R)-2):
            widthBars.append((R[i+2]-R[i]))
        else:
            widthBars.append(0)

	#Pega os valores para as listas Y
    for i in range(1, len(R)-1, 2):
        yBar.append(R[i])
		#Para desenhar a linha do horizonte sobre o grafico de barras,
		#necessita de duas vezes as coordenadas de Y acrescida de 0 no inicio e fim
        ySkyline.append(R[i])
        ySkyline.append(R[i])

    yBar.append(0)
    ySkyline.append(0)
    
    #Gera o grafico
    plt.bar(xBar, yBar, widthBars, align='edge', fill=False)
    plt.plot(xSkyline, ySkyline, 'b--')
    plt.title('SOLUÇÃO FINAL')
    plt.savefig('solucao_final.png')
    
    plt.clf()

def passo(R, predios, pontos, maior):
    NovoR = []
    opcoes = []
    maiorh = -1

    if(pontos != []):
        #Cria uma lista das opcoes de predios entre o ponto atual
        for i in range(0, len(predios), 1):
            if((predios[i][0] <= pontos[0]) and (predios[i][2] > pontos[0])):
                opcoes.append(predios[i])

        #Procura dentro as opcoes, qual delas e o maior
        if(opcoes != []):
            for i in range(0, len(opcoes), 1):
                if(opcoes[i][1] > maiorh):
                    maiorh = opcoes[i][1]

            #Verifica se o maior encontrado nas opcoes eh diferente do maior atual dos pontos anteriores
            if(maiorh != maior):
                maior = maiorh
                NovoR.append(pontos[0])
                NovoR.append(maiorh)
        else:
            maior = -1
            NovoR.append(pontos[0])
            NovoR.append(0)
        
        #Recurssao
        NovoRaux = passo(NovoR, predios, pontos[1:], maior)
        
        for i in range(0, len(NovoRaux), 2):
            if(not([NovoRaux[i], NovoRaux[i+1]] in NovoR)):
                NovoR.append(NovoRaux[i])
                NovoR.append(NovoRaux[i+1])

    return NovoR

def main():
    R = []
    pontos = []
    lentrada = []

    #Recebe a entrada no terminal ate encontrar a entrada (0,0,0), significando fim de entrada
    while True:
        entrada = eval(input())
         
        if(list(entrada) != [0,0,0] and list(entrada) != [0, 0, 0]):
            lentrada.append(entrada)
        else:
            break

    #Separa apenas os pontos, deixa de fora as alturas
    for i in range(0, len(lentrada), 1):
        pontos.append(lentrada[i][0])
        pontos.append(lentrada[i][2])
    
    #Chama a funcao de realizara o skyline
    R = passo(R, lentrada, sorted(pontos), -1)
    print("Solucao: ",R)

    #Plota o histograma da solucao final
    if(R != []):
        plotaGraficosR(R)

main()