"""
Exercício 26 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

uma eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar
 e ao final mostrar o número de votos de cada candidato.

    >>> calcular_votos()
    Votantes: 0
    Votos no candidato corrupto: 0
    Votos no candidato mentiroso: 0
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto')
    Votantes: 1
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 0
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto', 'mentiroso')
    Votantes: 2
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 1
    Votos no candidato rouba, mas faz: 0
    >>> calcular_votos('corrupto', 'mentiroso', 'rouba, mas faz')
    Votantes: 3
    Votos no candidato corrupto: 1
    Votos no candidato mentiroso: 1
    Votos no candidato rouba, mas faz: 1
    >>> calcular_votos('corrupto', 'mentiroso', 'rouba, mas faz', 'corrupto', 'mentiroso', 'rouba, mas faz')
    Votantes: 6
    Votos no candidato corrupto: 2
    Votos no candidato mentiroso: 2
    Votos no candidato rouba, mas faz: 2

"""


def calcular_votos(*votos):
    """Escreva aqui em baixo a sua solução"""
 
    """ Esta é uma solução mais geral, mas não passa no doctext

    total_votantes = len(votos)
    lista_de_votos = list(votos)
    conjunto_candidatos = set(lista_de_votos)

    print(f'Votantes: {total_votantes}')
    for candidato in conjunto_candidatos:
        print(f'Votos no candidato {candidato}: {lista_de_votos.count(candidato)}')
    """
    total_votantes = len(votos)
    lista_de_votos = list(votos)
    tupla_de_candidatos = ('corrupto', 'mentiroso', 'rouba, mas faz')
  
    print(f'Votantes: {total_votantes}')
    for candidato in tupla_de_candidatos:
        print(f'Votos no candidato {candidato}: {lista_de_votos.count(candidato)}')
 

#calcular_votos('corrupto', 'mentiroso', 'rouba, mas faz', 'corrupto', 'mentiroso', 'rouba, mas faz')