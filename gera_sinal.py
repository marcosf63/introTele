#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

def gera_sinal(n):
    """
    função que recebe um numero inteiro como entrada e devolve
    um lista de bits (0 e 1) de tamanho n
    """
    sinal = []
    for i in range(n):
        sinal.append(randint(0,1))
    return sinal

def gera_grafico(sinal):
    print sinal

if __name__ == '__main__':
    n =  input('Digite o tamanho do sinal: ')
    print "Sinal gerado: ", 
    print gera_sinal(n)
