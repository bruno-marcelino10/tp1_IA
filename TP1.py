# Importando algoritmos
from src.bfs import bfs
from src.ids import ids
from src.ucs import ucs
from src.a_star import a_star
from src.gs import gs

# Tratamento de Entrada (não faz nada com o tamanho do vetor)
from src.inputs import Entrada
inputs = Entrada()

# Realiza operações
    
if inputs.nome_algoritmo == "B" and inputs.printar == False:
    bfs(inputs.values, False)
elif inputs.nome_algoritmo == "B" and inputs.printar == True:
    bfs(inputs.values)
if inputs.nome_algoritmo == "I" and inputs.printar == False:
    ids(inputs.values, False)
elif inputs.nome_algoritmo == "I" and inputs.printar == True:
    ids(inputs.values)
if inputs.nome_algoritmo == "U" and inputs.printar == False:
    ucs(inputs.values, False)
elif inputs.nome_algoritmo == "U" and inputs.printar == True:
    ucs(inputs.values)
if inputs.nome_algoritmo == "A" and inputs.printar == False:
    a_star(inputs.values, False)
elif inputs.nome_algoritmo == "A" and inputs.printar == True:
    a_star(inputs.values)
if inputs.nome_algoritmo == "G" and inputs.printar == False:
    gs(inputs.values, False)
elif inputs.nome_algoritmo == "G" and inputs.printar == True:
    gs(inputs.values)
