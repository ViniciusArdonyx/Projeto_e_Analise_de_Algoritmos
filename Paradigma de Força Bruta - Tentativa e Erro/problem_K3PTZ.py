#
# ------------------------------------------------ #
# Autor: Vinicius Alves de Araujo - Mat.: 0011941
# ------------------------------------------------ #
#
# Nota: 
## Utiliza o random para embaralhar os candidatos, para que nao fique sempre a mesma ordem de opcoes de escolhas
## O paradigma escolhido, foi o de Tentativa e Erro.

import random

# Usado para sortear uma vez para dar valor aos candidatos, para nao ficar sempre a mesmas opcoes
def ordemCandidatos(bases):
    ordem = []

    while(bases != []):
        sorteado = random.choice(bases)
        ordem.append(sorteado)
        bases.remove(sorteado)

    return ordem

# Retorna como ficou o genoma apos a escolha de uma opcao
def escolheBaseParaGenoma(ordem, opc, genoma):
    if(opc == 1):
        genoma += str(ordem[0])
    elif(opc == 2):
        genoma += str(ordem[1])
    elif(opc == 3):
        genoma += str(ordem[2])

    return genoma

# Gera o genoma atraves da tentativa e erro
def gerarGenoma(entrada, passo, genoma):
    if(passo > entrada):
        return genoma
    
    # Bases existentes
    bases = ['X', 'P', 'E']
    ordem = ordemCandidatos(bases)

    # A quantidade de escolhas de base possivel
    for opc in range(1, 4, 1):
        novo_genoma = escolheBaseParaGenoma(ordem, opc, genoma)
        pos = 1
        
        # Verifica se a opcao escolhida, mantem o genoma valido, ou seja, sem subsequentes adjacentes
        while(pos <= len(genoma)):
            fim = 0

            while(pos != fim):
                if(genoma[len(genoma)-(pos+fim):len(genoma)-fim] == novo_genoma[len(novo_genoma)-pos:len(novo_genoma)]):
                    novo_genoma = ''
                    break

                fim += 1

            if(novo_genoma == ''):
                break
            else:
                pos += 1

        if(novo_genoma != ''):
            passo += 1
            genoma = gerarGenoma(entrada, passo, novo_genoma)
            return genoma
    
    return ''

def main():
    genoma = ''
    passo = 1

    entrada = int(input())

    if((entrada >= 1) and (entrada <= 5000)):
        while(genoma == ''):
            genoma = gerarGenoma(entrada, passo, genoma)
    else:
        print("\n\t*ERRO: A entrada deve ser entre 1 e 5000.")
        exit(0)

    print(genoma)

if __name__ == '__main__':
    main()