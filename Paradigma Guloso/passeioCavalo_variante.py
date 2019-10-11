# @ViniciusArdonyx
# ------------------------------------------------ #
# Autor: Vinicius Alves de Araujo - Mat.: 0011941
# ------------------------------------------------ #
#
# Nota:
## O paradigma utilizado foi o Guloso - enumera os candidatos e verifica qual esta mais proximo da proxima casa objetiva

def iniciaTabuleiro():
    tabuleiro = []
    valor = 1

    for i in range(0, 8, 1):
        tabuleiro.append([])
        for j in range(0, 8, 1):
            tabuleiro[i].append(valor)
            valor += 1
    
    return tabuleiro

def posicaoValorCasa(tab, valor):
    for i in range(0, 8, 1):
        if((valor >= tab[i][0]) and (valor <= tab[i][7])):
            for j in range(0, 8, 1):
                if(valor == tab[i][j]):
                    return [i,j]
        else:
            break
    
    return [-1,-1]

def atualizaListaAVisitar(visitar, valor):
    if(valor in visitar):
        visitar.remove(valor)
    
    return visitar

def atualizaListaMovimentos(lista, casa):
    if((lista == [])  or (lista[len(lista)-1] != casa)):
        lista.append(casa)
    
    return lista

def movimentosFuturoValidos(casa):
    validos = []

    if(((casa[0]+2) >= 0 and (casa[0]+2) <= 7) and ((casa[1]+1) >= 0 and (casa[1]+1) <= 7)):
        validos.append([(casa[0]+2), (casa[1]+1)])
    
    if(((casa[0]+1) >= 0 and (casa[0]+1) <= 7) and ((casa[1]+2) >= 0 and (casa[1]+2) <= 7)):
        validos.append([(casa[0]+1), (casa[1]+2)])
    
    if(((casa[0]-1) >= 0 and (casa[0]-1) <= 7) and ((casa[1]+2) >= 0 and (casa[1]+2) <= 7)):
        validos.append([(casa[0]-1), (casa[1]+2)])
    
    if(((casa[0]-2) >= 0 and (casa[0]-2) <= 7) and ((casa[1]+1) >= 0 and (casa[1]+1) <= 7)):
        validos.append([(casa[0]-2), (casa[1]+1)])
    
    if(((casa[0]-2) >= 0 and (casa[0]-2) <= 7) and ((casa[1]-1) >= 0 and (casa[1]-1) <= 7)):
        validos.append([(casa[0]-2), (casa[1]-1)])
    
    if(((casa[0]-1) >= 0 and (casa[0]-1) <= 7) and ((casa[1]-2) >= 0 and (casa[1]-2) <= 7)):
        validos.append([(casa[0]-1), (casa[1]-2)])
    
    if(((casa[0]+1) >= 0 and (casa[0]+1) <= 7) and ((casa[1]-2) >= 0 and (casa[1]-2) <= 7)):
        validos.append([(casa[0]+1), (casa[1]-2)])
    
    if(((casa[0]+2) >= 0 and (casa[0]+2) <= 7) and ((casa[1]-1) >= 0 and (casa[1]-1) <= 7)):
        validos.append([(casa[0]+2), (casa[1]-1)])

    return validos

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

def passeioCavalo(tab, visitar, lista, posicao_cavalo):
    while(visitar != []):
        # Procura se existe alguma casa com o movimento direto partindo da casa atual do cavalo
        for i in range(0, len(visitar), 1):
            atual = posicaoValorCasa(tab, visitar[i])

            # Existe um movimento direto entre a casa atual e a proxima
            if( (((atual[0] - posicao_cavalo[0]) == 2 or (atual[0] - posicao_cavalo[0]) == -2) and ((atual[1] - posicao_cavalo[1]) == 1 or (atual[1] - posicao_cavalo[1]) == -1)) or
                (((atual[0] - posicao_cavalo[0]) == 1 or (atual[0] - posicao_cavalo[0]) == -1) and ((atual[1] - posicao_cavalo[1]) == 2 or (atual[1] - posicao_cavalo[1]) == -2)) ):
                proximo = visitar[i]
                break
            else:
                proximo = visitar[0]
        
        proxima_casa = posicaoValorCasa(tab, proximo)
        melhor_encontrado = posicao_cavalo

        achou = False
        diferenca = 99999

        for mov in range(1, 9, 1):
            casa = movimentoCavalo(mov, posicao_cavalo)
            validos = []

            # Verifica se o movimento escolhido para ser realizado com o cavalo, o mantem dentro das dimensoes do tabuleiro
            if((casa[0] >= 0 and casa[0] <= 7) and (casa[1] >= 0 and casa[1] <= 7)):
                if(proximo == tab[casa[0]][casa[1]]):
                    melhor_encontrado = casa
                    break
                else:
                    if not(achou):
                        validos = movimentosFuturoValidos(casa)

                        for p_mov in range(1, 9, 1):
                            achou = False
                            pos = movimentoCavalo(p_mov, proxima_casa)

                            if((pos[0] >= 0 and pos[0] <= 7) and (pos[1] >= 0 and pos[1] <= 7)):
                                for v in validos:
                                    if(tab[v[0]][v[1]] == tab[pos[0]][pos[1]] or tab[v[0]][v[1]] == proximo):
                                        achou = True
                                        break
                        
                            if(achou):
                                melhor_encontrado = casa
                                break
                        
                        if(not(achou) and ((tab[casa[0]][casa[1]] - proximo) < diferenca)):
                            melhor_encontrado = casa
                            diferenca = (tab[casa[0]][casa[1]] - proximo)
                            
        posicao_cavalo = melhor_encontrado
        
        # Caso em uma das tentativas de chegar na casa mais proxima do cavalo, ocorra de passar em uma das casas que deseja visitar
        if(tab[melhor_encontrado[0]][melhor_encontrado[1]] in visitar):
            visitar = atualizaListaAVisitar(visitar, tab[melhor_encontrado[0]][melhor_encontrado[1]])

        # Adiciona a lista de passeio
        atualizaListaMovimentos(lista, tab[melhor_encontrado[0]][melhor_encontrado[1]])
    
    return lista

def main():
    # Lista para guardas as casas que o cavalo passou, o seu passeio no tabuleiro
    passeio = []
    lentrada = []
    tab = iniciaTabuleiro()

    # A entrada deve ser: "[valor, valor ...]"
    entrada = input()
    numero = ''

    for e in range(0, len(entrada), 1):
        if((entrada[e] != "[") and (entrada[e] != ",") and (entrada[e] != "]") and (entrada[e] != " ")):
            numero += entrada[e]

        if((entrada[e] == ",") or (entrada[e] == "]")):
            lentrada.append(int(numero))
            numero = ''

    # Copia a entrada
    visitar = []

    for i in range(0, len(lentrada), 1):
        visitar.append(int(lentrada[i]))

    casa_inicial = visitar[0]
    pos_partida = posicaoValorCasa(tab, casa_inicial)

    # Adiciona a lista de passeio
    atualizaListaMovimentos(passeio, casa_inicial)

    # Remove a casa inicial, pois ja foi visitada
    visitar = atualizaListaAVisitar(visitar, casa_inicial)

    # Chama a funcao gulosa para o passeio do cavalo
    passeio = passeioCavalo(tab, visitar, passeio, pos_partida)

    print("Quantidade de casas visitadas: ",len(passeio))
    print("Casas em que o cavalo passou: ",passeio)

if __name__ == '__main__':
    main()