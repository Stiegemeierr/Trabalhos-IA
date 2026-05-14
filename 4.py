import time

# ==============================================================================
# CONFIGURAÇÕES GERAIS DO PROBLEMA
# ==============================================================================
VARIABLES = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6']
VALUES = ['A', 'B', 'C', 'D']

def check_value(assignment, var, val):
    """
    Simula a atribuição de 'val' a 'var' e verifica todas as restrições (R1 a R5).
    Retorna uma tupla (is_valid, conflicts), onde 'conflicts' é um set com as 
    variáveis já atribuídas que causaram o conflito (necessário para o Backjumping).
    """
    assignment[var] = val
    conflicts = set()
    valid = True
    
    idx = int(var[1]) - 1
    
    # R1: Não pode haver médicos iguais em turnos consecutivos
    if idx > 0:
        prev_var = f'T{idx}'
        if prev_var in assignment and assignment[prev_var] == val:
            conflicts.add(prev_var)
            valid = False
    if idx < 5:
        next_var = f'T{idx+2}'
        if next_var in assignment and assignment[next_var] == val:
            conflicts.add(next_var)
            valid = False
            
    # R2: T3 não pode ser 'A'
    if var == 'T3' and val == 'A':
        valid = False # Restrição unária, não depende de variáveis anteriores
        
    # R3: Pelo menos um entre T1 e T2 deve ser 'B'
    if 'T1' in assignment and 'T2' in assignment:
        if assignment['T1'] != 'B' and assignment['T2'] != 'B':
            conflicts.add('T1' if var == 'T2' else 'T2')
            valid = False
            
    # R4: T2 e T3 não podem ser ambos 'C'
    if 'T2' in assignment and 'T3' in assignment:
        if assignment['T2'] == 'C' and assignment['T3'] == 'C':
            conflicts.add('T2' if var == 'T3' else 'T3')
            valid = False
            
    # R5: Médico 'D' no máximo 2 vezes
    count_D = sum(1 for v in assignment.values() if v == 'D')
    if count_D > 2:
        # Se estourou o limite, TODAS as variáveis anteriores que são 'D' causaram conflito
        for k, v in assignment.items():
            if k != var and v == 'D':
                conflicts.add(k)
        valid = False
        
    # Desfaz a simulação
    del assignment[var]
    return valid, conflicts


# ==============================================================================
# 1. BACKTRACKING SIMPLES
# ==============================================================================
def bt_simple():
    """
    Backtracking Clássico. Utiliza ordem fixa de variáveis (T1 a T6) e de valores.
    Verifica restrições apenas quando uma nova atribuição é tentada.
    """
    metrics = {'explored': 0, 'backtracks': 0}
    
    def solve(assignment):
        if len(assignment) == 6:
            return dict(assignment)
        
        # Pega a próxima variável na ordem fixa
        var = VARIABLES[len(assignment)]
        
        for val in VALUES:
            metrics['explored'] += 1
            valid, _ = check_value(assignment, var, val)
            
            if valid:
                assignment[var] = val
                res = solve(assignment)
                if res: return res
                
                # Falha, realiza o retrocesso (backtrack)
                del assignment[var]
                metrics['backtracks'] += 1
                
        return None

    start = time.time()
    sol = solve({})
    return "1. BACKTRACKING SIMPLES", sol, metrics, (time.time() - start) * 1000


# ==============================================================================
# 2. BACKTRACKING + MRV
# ==============================================================================
def get_mrv_var(assignment):
    """
    Encontra a variável com o menor domínio restante (Minimum Remaining Values).
    Como exigido, filtra dinamicamente avaliando as restrições R1 e R2 para os cálculos.
    Em caso de empate, a ordem sequencial natural da iteração (T1 a T6) servirá 
    como tie-breaker automático (menor índice).
    """
    best_var = None
    min_domain = 999
    
    for var in VARIABLES:
        if var not in assignment:
            valid_count = 0
            for val in VALUES:
                # Simula R1 e R2
                is_valid = True
                idx = int(var[1]) - 1
                if idx > 0 and f'T{idx}' in assignment and assignment[f'T{idx}'] == val: is_valid = False
                if idx < 5 and f'T{idx+2}' in assignment and assignment[f'T{idx+2}'] == val: is_valid = False
                if var == 'T3' and val == 'A': is_valid = False
                
                if is_valid: valid_count += 1
                    
            if valid_count < min_domain:
                min_domain = valid_count
                best_var = var
                
    return best_var

