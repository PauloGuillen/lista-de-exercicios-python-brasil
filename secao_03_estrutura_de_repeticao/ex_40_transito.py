"""
Exercício 40 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os
1) seguintes dados:
2) Código da cidade;
3) Número de veículos de passeio (em 1999);
4) Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:

1) Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
2) Qual a média de veículos nas cinco cidades juntas;
3) Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

Mostre os valores com uma casa decimail

    >>> calcular_estatisticas(('SJC', 190_000, 300), ('SP', 1_000_000, 2_000 ),
    ... ('BH', 800_000, 1000), ('FZ', 600_000, 700), ('FL', 150_000, 900)
    ... )
    O maior índice de acidentes é de FL, com 6.0 acidentes por mil carros.
    O menor índice de acidentes é de FZ, com 1.2 acidentes por mil carros.
    O média de veículos por cidade é de 548000.
    A média de acidentes total nas cidades com menos de 150 mil carros é de 900.0 acidentes.
"""


def calcular_estatisticas(*cidades):
    """Escreva aqui em baixo a sua solução"""
    total_veiculos = 0
    numero_cidades = 0
    acidentes_cidades_menores = 0
    numero_cidades_menores = 0

    for codigo_cidade, numero_veiculos, numero_acidentes in cidades:
        total_veiculos += numero_veiculos
        numero_cidades += 1
        indice_acidentes = numero_acidentes / numero_veiculos * 1000

        if 'maior_indice' not in vars() or indice_acidentes > maior_indice:
            maior_indice = indice_acidentes
            cidade_maior_indice = codigo_cidade

        if 'menor_indice' not in vars() or indice_acidentes < menor_indice:
            menor_indice = indice_acidentes
            cidade_menor_indice = codigo_cidade
        
        if numero_veiculos <= 150_000:
            numero_cidades_menores += 1
            acidentes_cidades_menores += numero_acidentes


    print(f'O maior índice de acidentes é de {cidade_maior_indice}, com {maior_indice:.1f} acidentes por mil carros.')
    print(f'O menor índice de acidentes é de {cidade_menor_indice}, com {menor_indice:.1f} acidentes por mil carros.')
    print(f'O média de veículos por cidade é de {total_veiculos / numero_cidades:.0f}.')
    if numero_cidades_menores > 0:
        print(f'A média de acidentes total nas cidades com menos de 150 mil carros é de {acidentes_cidades_menores / numero_cidades_menores:.1f} acidentes.')
