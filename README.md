Trabalho Prático 1 - Introdução à Inteligência Artificial
Aluno: Bruno Marcelino
Matrícula: 2019013155
Data: 14/05
Profº: Luiz Chaimowicz 

Este documento tem por finalidade demonstrar como funciona o projeto.

# Estrutura de Pastas

### Arquivo `TP1.py`

Realiza a execução do projeto, que foi construido inteiramente na linguagem Python. Para rodar, deve-se inserir os parâmetros desejados na linha de comando utilizando a sintaxe:

`python TP1.py sigla_do_algoritmo tamanho_do_vetor valor_1 valor_2 (...) PRINT`

**Obs.:** O argumento

Exemplo: `python TP1.py A 4 2 3 1 4`
* Algoritmo: A* (vide enunciado do trabalho)
* Tamanho do Input: 4 elementos
* Input: `[2, 3, 1, 4]`
* Printar estados intermediários: não

A saída sempre deve conter dois números: O custo total até a solução encontrada, e o número de estados expandidos. Caso o argumento PRINT seja inserido, a saída retornará listas contendo os estados intermediários até a solução

### Arquivo Documentação.pdf

Contém a parte escrita descrita no enunciado do trabalho.

### Pasta `docs`:

Contém Jupyter Notebooks utilizados para auxiliar na criação dos algoritmos, e na criação da documentação final do projeto. 

### Pasta `src`: 

Contém os códigos-fonte dos algoritmos a serem testados. São eles: 

* Breadth-first search (B)
* Iterative deepening search (I)
* Uniform-cost search (U)
* A* search (A)
* Greedy best-first search (G)