def bt_mrv():
    """
    Backtracking utilizando a heurística MRV para ordenação dinâmica das variáveis.
    """
    metrics = {'explored': 0, 'backtracks': 0}
    
    def solve(assignment):
        if len(assignment) == 6:
            return dict(assignment)
        
        var = get_mrv_var(assignment)
        
        for val in VALUES:
            metrics['explored'] += 1
            valid, _ = check_value(assignment, var, val)
            
            if valid:
                assignment[var] = val
                res = solve(assignment)
                if res: return res
                
                del assignment[var]
                metrics['backtracks'] += 1
                
        return None

    start = time.time()
    sol = solve({})
    return "2. BACKTRACKING + MRV", sol, metrics, (time.time() - start) * 1000


# ==============================================================================
# 3. BACKTRACKING + DEGREE HEURISTIC
# ==============================================================================
def get_degree_var(assignment):
    """
    Encontra a variável com o maior número de restrições envolvendo outras 
    variáveis NÃO atribuídas. 
    A topologia baseia-se em R1, R3 e R4.
    """
    best_var = None
    max_degree = -1
    
    # Mapeamento estático dos vizinhos envolvidos em restrições (excluindo globais não topológicas)
    neighbors = {
        'T1': ['T2'],
        'T2': ['T1', 'T3'],
        'T3': ['T2', 'T4'],
        'T4': ['T3', 'T5'],
        'T5': ['T4', 'T6'],
        'T6': ['T5']
    }
    
    for var in VARIABLES:
        if var not in assignment:
            # Grau = quantidade de vizinhos que ainda NÃO foram atribuídos
            degree = sum(1 for n in neighbors[var] if n not in assignment)
            if degree > max_degree:
                max_degree = degree
                best_var = var
                
    return best_var

def bt_degree():
    """
    Backtracking utilizando Degree Heuristic para escolha de variável.
    """
    metrics = {'explored': 0, 'backtracks': 0}
    
    def solve(assignment):
        if len(assignment) == 6:
            return dict(assignment)
        
        var = get_degree_var(assignment)
        
        for val in VALUES:
            metrics['explored'] += 1
            valid, _ = check_value(assignment, var, val)
            
            if valid:
                assignment[var] = val
                res = solve(assignment)
                if res: return res
                
                del assignment[var]
                metrics['backtracks'] += 1
                
        return None

    start = time.time()
    sol = solve({})
    return "3. BACKTRACKING + DEGREE", sol, metrics, (time.time() - start) * 1000


# ==============================================================================
# 4. FORWARD CHECKING
# ==============================================================================
def bt_forward_checking():
    """
    Backtracking com Forward Checking. A cada atribuição, antecipa restrições locais (R1 e R2)
    e remove os valores inconsistentes dos domínios das variáveis vizinhas futuras.
    """
    metrics = {'explored': 0, 'backtracks': 0}
    
    def solve(assignment, domains):
        if len(assignment) == 6:
            return dict(assignment)
            
        var = VARIABLES[len(assignment)]
        
        for val in domains[var]:
            metrics['explored'] += 1
            # Continua verificando as globais e demais que não foram ativamente propagadas (R3, R4, R5)
            valid, _ = check_value(assignment, var, val) 
            
            if valid:
                assignment[var] = val
                
                # Cópia profunda dos domínios atuais para não poluir em caso de falha futura
                new_domains = {k: list(v) for k, v in domains.items()}
                fc_valid = True
                
                # Propagação ativa da R1 para os vizinhos
                idx = int(var[1]) - 1
                neighbors = []
                if idx > 0: neighbors.append(f'T{idx}')
                if idx < 5: neighbors.append(f'T{idx+2}')
                
                for n in neighbors:
                    if n not in assignment:
                        if val in new_domains[n]:
                            new_domains[n].remove(val) # Remove valor inconsistente
                        # Poda imediata se esgotar as possibilidades
                        if not new_domains[n]:
                            fc_valid = False
                            break
                            
                # Avança somente se o Forward Checking não detectou domínio vazio
                if fc_valid:
                    res = solve(assignment, new_domains)
                    if res: return res
                    
                # Falhou ou o FC detectou domínio vazio precocemente (backtrack!)
                del assignment[var]
                metrics['backtracks'] += 1
                
        return None

    # Domínios iniciais e propagação instantânea da R2
    initial_domains = {v: list(VALUES) for v in VARIABLES}
    initial_domains['T3'].remove('A') 
    
    start = time.time()
    sol = solve({}, initial_domains)
    return "4. FORWARD CHECKING", sol, metrics, (time.time() - start) * 1000


