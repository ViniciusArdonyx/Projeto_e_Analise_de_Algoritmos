#
# ------------------------------------------------ #
# Autor: Vinicius Alves de Araujo - Mat.: 0011941
# ------------------------------------------------ #
#
# Nota:
## Utiliza o matplotlib para plotar os graficos, caso nao queira,
## basta comentar todos os procedimentos e chamadas de procedimentos iniciados em "plota...".

import matplotlib.pyplot as plt

def plotaGraficosR(R, opc):
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

	if(opc == 0):
		plt.title('SOLUÇÃO PARCIAL INICIAL')
		plt.savefig('solucao_parcial_inicial.png')
	else:
		plt.title('SOLUÇÃO FINAL')
		plt.savefig('solucao_final.png')

	plt.clf()

def passo(R, T):
	NovoR = []
	Raux  = R

	#Caso Base
	if(R == []):
		for i in range(0, len(T), 1):
			NovoR.append(T[i])

		NovoR.append(0)
		return NovoR
	elif(len(R) == 2):
		eR   = R[0]
		altR = R[1]
		eT   = T[0]
		altT = T[1]
		dT   = T[2]

		if(eR < eT):
			for i in range(0, len(R), 1):
				NovoR.append(R[i])

			Raux.pop(0)
			Raux.pop(0)

			NovoRaux = passo(Raux, T)

			for i in range(0, len(NovoRaux), 1):
				NovoR.append(NovoRaux[i])
			
		elif(eR == eT):
			if(altR > altT):
				T[1] = altR
			
			Raux.pop(0)
			Raux.pop(0)

			NovoRaux = passo(Raux, T)

			for i in range(0, len(NovoRaux), 1):
				NovoR.append(NovoRaux[i])

		elif(eR > eT and eR <= dT):
			if(altR > altT):
				T[0] = eR
				NovoR.append(eT)
				NovoR.append(altR)
				NovoR.append(eR)

			Raux.pop(0)
			Raux.pop(0)

			NovoRaux = passo(Raux, T)

			for i in range(0, len(NovoRaux), 1):
				NovoR.append(NovoRaux[i])

		elif(eR > eT and eR > dT):
			Raux.pop(0)
			Raux.pop(0)

			if(Raux == []):
				T = [eR]

			NovoRaux = passo(Raux, T)

			for i in range(0, len(NovoRaux), 1):
				NovoR.append(NovoRaux[i])

		return NovoR
	else:
		eR   = R[0]
		altR = R[1] 
		dR   = R[2]
		eT   = T[0]
		altT = T[1]
		dT   = T[2]

		if(eR < eT and dR < dT and eT < dR):
			NovoR.append(eR)
			NovoR.append(altR)
			
			if(altR > altT):
				T[0] = dR
				
			Raux.pop(0)
			Raux.pop(0)

			NovoRaux = passo(Raux, T)

			for i in range(0, len(NovoRaux), 1):
				NovoR.append(NovoRaux[i])
		
		elif(eR > eT and dR > dT and dT >= eR):
			NovoR.append(eT)
			NovoR.append(altT)

			if(altR > altT):
				T[0] = eR
				T[1] = altR
				T[2] = dR
			else:
				T[0] = dT
				T[1] = altR
				T[2] = dR

			Raux.pop(0)
			Raux.pop(0)

			NovoRaux = passo(Raux, T)

			for i in range(0, len(NovoRaux), 1):
				NovoR.append(NovoRaux[i])

		elif(eR < eT and dR > dT):
			if(altR < altT):
				NovoR.append(eR)
				NovoR.append(altR)
				NovoR.append(eT)
				NovoR.append(altT)

				T[0] = dT
				T[1] = altR
				T[2] = dR
			else:
				NovoR.append(eR)
				NovoR.append(altR)
			
			Raux.pop(0)
			Raux.pop(0)

			NovoRaux = passo(Raux, T)

			for i in range(0, len(NovoRaux), 1):
				NovoR.append(NovoRaux[i])

		elif(eR == eT and dR > dT):
			if(altR < altT):
				NovoR.append(eT)
				NovoR.append(altT)
				T[0] = dT
				T[1] = altR
				T[2] = dR
			else:
				NovoR.append(eR)
				NovoR.append(altR)
				T[1] = altR
				T[2] = dR

			Raux.pop(0)
			Raux.pop(0)

			NovoRaux = passo(Raux, T)

			for i in range(0, len(NovoRaux), 1):
				NovoR.append(NovoRaux[i])

		elif(eR >= eT and dR < dT):
			if(altR > altT):
				if(eR != eT):
					NovoR.append(eT)
					NovoR.append(altT)

				NovoR.append(eR)
				NovoR.append(altR)
				T[0] = dR

			Raux.pop(0)
			Raux.pop(0)

			NovoRaux = passo(Raux, T)

			for i in range(0, len(NovoRaux), 1):
				NovoR.append(NovoRaux[i])

		elif(eR == eT and dR == dT):
			if(altR > altT):
				T[1] = altR
			
			Raux.pop(0)
			Raux.pop(0)

			NovoRaux = passo(Raux, T)

			for i in range(0, len(NovoRaux), 1):
				NovoR.append(NovoRaux[i])
		
		elif(eR < eT and dR < dT):
			NovoR.append(eR)
			NovoR.append(altR)
			Raux.pop(0)
			Raux.pop(0)

			NovoRaux = passo(Raux, T)

			for i in range(0, len(NovoRaux), 1):
				NovoR.append(NovoRaux[i])

		elif(eR > eT and dR > dT):
			NovoR.append(eT)
			NovoR.append(altT)
			NovoR.append(dT)
			T[0] = eR
			T[1] = altR
			T[2] = dR

			Raux.pop(0)
			Raux.pop(0)

			NovoRaux = passo(Raux, T)

			for i in range(0, len(NovoRaux), 1):
				NovoR.append(NovoRaux[i])

	return NovoR

def main():
	R = [0,8,2,10,9,0,11,5,15,3,17,11,19,17,22,3,25,13,30,0]
	T = [8,6,23]

	#Teste com outro R e T
	#R = [3,15,7,12,12,0,15,10,20,8,24 ,0]
	#T = [2,10,9]

	#Opcional: comentar para nao plotar o grafico
	if(R != []):
		plotaGraficosR(R, 0) # 0 = ao grafico inicial

	#NovoR deve ser [0,8,2,10,9,6,11,6,15,6,17,11,19,17,22,6,25,13,30,0]
	NovoR = passo(R,T)
	print("\nNova Solucao: ", NovoR, "\n")

	#Opcional: comentar para nao plotar o grafico
	plotaGraficosR(NovoR, 1) # Qualquer outro valor = ao grafico da nova solucao(NovoR)

main()