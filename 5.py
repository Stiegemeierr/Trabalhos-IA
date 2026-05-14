# ==============================================================================
# DEFINIÇÃO DAS ÁRVORES DE JOGO
# ==============================================================================

tree_original = {
    'A': {'type': 'MAX', 'children': ['B', 'C', 'H']},
    'B': {'type': 'MIN', 'children': ['D', 'E']},
    'C': {'type': 'MIN', 'children': ['F', 'G']},
    'H': {'type': 'MIN', 'children': ['I', 'J']},
    'D': {'type': 'MAX', 'children': ['D1', 'D2']},
    'E': {'type': 'MAX', 'children': ['E1', 'E2']},
    'F': {'type': 'MAX', 'children': ['F1', 'F2']},
    'G': {'type': 'MAX', 'children': ['G1', 'G2']},
    'I': {'type': 'MAX', 'children': ['I1', 'I2']},
    'J': {'type': 'MAX', 'children': ['J1', 'J2']},
    'D1': {'value': 3}, 'D2': {'value': 5},
    'E1': {'value': 6}, 'E2': {'value': 9},
    'F1': {'value': 1}, 'F2': {'value': 2},
    'G1': {'value': 0}, 'G2': {'value': -1},
    'I1': {'value': 7}, 'I2': {'value': 4},
    'J1': {'value': 5}, 'J2': {'value': 6},
}

"""
EXPERIMENTO ADICIONAL: ÁRVORE MODIFICADA
Folhas alteradas para forçar A a mudar sua decisão de H (valor 6) para B (valor 8).
1. D2: de 5 para 8. (Fortalece o nó D para 8. Consequentemente, B melhora de 5 para 8).
2. I1: de 7 para 2. (Enfraquece o nó I de 7 para 4. Prejudica H).
3. J2: de 6 para 1. (Enfraquece o nó J de 6 para 5. H cai de 6 para 4).
Com isso, A escolherá B (valor 8) no lugar de H (valor 4).
"""
tree_modified = {
    'A': {'type': 'MAX', 'children': ['B', 'C', 'H']},
    'B': {'type': 'MIN', 'children': ['D', 'E']},
    'C': {'type': 'MIN', 'children': ['F', 'G']},
    'H': {'type': 'MIN', 'children': ['I', 'J']},
    'D': {'type': 'MAX', 'children': ['D1', 'D2']},
    'E': {'type': 'MAX', 'children': ['E1', 'E2']},
    'F': {'type': 'MAX', 'children': ['F1', 'F2']},
    'G': {'type': 'MAX', 'children': ['G1', 'G2']},
    'I': {'type': 'MAX', 'children': ['I1', 'I2']},
    'J': {'type': 'MAX', 'children': ['J1', 'J2']},
    'D1': {'value': 3}, 'D2': {'value': 8},  # ALTERADO
    'E1': {'value': 6}, 'E2': {'value': 9},
    'F1': {'value': 1}, 'F2': {'value': 2},
    'G1': {'value': 0}, 'G2': {'value': -1},
    'I1': {'value': 2}, 'I2': {'value': 4},  # ALTERADO
    'J1': {'value': 5}, 'J2': {'value': 1},  # ALTERADO
}

# ==============================================================================
# 1. MINIMAX COMPLETO
# ==============================================================================
def run_minimax(tree, root_node='A'):
    explored = []

    def _minimax(node):
        explored.append(node)
        
        # Caso base: nó folha
        if 'value' in tree[node]:
            return tree[node]['value'], [node]
            
        is_max = tree[node]['type'] == 'MAX'
        best_val = float('-inf') if is_max else float('inf')
        best_path = []
        
        # Propagação dos valores dos filhos para o pai
        for child in tree[node]['children']:
            val, path = _minimax(child)
            if is_max:
                if val > best_val:
                    best_val = val
                    best_path = path
            else:
                if val < best_val:
                    best_val = val
                    best_path = path
                    
        return best_val, [node] + best_path

    val, path = _minimax(root_node)
    return val, path, explored

