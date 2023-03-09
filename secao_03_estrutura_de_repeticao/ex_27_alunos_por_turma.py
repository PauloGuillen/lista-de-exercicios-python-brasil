"""
Exercício 27 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade
de alunos para cada turma. As turmas não podem ter mais de 40 alunos e devem ter ao menos um aluno.
Arredonde o valor da média para baixo.

    >>> from secao_03_estrutura_de_repeticao import ex_27_alunos_por_turma
    >>> entradas = ['1', '1']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 1
    Média de alunos por turma: 1
    >>> entradas = ['10', '20', '30', '40', '-1', '5']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 5
    Uma turma deve ter de 1 a 40 alunos, não é possível ter -1 alunos
    Média de alunos por turma: 25
    >>> entradas = ['40', '40', '2']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 2
    Média de alunos por turma: 40
    >>> entradas = ['10', '20', '30', '0', '41', '5']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 5
    Uma turma deve ter de 1 a 40 alunos, não é possível ter 41 alunos
    Uma turma deve ter de 1 a 40 alunos, não é possível ter 0 alunos
    Média de alunos por turma: 20

"""
from math import floor

def calcular_media_de_alunos_por_turma():
    """Escreva aqui em baixo a sua solução"""

    alunos_por_turma = []
    numero_de_turmas = int(input('Informe o número de turmas: '))
    for i in range(numero_de_turmas):
        alunos_por_turma.append(int(input(f'Informe o número de alunos da {i+1}° turma: ')))

    print(f'Número de turmas: {numero_de_turmas}')
    turmas_validas = 0
    total_alunos = 0
    for numero_alunos in alunos_por_turma:
        if numero_alunos < 1 or numero_alunos > 40:
            print(f'Uma turma deve ter de 1 a 40 alunos, não é possível ter {numero_alunos} alunos')
        else:
            turmas_validas += 1
            total_alunos += numero_alunos

        
    media = floor(total_alunos / turmas_validas)
    print(f'Média de alunos por turma: {media}')  
    

#calcular_media_de_alunos_por_turma()