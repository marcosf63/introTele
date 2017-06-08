#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Trabablho da Disciplina Introdução as Telecomunicações
Aluno: Marcos Antonio Fernandes de Oliveira
Professor:  Anderson B Rodrigues
"""
from random import randint
import matplotlib.pyplot as plt

def gera_sinal(n):
    """
    função que recebe um numero inteiro como entrada e devolve
    um lista de bits (0 e 1) de tamanho n
    """
    sinal = []
    for i in range(n):
        sinal.append(randint(0,1))
    return sinal

def ger_x_do_grafico(sinal):
    """
    Gera uma lista com os x's do par (x,y) para construir o gráfico
    """
    x = []
    x.append(0)
    i = j = 1
    while i < (len(sinal) * 2):
        if (j < len(sinal)):
            x.append(j)
            x.append(j)
        i = i + 2
        j = j + 1
    x.append(len(sinal))
    return x

def ger_y_do_grafico(sinal):
    """
    Gera uma lista com os y's do par (x,y) para construir o gráfico
    """
    y = []
    for a,b in zip(sinal,sinal):
        y.append(a)
        y.append(b)
    return y


def gera_grafico(sinal):
    x = ger_x_do_grafico(sinal)
    y = ger_y_do_grafico(sinal)
    plt.axis([0, len(sinal)* 1.5, 0, 2])
    plt.plot(x, y, 'b-', lw=4)
    plt.show()

if __name__ == '__main__':
    n =  input('Digite o tamanho do sinal: ')
    print "Sinal gerado: ",
    s = gera_sinal(n)
    print s
    # print ger_x_do_grafico(s)
    # print ger_y_do_grafico(s)
    gera_grafico(s)