# ==============================================================================
# 2. ALPHA-BETA
# ==============================================================================
def run_alphabeta(tree, root_node='A'):
    explored = []
    prunings = []

    def _alphabeta(node, alpha, beta):
        explored.append(node)
        
        # Caso base: nó folha
        if 'value' in tree[node]:
            return tree[node]['value'], [node]
            
        is_max = tree[node]['type'] == 'MAX'
        best_val = float('-inf') if is_max else float('inf')
        best_path = []
        
        for i, child in enumerate(tree[node]['children']):
            val, path = _alphabeta(child, alpha, beta)
            
            if is_max:
                if val > best_val:
                    best_val = val
                    best_path = path
                alpha = max(alpha, best_val)
                # Lógica de Poda para MAX: se o valor atualizado garantir algo >= ao limite 
                # tolerado pelo MIN acima (beta), o MIN jamais escolherá este caminho. Poda!
                if best_val >= beta:
                    remaining = tree[node]['children'][i+1:]
                    if remaining:
                        prunings.append(f"No nó {node}, filhos {remaining} podados (motivo: valor {best_val} >= beta {beta})")
                    break
            else:
                if val < best_val:
                    best_val = val
                    best_path = path
                beta = min(beta, best_val)
                # Lógica de Poda para MIN: se o valor garantido for <= ao piso 
                # tolerado pelo MAX acima (alpha), o MAX jamais virá para cá. Poda!
                if best_val <= alpha:
                    remaining = tree[node]['children'][i+1:]
                    if remaining:
                        prunings.append(f"No nó {node}, filhos {remaining} podados (motivo: valor {best_val} <= alpha {alpha})")
                    break
                    
        return best_val, [node] + best_path

    val, path = _alphabeta(root_node, float('-inf'), float('inf'))
    return val, path, explored, prunings

# ==============================================================================
# 3. MINIMAX COM PROFUNDIDADE LIMITADA
# ==============================================================================
def run_depth_limited(tree, root_node='A', limit=2):
    explored = []
    heuristics = {'D': 4, 'E': 7, 'F': 2, 'G': 5, 'I': 6, 'J': 1}

    def _depth_limited(node, depth):
        explored.append(node)
        
        # Interrompe a busca na profundidade limite e retorna a estimativa estática (heurística)
        if depth == limit:
            return heuristics[node], [node]
            
        is_max = tree[node]['type'] == 'MAX'
        best_val = float('-inf') if is_max else float('inf')
        best_path = []
        
        for child in tree[node]['children']:
            val, path = _depth_limited(child, depth + 1)
            if is_max:
                if val > best_val:
                    best_val = val
                    best_path = path
            else:
                if val < best_val:
                    best_val = val
                    best_path = path
                    
        return best_val, [node] + best_path

    val, path = _depth_limited(root_node, 0)
    return val, path, explored

# ==============================================================================
# FUNÇÃO DE EXECUÇÃO E FORMATAÇÃO DE SAÍDA
# ==============================================================================
def execute_and_print():
    configs = [
        ("ÁRVORE ORIGINAL", tree_original),
        ("ÁRVORE MODIFICADA", tree_modified)
    ]
    
    comparative_table = []

    for tree_name, tree in configs:
        print("="*60)
        print(f"=== 1. MINIMAX COMPLETO === {tree_name} ===")
        val, path, expl = run_minimax(tree)
        decisao_A = path[1] if len(path) > 1 else 'N/A'
        print(f"Valor na raiz: {val}")
        print(f"Caminho ótimo: {' -> '.join(path)}")
        print(f"Nós explorados: {len(expl)}")
        print(f"Decisão de A: filho {decisao_A}")
        comparative_table.append(('Minimax Comp.', tree_name, val, len(expl), '-', decisao_A))

        print("="*60)
        print(f"=== 2. ALPHA-BETA === {tree_name} ===")
        val, path, expl, prunings = run_alphabeta(tree)
        decisao_A = path[1] if len(path) > 1 else 'N/A'
        print(f"Valor na raiz: {val}")
        print(f"Caminho ótimo: {' -> '.join(path)}")
        print(f"Nós explorados: {len(expl)}")
        print(f"Podas: {len(prunings)}")
        for p in prunings:
            print(f"  - {p}")
        print(f"Decisão de A: filho {decisao_A}")
        comparative_table.append(('Alpha-Beta', tree_name, val, len(expl), len(prunings), decisao_A))

        print("="*60)
        print(f"=== 3. MINIMAX DEPTH-LIMITED (L=2) === {tree_name} ===")
        val, path, expl = run_depth_limited(tree)
        decisao_A = path[1] if len(path) > 1 else 'N/A'
        print(f"Valor na raiz: {val}")
        print(f"Caminho ótimo: {' -> '.join(path)}")
        print(f"Nós explorados: {len(expl)}")
        print(f"Decisão de A: filho {decisao_A}")
        comparative_table.append(('Depth-Lim(2)', tree_name, val, len(expl), '-', decisao_A))

    print("="*60)
    print("\n| Algoritmo            | Árvore            | Valor raiz | Nós explorados | Podas | Decisão A |")
    print("|----------------------|-------------------|------------|----------------|-------|-----------|")
    for row in comparative_table:
        print(f"| {row[0]:<20} | {row[1]:<17} | {row[2]:<10} | {row[3]:<14} | {row[4]:<5} | {row[5]:<9} |")

if __name__ == "__main__":
    execute_and_print()