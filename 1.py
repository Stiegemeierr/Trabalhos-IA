from collections import deque

class Node:
    def __init__(self, state, parent=None, depth=0):
        self.state = state
        self.parent = parent
        self.depth = depth

def get_caminho(node):
    caminho = []
    atual = node
    while atual:
        caminho.append(atual.state)
        atual = atual.parent
    return caminho[::-1]

def print_resultados(resultado):
    print("\nResultados da Busca:")
    print(f"a) Ordem completa de expansão: {' -> '.join(resultado['ordem'])}")
    print(f"b) Conteúdo da fronteira: (Visto na tabela acima passo a passo)")
    print(f"c) Árvore parcial de busca: [{', '.join(resultado['arvore'])}]")
    print(f"d) Caminho solução encontrado: {' -> '.join(resultado['path'])}")
    print(f"e) Profundidade da solução: {resultado['depth']}")
    print(f"f) Custo da solução: {resultado['cost']}")
    print(f"g) Quantidade de nós gerados: {resultado['gerados']}")
    print(f"h) Quantidade de nós expandidos: {resultado['expandidos']}")

def bfs(grafo, inicio, objetivo):
    fronteira = deque([Node(inicio)])
    expandidos_count = 0
    gerados_count = 1
    passo = 1
    ordem_expansao = []
    arvore_parcial = []

    print(f"| {'Passo':^5} | {'Nó expandido':^12} | {'Conteúdo da fronteira':^30} |")
    print("-" * 57)

    while fronteira:
        no_atual = fronteira.popleft()
        ordem_expansao.append(no_atual.state)

        if no_atual.state == objetivo:
            str_fronteira = "[" + ", ".join([n.state for n in fronteira]) + "]"
            print(f"| {passo:^5} | {no_atual.state:^12} | {str_fronteira:<30} |")
            return {
                'path': get_caminho(no_atual),
                'depth': no_atual.depth,
                'cost': no_atual.depth,
                'gerados': gerados_count,
                'expandidos': expandidos_count,
                'ordem': ordem_expansao,
                'arvore': arvore_parcial
            }

        expandidos_count += 1
        sucessores = grafo.get(no_atual.state, [])
        for suc in sucessores:
            fronteira.append(Node(suc, no_atual, no_atual.depth + 1))
            gerados_count += 1
            arvore_parcial.append(f"{no_atual.state}->{suc}")

        str_fronteira = "[" + ", ".join([n.state for n in fronteira]) + "]"
        print(f"| {passo:^5} | {no_atual.state:^12} | {str_fronteira:<30} |")
        passo += 1
        
    return None

def dfs(grafo, inicio, objetivo):
    fronteira = [Node(inicio)]
    expandidos_count = 0
    gerados_count = 1
    passo = 1
    ordem_expansao = []
    arvore_parcial = []

    print(f"| {'Passo':^5} | {'Nó expandido':^12} | {'Conteúdo da fronteira':^30} |")
    print("-" * 57)

    while fronteira:
        no_atual = fronteira.pop()
        ordem_expansao.append(no_atual.state)

        # Na DFS, exibimos a fronteira do topo (fim da lista) para a base, para legibilidade
        if no_atual.state == objetivo:
            str_fronteira = "[" + ", ".join([n.state for n in reversed(fronteira)]) + "]"
            print(f"| {passo:^5} | {no_atual.state:^12} | {str_fronteira:<30} |")
            return {
                'path': get_caminho(no_atual),
                'depth': no_atual.depth,
                'cost': no_atual.depth,
                'gerados': gerados_count,
                'expandidos': expandidos_count,
                'ordem': ordem_expansao,
                'arvore': arvore_parcial
            }

        expandidos_count += 1
        sucessores = grafo.get(no_atual.state, [])
        
        # Adiciona na ordem inversa para que o primeiro vizinho fique no topo da pilha
        for suc in reversed(sucessores):
            fronteira.append(Node(suc, no_atual, no_atual.depth + 1))
            gerados_count += 1
            # Para registro da árvore manteremos a ordem real do grafo original
            # O insert(0) ajuda a manter a visualização a ordem que foi lida
            arvore_parcial.insert(0, f"{no_atual.state}->{suc}")

        str_fronteira = "[" + ", ".join([n.state for n in reversed(fronteira)]) + "]"
        print(f"| {passo:^5} | {no_atual.state:^12} | {str_fronteira:<30} |")
        passo += 1
        
    return None

