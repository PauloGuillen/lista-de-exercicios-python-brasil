"""
Exercício 01 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo
até que o usuário informe um valor válido.

    >>> from secao_03_estrutura_de_repeticao import ex_01_numero_valido
    >>> ex_01_numero_valido.input = lambda k: '0'
    >>> ex_01_numero_valido.obter_numero_valido()
    0
    >>> entradas = ['1', 'a']
    >>> ex_01_numero_valido.input = lambda k: entradas.pop()
    >>> ex_01_numero_valido.obter_numero_valido()
    Número inválido: a
    1
    >>> entradas = ['0', 'a', '-1']
    >>> ex_01_numero_valido.input = lambda k: entradas.pop()
    >>> ex_01_numero_valido.obter_numero_valido()
    Número inválido: -1
    Número inválido: a
    0
    >>> entradas = ['10', 'a', '-1', '11']
    >>> ex_01_numero_valido.input = lambda k: entradas.pop()
    >>> ex_01_numero_valido.obter_numero_valido()
    Número inválido: 11
    Número inválido: -1
    Número inválido: a
    10


"""


def obter_numero_valido():
    """Escreva aqui em baixo a sua solução"""
    while True:
        try:
            str_numero = input('Dígite um número: ')
            numero = int(str_numero)
            if numero >= 0 and numero <= 10:
                print(numero)
                break
            print(f'Número inválido: {str_numero}')
        except:
            print(f'Número inválido: {str_numero}')
