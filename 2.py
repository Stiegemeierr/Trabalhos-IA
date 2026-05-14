import heapq

# ==============================================================================
# DEFINIÇÃO DOS DADOS DO PROBLEMA
# ==============================================================================

# Grafo representado como dicionário de dicionários. 
# A partir do Python 3.7, dicionários preservam a ordem de inserção,
# garantindo que a "ordem obrigatória" da tabela seja respeitada nativamente.
grafo = {
    'A': {'B': 2, 'C': 4, 'D': 3},
    'B': {'E': 3, 'F': 5},
    'C': {'G': 4, 'H': 6},
    'D': {'I': 2},
    'E': {'J': 4},
    'F': {'K': 3, 'L': 5},
    'G': {'M': 6},
    'H': {'N': 3, 'O': 4},
    'I': {'P': 5},
    'J': {'Q': 4},
    'K': {'R': 3},
    'L': {},
    'M': {'S': 2},
    'N': {},
    'O': {'T': 5},
    'P': {},
    'Q': {},
    'R': {'T': 4},
    'S': {'T': 3},
    'T': {}
}

# Heurística original (admissível)
h_original = {
    'A': 10, 'B': 8, 'C': 7, 'D': 9, 'E': 6,
    'F': 5, 'G': 6, 'H': 4, 'I': 7, 'J': 5,
    'K': 3, 'L': 6, 'M': 3, 'N': 4, 'O': 1,
    'P': 8, 'Q': 4, 'R': 2, 'S': 1, 'T': 0
}

# Heurística modificada (inadmissível para testar quebra de otimalidade do A*)
h_modificada = h_original.copy()
h_modificada['B'] = 20  # Original: 8. Modificado para tornar a heurística inadmissível (h > custo real)
h_modificada['C'] = 2   # Original: 7. Modificado para atrair a busca Gulosa
h_modificada['H'] = 15  # Original: 4. Modificado para repelir caminhos por H

# ==============================================================================
# FUNÇÕES AUXILIARES
# ==============================================================================

def format_frontier_greedy(pq):
    """Formata a fila de prioridade do Greedy para exibição clara."""
    sorted_pq = sorted(pq, key=lambda x: (x[0], x[1]))
    return "[" + ", ".join([f"{item[2]}({item[0]})" for item in sorted_pq]) + "]"

def format_frontier_astar(pq):
    """Formata a fila de prioridade do A* para exibição clara."""
    sorted_pq = sorted(pq, key=lambda x: (x[0], x[1]))
    return "[" + ", ".join([f"{item[2]}({item[0]})" for item in sorted_pq]) + "]"

# ==============================================================================
# ALGORITMOS DE BUSCA
# ==============================================================================

def greedy_best_first_search(graph, h, start, goal):
    """
    Busca Gulosa (Greedy Best-First Search).
    Fronteira ordenada apenas pela heurística: h(n).
    """
    pq = []
    insert_order = 0
    # Tupla: (prioridade, ordem_insercao, no_atual, caminho_ate_aqui, custo_acumulado_g)
    heapq.heappush(pq, (h[start], insert_order, start, [start], 0))
    visited = set()
    
    passos_log = []
    gerados = 1
    expandidos = 0
    ordem_expansao = []
    
    while pq:
        current_h, _, current_node, path, current_g = heapq.heappop(pq)
        
        # Uso de lista fechada para evitar revisitar nós
        if current_node in visited:
            continue
            
        visited.add(current_node)
        expandidos += 1
        ordem_expansao.append(current_node)
        
        # Teste de objetivo
        if current_node == goal:
            passos_log.append({
                'passo': expandidos, 'no': current_node, 'h': current_h, 'fronteira': format_frontier_greedy(pq)
            })
            return path, current_g, gerados, expandidos, passos_log, ordem_expansao
            
        # Expansão dos sucessores
        for neighbor, edge_cost in graph.get(current_node, {}).items():
            if neighbor not in visited:
                insert_order += 1
                gerados += 1
                heapq.heappush(pq, (h[neighbor], insert_order, neighbor, path + [neighbor], current_g + edge_cost))
        
        # Registro do log do passo
        passos_log.append({
            'passo': expandidos, 'no': current_node, 'h': current_h, 'fronteira': format_frontier_greedy(pq)
        })
        
    return [], 0, gerados, expandidos, passos_log, ordem_expansao

def astar_search(graph, h, start, goal):
    """
    Busca A* (A-Star).
    Fronteira ordenada por f(n) = g(n) + h(n).
    """
    pq = []
    insert_order = 0
    # Tupla: (f_n, ordem_insercao, no_atual, caminho_ate_aqui, g_n)
    heapq.heappush(pq, (0 + h[start], insert_order, start, [start], 0))
    visited = set()
    
    passos_log = []
    gerados = 1
    expandidos = 0
    ordem_expansao = []
    
    while pq:
        current_f, _, current_node, path, current_g = heapq.heappop(pq)
        
        if current_node in visited:
            continue
            
        visited.add(current_node)
        expandidos += 1
        ordem_expansao.append(current_node)
        
        if current_node == goal:
            passos_log.append({
                'passo': expandidos, 'no': current_node, 'g': current_g, 'h': h[current_node], 
                'f': current_f, 'fronteira': format_frontier_astar(pq)
            })
            return path, current_g, gerados, expandidos, passos_log, ordem_expansao
            
        for neighbor, edge_cost in graph.get(current_node, {}).items():
            if neighbor not in visited:
                insert_order += 1
                gerados += 1
                g_new = current_g + edge_cost
                f_new = g_new + h[neighbor]
                heapq.heappush(pq, (f_new, insert_order, neighbor, path + [neighbor], g_new))
        
        passos_log.append({
            'passo': expandidos, 'no': current_node, 'g': current_g, 'h': h[current_node], 
            'f': current_f, 'fronteira': format_frontier_astar(pq)
        })
        
    return [], 0, gerados, expandidos, passos_log, ordem_expansao