def ids(grafo, inicio, objetivo):
    limite = 0
    total_gerados = 0
    total_expandidos = 0

    while True:
        print(f"\n--- Iteração com limite de profundidade: {limite} ---")
        print(f"| {'Passo':^5} | {'Nó expandido':^12} | {'Conteúdo da fronteira':^30} |")
        print("-" * 57)
        
        fronteira = [Node(inicio)]
        gerados_iteracao = 1
        expandidos_iteracao = 0
        passo = 1
        ordem_expansao = []
        arvore_parcial = []
        solucao = None

        while fronteira:
            no_atual = fronteira.pop()
            ordem_expansao.append(no_atual.state)

            if no_atual.state == objetivo:
                str_fronteira = "[" + ", ".join([n.state for n in reversed(fronteira)]) + "]"
                print(f"| {passo:^5} | {no_atual.state:^12} | {str_fronteira:<30} |")
                solucao = {
                    'path': get_caminho(no_atual),
                    'depth': no_atual.depth,
                    'cost': no_atual.depth,
                    'ordem': ordem_expansao,
                    'arvore': arvore_parcial
                }
                break

            if no_atual.depth < limite:
                expandidos_iteracao += 1
                sucessores = grafo.get(no_atual.state, [])
                for suc in reversed(sucessores):
                    fronteira.append(Node(suc, no_atual, no_atual.depth + 1))
                    gerados_iteracao += 1
                    arvore_parcial.insert(0, f"{no_atual.state}->{suc}")
                
                str_fronteira = "[" + ", ".join([n.state for n in reversed(fronteira)]) + "]"
                print(f"| {passo:^5} | {no_atual.state:^12} | {str_fronteira:<30} |")
            else:
                str_fronteira = "[" + ", ".join([n.state for n in reversed(fronteira)]) + "]"
                print(f"| {passo:^5} | {no_atual.state+' (lim)':^12} | {str_fronteira:<30} |")

            passo += 1

        total_gerados += gerados_iteracao
        total_expandidos += expandidos_iteracao

        if solucao:
            solucao['gerados'] = total_gerados
            solucao['expandidos'] = total_expandidos
            return solucao

        limite += 1

def run_all(grafo, nome_grafo):
    print("=" * 65)
    print(f"EXECUÇÃO: {nome_grafo}")
    print("=" * 65)

    print("\n" + "=" * 45)
    print("1. BUSCA EM AMPLITUDE/LARGURA (BFS)")
    print("=" * 45)
    res_bfs = bfs(grafo, 'A', 'S')
    if res_bfs: print_resultados(res_bfs)

    print("\n" + "=" * 45)
    print("2. BUSCA EM PROFUNDIDADE (DFS)")
    print("=" * 45)
    res_dfs = dfs(grafo, 'A', 'S')
    if res_dfs: print_resultados(res_dfs)

    print("\n" + "=" * 45)
    print("3. BUSCA ITERATIVA EM PROFUNDIDADE (IDS)")
    print("=" * 45)
    res_ids = ids(grafo, 'A', 'S')
    if res_ids: print_resultados(res_ids)
    print("\n")

# ==============================================================================
# DEFINIÇÃO DOS GRAFOS
# ==============================================================================

grafo_original = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I'],
    'E': ['J'],
    'F': ['K', 'L'],
    'G': ['M'],
    'H': ['N', 'O'],
    'I': ['P'],
    'J': [],
    'K': ['Q'],
    'L': [],
    'M': ['R'],
    'N': [],
    'O': ['S'],
    'P': [],
    'Q': [],
    'R': [],
    'S': []
}

grafo_modificado = {
    'A': ['D', 'C', 'B'], # ALTERAÇÃO 1: Ordem invertida
    'B': ['E', 'F'],
    'C': ['H', 'G'],      # ALTERAÇÃO 2: Ordem invertida
    'D': ['I'],
    'E': ['J'],
    'F': ['K', 'L'],
    'G': ['M'],
    'H': ['N', 'O'],
    'I': ['P'],
    'J': [],
    'K': ['Q'],
    'L': [],
    'M': ['R'],
    'N': [],
    'O': ['S'],
    'P': [],
    'Q': [],
    'R': [],
    'S': []
}

# ==============================================================================
# EXECUÇÕES
# ==============================================================================

if __name__ == "__main__":
    run_all(grafo_original, "GRAFO ORIGINAL")
    run_all(grafo_modificado, "GRAFO MODIFICADO")

"""
================================================================================
EXPLICAÇÃO DO EXPERIMENTO - NÓS MODIFICADOS:
================================================================================

No grafo_modificado, a ordem dos sucessores de exatos dois nós foi alterada para 
demonstrar impacto significativo na exploração dos algoritmos de busca:

1. Nó 'A' (Estado Inicial): 
   - Original: ['B', 'C', 'D']
   - Modificado: ['D', 'C', 'B']
   - Motivo/Impacto: Modificar a ordem de expansão da raiz altera diretamente qual 
     ramo completo a DFS (e a IDS) mergulhará primeiro. A DFS forçosamente irá 
     explorar o ramo improdutivo 'D' (e seu sucessor 'I', 'P') antes de chegar 
     ao ramo 'C' onde o objetivo reside.

2. Nó 'C' (Ancestral no caminho da solução):
   - Original: ['G', 'H']
   - Modificado: ['H', 'G']
   - Motivo/Impacto: Como o caminho solução passa por C -> H -> O -> S, colocar 
     'H' antes de 'G' garante que o algoritmo alcance o caminho correto mais 
     rapidamente. Isso reduzirá drasticamente os nós expandidos nos algoritmos 
     DFS e IDS, compensando a variação imposta pela primeira alteração.
"""