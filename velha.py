#!/bin/python3


# Autor: Gabriel Henrique Martinez Saraiva
# extremez3r0@gmail.com
#
# Universidade Estadual Paulista - "Júlio de Mesquita Filho"
# Instituto de Biociências, Letras e Ciências Exatas (IBILCE)
# Campus de São José do Rio Preto
#
# Departamento de Ciência de Computação e Estatística
# Grupo de Sistemas Paralelos e Distribuídos
# 
# Um simples jogo da velha!
#
# Fiz esse jogo em 23/09/2014, como primeiro programa feito em Python.
# Ainda estou aprendendo o tal do Python Thinking... que é bem dificil pra quem
# faz 12 anos que programa e já tem um modelo bem definido.
# Em breve pretendo otimizar esse códido... :)
#
# Agradecimentos: Ao careca do Jabuka que me amolou muito, e ao Tesouro que me 
# motivou :)
#
#===============================================================================


import os
import sys, traceback



def desenhaTabuleiro(tabuleiro):

    """ Desenha o tabuleiro com as jogadas,
            recebe como parâmetro a matriz do tabuleiro
    """

    print()
    print("      ",end="")

    traco = "+" + ("---+"*len(tabuleiro[0]))

    # Imprime as colunas...
    for (c,coluna) in enumerate(tabuleiro[0]):
        print("  ",c+1," ",end="",sep="")
    print()


    # Imprime o resto do tabuleiro com o número das linhas...
    for (l,linha) in enumerate(tabuleiro):

        print("     ",traco)
        print("   ",l+1,"  ",sep="",end="")

        for (c,elemento) in enumerate(linha):
            print("| ",elemento," ",sep="",end="")
        print("|")

    # Final do tabuleiro.
    print("     ",traco)



#===============================================================================
def obterCoordenadasDeJogada(jogador):
    while True:
        try:
            linha = int(input("Jogador "+jogador+" entre com a linha:"))
            coluna = int(input("Jogador "+jogador+" entre com a coluna:"))

            return linha,coluna

        except KeyboardInterrupt:
            print()
            print("Jogo abortado!")
            sys.exit(0)
        except:
            print("Por favor, insira números válidos!")
            continue

def executarJogada(jogador,tabuleiro):

    """ Executa uma jogada com o jogador especificado.
        Essa jogada é recebida, validada e executada nessa função
    """
    erro = True

    while erro:
        print()
        linha,coluna = obterCoordenadasDeJogada(jogador)

        linha = linha - 1
        coluna = coluna - 1
        linhas=len(tabuleiro)
        colunas=len(tabuleiro[0])

        if linha >= 0 and linha < linhas:
            if coluna >= 0 and coluna < colunas :
                erro = False

        if (erro):
            print("A posição entrada é inválida!")
            print("Por favor, tente novamente.")
            continue

        
        if tabuleiro[linha][coluna] != " ":
            erro=True
            print("Essa posição já está ocupada!")
            print("Por favor, tente novamente.")
            continue
        else:

            # Tudo ok, então realiza a jogada...
            tabuleiro[linha][coluna] = jogador



def limparTela():
    """ Função simples para limpar a tela utilizando caracteres de controle """
    print (chr(27) + "[2J")

def testarVitoria(a,t):
    """ Função que busca vitória no tabuleiro para o jogador especificado.
        Eu poderia ter feito essa função utilizando IFS simples sem laços,
        mas eu já sabia fazer assim, resolvi utilizar laços e brincar um pouco
        mais com python. (Mas suave nunca fez bom marinheiro)
    """
    # Sim, esse código não é o mais belo que eu escrevi... eu sei. Um dia irei 
    # refatorá-lo
   
    # é declarado vitória quando alguém obtem o número de pontos igual a ordem
    # do tabuleiro.
    
    pontos=0

    tamanho=len(t)

    # Busca vencedor nas linhas...
    for (i,linha) in enumerate(t):
        pontos=0
        for (j,coluna) in enumerate(linha):
            if t[i][j] == a:
                pontos=pontos+1
                if pontos==tamanho:
                    return True

    # Busca vencedor nas colunas
    for (i,linha) in enumerate(t):
        pontos=0
        for (j,coluna) in enumerate(linha):
            # Abuso de mapeamento, mas é python, então a zona está autorizada
            if t[j][i] == a:
                pontos=pontos+1
                if pontos==tamanho:
                    return True

    # Busca vencedor na diagonal principal
    pontos=0
    for (i,linha) in enumerate(t):
        if t[i][i] == a:
            pontos=pontos+1

    if pontos==tamanho:
        return True
    else:
        pontos=0

    # Busca vencedor na diagonal espelhada
    for (i,linha) in enumerate(t):
        if t[i][(tamanho-i)-1] == a:
            pontos=pontos+1

    if pontos==tamanho:
        return True
    else:
        return False



def main():
        
    linhas=colunas=3

    tabuleiro = [[" " for coluna in range(colunas)] for linha in range(linhas)]

    jogadores=["\033[1;31m✗\033[0m","\033[1;32m⚫\033[0m"]

    fim=False

    for i in range(1, linhas * colunas + 1):

        limparTela()

        jogador = jogadores[i%2]       

        print(" --- RODADA",i,"- Vez do Jogador",jogador,"---   ")
        desenhaTabuleiro(tabuleiro)
        executarJogada(jogador,tabuleiro)
        fim = testarVitoria(jogador,tabuleiro)

        if fim:
            limparTela()
            desenhaTabuleiro(tabuleiro)
            print()
            print(" ---> Jogador",jogador,"ganhou! <--- ")
            break;

        if i == linhas*colunas:
            print("Velha!!!")

    print()

if __name__ == "__main__":
    main()




# Ah, o mais importante de tudo, aos futuros leitores, que um dia por ventura,
# lerem isso, por favor, peço encarecidamente que desconsiderem essas linhas...
#
# CHUPA JABUKA SEU MORFÉTICO :) 
#
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