# ==============================================================================
# 5. BACKJUMPING (Conflict-Directed)
# ==============================================================================
def bt_backjumping():
    """
    Conflict-Directed Backjumping (CBJ). Ao invés de voltar apenas uma variável no tempo,
    ele pula direto para a raiz do problema causador da falha consultando os Conflict Sets.
    """
    metrics = {'explored': 0, 'backtracks': 0}
    assignment = {}
    conflict_sets = {v: set() for v in VARIABLES}
    
    def solve(var_idx):
        if var_idx == 6:
            return dict(assignment), -1 # -1 indica solução encontrada
        
        var = VARIABLES[var_idx]
        conflict_sets[var] = set() # Reinicia o set da variável atual nesta ramificação
        
        for val in VALUES:
            metrics['explored'] += 1
            valid, conflicts = check_value(assignment, var, val)
            
            if valid:
                assignment[var] = val
                res, jump_idx = solve(var_idx + 1)
                
                if res is not None:
                    return res, -1
                
                # Um retrocesso ocorreu a partir do futuro
                del assignment[var]
                metrics['backtracks'] += 1
                
                # Se fomos instruídos a saltar para antes de mim, ignoro o restante e propago
                if jump_idx < var_idx:
                    return None, jump_idx
            else:
                # O valor falhou, armazeno quem foi o culpado no meu Conflict Set
                conflict_sets[var].update(conflicts)
                
        # Esgotou as opções para esta variável. Precisa executar o Backjump.
        if not conflict_sets[var]:
            # Casos de domínio vazio estrutural (ex: restrição unária). Volta 1 passo.
            jump_idx = var_idx - 1 
        else:
            # Encontra a variável culposa mais recente (maior índice)
            jump_idx = max(VARIABLES.index(c) for c in conflict_sets[var])
            
        if jump_idx >= 0 and jump_idx < var_idx:
            # Funde o Conflict Set para que a variável culposa continue o salto se necessário
            jump_var = VARIABLES[jump_idx]
            conflict_sets[jump_var].update(conflict_sets[var])
            conflict_sets[jump_var].discard(jump_var)
            
        return None, jump_idx

    start = time.time()
    sol, _ = solve(0)
    return "5. BACKJUMPING", sol, metrics, (time.time() - start) * 1000


# ==============================================================================
# EXECUÇÃO E IMPRESSÃO
# ==============================================================================
if __name__ == "__main__":
    algorithms = [bt_simple, bt_mrv, bt_degree, bt_forward_checking, bt_backjumping]
    results = []

    for algo in algorithms:
        name, sol, metrics, duration = algo()
        results.append((name, sol, metrics, duration))
        
        print(f"=== {name} ===")
        print(f"Solução: {sol}")
        print(f"Estados explorados: {metrics['explored']}")
        print(f"Retrocessos: {metrics['backtracks']}")
        print(f"Tempo: {duration:.4f} ms\n")

    # Tabela comparativa final
    print("-" * 85)
    print(f"| {'Algoritmo':<27} | {'Estados explorados':<18} | {'Retrocessos':<11} | {'Tempo (ms)':<10} |")
    print("-" * 85)
    for name, sol, metrics, duration in results:
        print(f"| {name:<27} | {metrics['explored']:<18} | {metrics['backtracks']:<11} | {duration:<10.4f} |")
    print("-" * 85)