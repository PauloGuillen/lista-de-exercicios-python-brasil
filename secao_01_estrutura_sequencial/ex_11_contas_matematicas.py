"""
Exercício 11 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 1) o produto do dobro do primeiro com metade do segundo;
 2) a soma do triplo do primeiro com o terceiro;
 3) o terceiro elevado ao cubo.

 Apresente os resultados com duas casas decimais

    >>> from secao_01_estrutura_sequencial import ex_11_contas_matematicas
    >>> numeros = ['3.14', '43', '42']
    >>> ex_11_contas_matematicas.input = lambda k: numeros.pop()
    >>> ex_11_contas_matematicas.calcular_formulas()
    O produto do dobro do primeiro com metade do segundo é 1806.00
    A soma do triplo do primeiro com o terceiro é 129.14
    O terceiro elevado ao cubo é 30.96

"""


def calcular_formulas():
    """Escreva aqui em baixo a sua solução"""
    numero_inteiro_1 = int(input("Informe um número inteiro:"))
    numero_inteiro_2 = int(input("Informe outro número inteiro:"))
    numero_real = float(input("Informe um número real:"))
    dobro_metade = (numero_inteiro_1 * 2) * (numero_inteiro_2 / 2)
    print(f"O produto do dobro do primeiro com metade do segundo é {dobro_metade:.2f}")
    triplo_terceiro = (numero_inteiro_1 * 3) + numero_real
    print(f"A soma do triplo do primeiro com o terceiro é {triplo_terceiro:.2f}")
    print(f"O terceiro elevado ao cubo é {numero_real ** 3:.2f}")
