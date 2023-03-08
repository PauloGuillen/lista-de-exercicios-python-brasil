"""
Exercício 06 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele
mostre os números um ao lado do outro.

    >>> escrever_numeros_de_1_a_20(formato = 'um_abaixo_do_outro')
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    >>> escrever_numeros_de_1_a_20(formato = 'um_ao_lado_do_outro')
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
"""


def escrever_numeros_de_1_a_20(formato:str) -> str:
    """Escreva aqui em baixo a sua solução"""

    if formato == 'um_abaixo_do_outro':
        cararacter_end = '\n'
    else:
        cararacter_end = ' '
        
    for numero in range(1, 20):
        print(numero, end=cararacter_end)
    else:
        print(20) # para incluir o caracter fim de linha e ficar igual ao teste.
