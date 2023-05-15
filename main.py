# Importando algoritmos
from src.bfs import bfs
from src.ids import ids
from src.ucs import ucs
from src.a_star import a_star
from src.gs import gs

import time

vetores = [
    [2,3,1,4],
    [3,1,4,5,2],
    [5,1,3,4,6,2],
    [1,2,5,4,7,3,6],
    [2,3,5,8,4,6,1,7],
    [4,3,6,1,5,9,8,7,2],
    [10,7,3,5,1,4,6,8,2],
    ]

for vetor in vetores:
    print("\nEstado Inicial: ", vetor)
    
    start = time.time()
    print("Busca em Largura")
    bfs(vetor, False)
    end = time.time()
    print("Tempo de Execução: ", round(end-start,2), " segundos")

    start = time.time()
    print("Busca em Aprofundamento iterativo")
    ids(vetor, False)
    end = time.time()
    print("Tempo de Execução: ", round(end-start,2), " segundos")

    start = time.time()
    print("Busca em Custo Uniforme")
    ucs(vetor, False)
    end = time.time()
    print("Tempo de Execução: ", round(end-start,2), " segundos")
    
    start = time.time()
    print("Busca A*")
    a_star(vetor, False)
    end = time.time()
    print("Tempo de Execução: ", round(end-start,2), " segundos")

    start = time.time()    
    print("Busca Gulosa")
    gs(vetor, False)
    end = time.time()
    print("Tempo de Execução: ", round(end-start,2), " segundos")