"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""
import math


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    area = float(input(f"Informe o tamanho em metros quadrados da área:"))
    litros_necessarios = math.ceil(area / 6 * 1.1)

    numero_latas = math.ceil(litros_necessarios / 18)
    numero_galoes = math.ceil(litros_necessarios / 3.6)

    numero_latas_otimizadas = math.floor(litros_necessarios / 18)
    litros_faltantes = litros_necessarios - numero_latas_otimizadas * 18
    numero_galoes_otimizados = math.ceil(litros_faltantes / 3.5)

    print(f"Você deve comprar {litros_necessarios} litros de tinta.")
    print(f'Você pode comprar {numero_latas} lata(s) de 18 litros a um custo de R$ {numero_latas * 80:.0f}. Vão sobrar {numero_latas * 18 - litros_necessarios:.1f} litro(s) de tinta.')
    print(f'Você pode comprar {numero_galoes} lata(s) de 3.6 litros a um custo de R$ {numero_galoes * 25:.0f}. Vão sobrar {numero_galoes * 3.6 - litros_necessarios:.1f} litro(s) de tinta.')
    print(f'Para menor custo, você pode comprar {numero_latas_otimizadas} lata(s) de 18 litros e {numero_galoes_otimizados} galão(ões) de 3.6 litros a um custo de R$ {numero_latas_otimizadas * 80 + numero_galoes_otimizados * 25:.0f}. Vão sobrar {numero_galoes_otimizados * 3.6 - litros_faltantes} litro(s) de tinta.')
