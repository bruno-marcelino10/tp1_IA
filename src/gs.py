def acao_gs(node):
    '''
    Entrada: representação de um nó -> [estado, pai, ação, heuristica, custo, profundidade]
    Saída: lista de nodes (que são as expansões deste)
    '''
    expansoes = []
    profundidade = node[5] + 1
    
    # Gera os nós filhos caso a condição de troca seja válida
    for i in range(len(node[0])):
        for j in range(len(node[0])):
            if node[0][i] > node[0][j]:
                
                # Cria novo estado
                estado = node[0].copy()
                tmp = estado[i]
                estado[i] = estado[j]
                estado[j] = tmp

                # Calcula custo total
                if j-i == 1:
                    custo = 2
                else:
                    custo = 4

                # Calcula h(node) -> quantidade de numeros fora do lugar
                h_n = 0
                for pos_atual in range(len(estado)):          
                    best_pos = estado[pos_atual]-1
                    if best_pos != pos_atual:
                        h_n += 1

                # Cria o node
                expansoes.append([
                    estado, 
                    node[0], 
                    [estado[i], estado[j]], 
                    h_n, 
                    node[4] + custo, 
                    profundidade])

    return expansoes

def menor_h_n(fronteira: list):
    # node = [estado, pai, ação, heuristica, custo, profundidade]
    heuristicas = [node[3] for node in fronteira]
    for i in range(len(heuristicas)):
        if heuristicas[i] == min(heuristicas):
            node_escolhido = fronteira[i]
            break
    
    return node_escolhido

def gs(init_node: list, printar=True):
    '''
    Entrada: lista contendo um estado do vetor
    Saída: None
    '''    
    
    init_node = [init_node, None, None, 0, 0, 0] # formato desejado -> [estado, pai, ação, heuristica, custo, profundidade]
    fronteira = None # Inicializa a fronteira
    explored = [] # Lista de nós explorados
    explored_states = [] # Lista de estados explorados
    solution = init_node[0].copy() 
    solution.sort() # Representação da solução
    
    continuar = True
    while continuar:

        # Primeiro caso
        if fronteira == None:
            fronteira = acao_gs(init_node) # Cria a primeira fronteira
            explored = [init_node] # adiciona o nó inicial dentre os casos já explorados
        else:
            # Caso onde não há solução
            if fronteira == []:
                # Finaliza o programa
                continuar = False
                print("Sem Solução")
            
            # Caso onde há solução
            else:

                # Seleciona um elemento
                explored_node = menor_h_n(fronteira)

                # Teste da solução
                if explored_node[0] == solution:

                    # mostra custo total e quantidade de expansões
                    print(explored_node[4], len(explored))

                    if printar:
                        # mostra estados intermediários até a solução no formato desejado
                        explored.append(explored_node)
                        pai = explored_node[1]
                        estados = [explored_node[0]]
                        while pai != None:                            
                            for node in explored:
                                if node[0] == pai:
                                    estados.append(node[0])
                                    pai = node[1]

                        for node in estados[::-1]:
                            str_node = ""
                            for elem in node:
                                str_node += str(elem) + " "
                            print(str_node[:-1])

                    # Finaliza o programa
                    continuar = False
                
                # Caso onde o estado já foi explorado
                if explored_node[0] in explored_states:
                    fronteira.remove(explored_node)

                # Caso onde nó ainda não foi explorado
                else:
                    fronteira += acao_gs(explored_node)
                    explored.append(explored_node)
                    explored_states.append(explored_node[0])
                    fronteira.remove(explored_node)