# ==============================================================================
# FUNÇÃO DE EXECUÇÃO E IMPRESSÃO
# ==============================================================================

def run_all(graph, h, nome_config):
    print("\n" + "="*80)
    print(f"EXECUÇÃO: {nome_config}")
    print("="*80 + "\n")
    
    # --- GREEDY ---
    print("-" * 80)
    print("1. GREEDY BEST-FIRST SEARCH")
    print("-" * 80)
    path, cost, gerados, exp, log, ordem = greedy_best_first_search(graph, h, 'A', 'T')
    
    print(f"| {'Passo':^5} | {'Nó expandido':^12} | {'h(n)':^4} | {'Fronteira'}")
    print("|" + "-"*7 + "|" + "-"*14 + "|" + "-"*6 + "|:---")
    for row in log:
        print(f"| {row['passo']:^5} | {row['no']:^12} | {row['h']:^4} | {row['fronteira']}")
        
    print(f"\n[+] Ordem de expansão: {' -> '.join(ordem)}")
    print(f"[+] Caminho solução: {' -> '.join(path)}")
    print(f"[+] Custo da solução: {cost}")
    print(f"[+] Nós gerados: {gerados} | Nós expandidos: {exp}\n")

    # --- A* ---
    print("-" * 80)
    print("2. A* SEARCH")
    print("-" * 80)
    path_a, cost_a, ger_a, exp_a, log_a, ordem_a = astar_search(graph, h, 'A', 'T')
    
    print(f"| {'Passo':^5} | {'Nó':^4} | {'g(n)':^4} | {'h(n)':^4} | {'f(n)':^4} | {'Fronteira'}")
    print("|" + "-"*7 + "|" + "-"*6 + "|" + "-"*6 + "|" + "-"*6 + "|" + "-"*6 + "|:---")
    for row in log_a:
        print(f"| {row['passo']:^5} | {row['no']:^4} | {row['g']:^4} | {row['h']:^4} | {row['f']:^4} | {row['fronteira']}")
        
    print(f"\n[+] Ordem de expansão: {' -> '.join(ordem_a)}")
    print(f"[+] Caminho solução: {' -> '.join(path_a)}")
    print(f"[+] Custo da solução: {cost_a}")
    print(f"[+] Nós gerados: {ger_a} | Nós expandidos: {exp_a}\n")

# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == "__main__":
    run_all(grafo, h_original, "HEURÍSTICA ORIGINAL (Admissível)")
    run_all(grafo, h_modificada, "HEURÍSTICA MODIFICADA (Inadmissível)")

"""
================================================================================
EXPLICAÇÃO DO EXPERIMENTO - HEURÍSTICA MODIFICADA
================================================================================

Foram alterados os valores de h(n) de 3 nós específicos para demonstrar como o 
comportamento dos algoritmos é influenciado:

1. Nó 'C': 
   - Antigo: h(C) = 7
   - Novo: h(C) = 2
   - Motivo: Fazer o ramo 'C' parecer extremamente promissor de imediato, atraindo 
     o Greedy Search instantaneamente para ele logo no início.

2. Nó 'H':
   - Antigo: h(H) = 4
   - Novo: h(H) = 15
   - Motivo: Como forçamos o algoritmo a entrar no ramo 'C', 'H' é o sucessor natural 
     para a solução. Aumentando drasticamente o custo estimado de 'H', repelimos os 
     algoritmos para o ramo de 'G', forçando a expansão por caminhos menos usuais.

3. Nó 'B' (A MODIFICAÇÃO INADMISSÍVEL):
   - Antigo: h(B) = 8
   - Novo: h(B) = 20
   - Motivo / Inadmissibilidade: O custo real ótimo para ir de 'B' até 'T' é 15 
     (caminho B -> F -> K -> R -> T com custos 5+3+3+4 = 15). 
     Como configuramos h(B) = 20, temos h(n) > custo real até o objetivo. 
     Isso torna a heurística INADMISSÍVEL.
   - Impacto no A*: Com h(B) = 20, o f(B) passa a ser 22 logo no primeiro passo. O 
     A* abandonará temporariamente o caminho ótimo (que passa por B) achando que ele 
     é muito caro, forçando-o a buscar e entregar um caminho subótimo (como o 
     caminho A -> C -> G -> M -> S -> T, cujo custo real é 19). Isso comprova a 
     teoria de que o A* só garante o caminho ótimo se a heurística for admissível.
================================================================================
"""