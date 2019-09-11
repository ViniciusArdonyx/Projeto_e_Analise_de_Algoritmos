# @ViniciusArdonyx
# ------------------------------------------------ #
# Autor: Vinicius Alves de Araujo - Mat.: 0011941
# ------------------------------------------------ #
#
# Nota:
## Utiliza o timeit para imprimir na tela o tempo gasto em verificar uma jogada valida, caso nao queira,
## basta comentar as variaveis inicio e fim e o print logo abaixo da variavel fim no procedimento "passeioBCT".

import timeit

def pilhaVazia(pilha):
    if(len(pilha) == 0):
        return True

def empilha(p, postabuleiro):
    pilha = p
    pilha.append(postabuleiro)
    return pilha

def desempilha(p):
    pilha = p
    pilha.pop()
    return pilha

def iniciaTabuleiro():
    tabuleiro = []

    for i in range(0,8,1):
        tabuleiro.append([0]*8)

    return tabuleiro

def atualizaTabuleiro(tab, casa, lance):
    tab[casa[0]][casa[1]] = lance
    return tab

def desatualizaTabuleiro(tab, casa):
    tab[casa[0]][casa[1]] = 0
    return tab

# Representacao dos candidatos parciais
def movimentoCavalo(mov, ultcasacavalo):
    x = 0
    y = 0

    if(mov == 1):
        # Representa o movimento do cavalo: L
        y = ultcasacavalo[0] + 2
        x = ultcasacavalo[1] + 1
    elif(mov == 2):
        # Representa o movimento do cavalo: '᠁
        y = ultcasacavalo[0] + 1
        x = ultcasacavalo[1] + 2
    elif(mov == 3):
        # Representa o movimento do cavalo: :᠁
        y = ultcasacavalo[0] - 1 
        x = ultcasacavalo[1] + 2
    elif(mov == 4):
        # Representa o movimento do cavalo: ɼ
        y = ultcasacavalo[0] - 2 
        x = ultcasacavalo[1] + 1
    elif(mov == 5):
        # Representa o movimento do cavalo: Ꞁ
        y = ultcasacavalo[0] - 2 
        x = ultcasacavalo[1] - 1 
    elif(mov == 6):
        # Representa o movimento do cavalo: ᠁:
        y = ultcasacavalo[0] - 1 
        x = ultcasacavalo[1] - 2 
    elif(mov == 7):
        # Representa o movimento do cavalo: ᠁'
        y = ultcasacavalo[0] + 1
        x = ultcasacavalo[1] - 2 
    elif(mov == 8):
        # Representa o movimento do cavalo: ɺ
        y = ultcasacavalo[0] + 2
        x = ultcasacavalo[1] - 1

    novacasa = [y,x]
    return novacasa

def passeioBCT(pilha, tab, lance):
    if(lance > 64):
        print('\n\t Do topo do tabuleiro ate a base:\n')

        for i in range(0, len(tab), 1):
            print('________________________________________________________')
            print('|', end="")
            for j in range(0, len(tab[i]), 1):
                if(j == (len(tab[i])-1)):
                    print('  %d\t|' %tab[i][j])
                else:
                    print('  %d  |' %tab[i][j], end="")

        print('________________________________________________________')
        return True

    for mov in range(1,9,1):
        casa = movimentoCavalo(mov, pilha[len(pilha)-1])

        # Verifica se o movimento escolhido para ser realizado com o cavalo, o mantem dentro das dimensoes do tabuleiro e ainda nao foi visitado
        if((casa[0] >= 0 and casa[0] <= 7) and (casa[1] >= 0 and casa[1] <= 7)) and (tab[casa[0]][casa[1]] == 0):
            inicio = None
            inicio = timeit.default_timer() # Para registrar o inicio de um movimento do cavalo

            pilha = empilha(pilha, casa)
            tab = atualizaTabuleiro(tab, casa, lance)
            lance = lance+1

            if passeioBCT(pilha, tab, lance):
                return True

            lance = lance-1
            pilha = desempilha(pilha)
            tab = desatualizaTabuleiro(tab, casa)

            fim = None
            fim = timeit.default_timer() # Para registrar o fim de um movimento do cavalo
            # Apenas para mostrar que o algoritmo esta executando (exibindo o tempo gasto em cada movimento valido do cavalo no tabuleiro).
            # Tentando por forca bruta, todos os possiveis movimentos validos do cavalo, visitando todas as casas do tabuleiro.
            print('Um movimento do cavalo (Tempo execucao): %f' %(fim-inicio))
    
    return False

def main():
    pilha = []

    partida = [0,0]                          # Recebe par ordenado inicial no tabuleiro
    pilha = empilha(pilha, partida)          # Empilha o movimento de partida
    tab = iniciaTabuleiro()
    tab = atualizaTabuleiro(tab, partida, 1) # Salva as casas por onde o cavalo passou, salvando em qual lance ele parou na respectiva casa
    
    if not passeioBCT(pilha, tab, 2):
        print('\n\tSem solucao.\n')

if __name__ == '__main__':
    main()