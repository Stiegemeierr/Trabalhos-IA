import random
import math
import time

# ==============================================================================
# LÓGICA DO JOGO CONNECT-4 (4x4)
# ==============================================================================

def get_valid_moves(board):
    """Retorna as colunas que ainda possuem espaço vazio na linha mais alta (topo)."""
    valid_moves = []
    for c in range(4):
        if board[3][c] == '.':
            valid_moves.append(c)
    return valid_moves

def make_move(board, col, player):
    """Gera um novo estado do tabuleiro com a peça do jogador inserida na coluna."""
    new_board = [row[:] for row in board]
    for r in range(4):
        if new_board[r][col] == '.':
            new_board[r][col] = player
            break
    return new_board

def check_winner(board):
    """Verifica se há um vencedor (V ou A), se houve empate ou se o jogo continua."""
    for p in ['V', 'A']:
        # Linhas
        for r in range(4):
            if all(board[r][c] == p for c in range(4)): return p
        # Colunas
        for c in range(4):
            if all(board[r][c] == p for r in range(4)): return p
        # Diagonais
        if all(board[i][i] == p for i in range(4)): return p
        if all(board[i][3-i] == p for i in range(4)): return p
        
    # Verifica empate
    if all(board[3][c] != '.' for c in range(4)):
        return 'Draw'
        
    return None

def get_winning_move(board, player, valid_moves):
    """Retorna a coluna que garante vitória imediata, se houver."""
    for col in valid_moves:
        if check_winner(make_move(board, col, player)) == player:
            return col
    return None

# ==============================================================================
# ESTRUTURA DO NÓ MCTS
# ==============================================================================

class MCTSNode:
    def __init__(self, board, player_just_moved, action, parent):
        self.board = board
        self.player_just_moved = player_just_moved # 'V' ou 'A'
        self.action = action                       # Coluna (0 a 3)
        self.parent = parent
        self.children = []
        self.N = 0                                 # Número de visitas
        self.W = 0.0                               # Número de vitórias do Vermelho ('V')
        self.untried_actions = get_valid_moves(board)

# ==============================================================================
# FUNÇÕES CORE DO MCTS
# ==============================================================================

def get_uct(node, c_param):
    """Calcula o valor UCT de um nó. Se não visitado, retorna infinito."""
    if node.N == 0:
        return float('inf')
    
    # Termo de explotação (alternando perspectiva: maximizar ou minimizar vitórias do vermelho)
    # Se 'V' acabou de jogar, a decisão que o levou até lá foi do oponente ('A' na raiz ou acima).
    # Como UCT guia o jogador atual a escolher os filhos, avaliamos o interesse dele.
    if node.player_just_moved == 'V':
        # Pai é 'A'. O UCT para 'A' ver os filhos seria tentar minimizar as vitórias do 'V'
        # Mas para simplificar o output e alinhar com "W conta vitórias do vermelho", usamos W/N para 'V'
        # e trataremos a alternância correta internamente.
        exploitation = node.W / node.N
    else:
        # Pai é 'V'. Ele quer maximizar as vitórias do 'V'
        exploitation = (node.N - node.W) / node.N
        
    exploration = c_param * math.sqrt(math.log(node.parent.N) / node.N)
    return exploitation + exploration

def select(node, c_param):
    """Fase 1: Seleção. Desce pela árvore escolhendo os filhos com maior UCT."""
    while not node.untried_actions and node.children:
        best_uct = -float('inf')
        best_child = None
        # O sort garante o desempate privilegiando o menor índice (c1 antes de c2)
        for child in sorted(node.children, key=lambda c: c.action):
            uct = get_uct(child, c_param)
            if uct > best_uct:
                best_uct = uct
                best_child = child
        node = best_child
    return node

def expand(node):
    """Fase 2: Expansão. Adiciona UM filho não visitado à árvore."""
    if node.untried_actions:
        action = node.untried_actions.pop(0) # Retira a menor coluna
        next_player = 'A' if node.player_just_moved == 'V' else 'V'
        new_board = make_move(node.board, action, next_player)
        child = MCTSNode(new_board, next_player, action, node)
        node.children.append(child)
        return child
    return node

def rollout_random(board, current_player):
    """Fase 3: Rollout Aleatório. Joga escolhendo movimentos uniformes ao acaso."""
    winner = check_winner(board)
    while winner is None:
        moves = get_valid_moves(board)
        if not moves:
            break
        move = random.choice(moves)
        board = make_move(board, move, current_player)
        current_player = 'A' if current_player == 'V' else 'V'
        winner = check_winner(board)
        
    if winner == 'V': return 1.0
    elif winner == 'A': return 0.0
    return 0.5 # Empate

def rollout_greedy(board, current_player):
    """Fase 3: Rollout Semi-Guloso. Segue as prioridades definidas."""
    winner = check_winner(board)
    while winner is None:
        valid_moves = get_valid_moves(board)
        if not valid_moves:
            break
            
        # Prioridade 1: Vitória imediata
        move = get_winning_move(board, current_player, valid_moves)
        
        # Prioridade 2: Bloquear vitória do adversário
        if move is None:
            opponent = 'A' if current_player == 'V' else 'V'
            move = get_winning_move(board, opponent, valid_moves)
            
        # Prioridade 3: Preferir centro (colunas 1 e 2 equivalem a c2 e c3)
        if move is None:
            centers = [c for c in valid_moves if c in [1, 2]]
            if centers:
                move = random.choice(centers)
                
        # Senão: Aleatório (bordas)
        if move is None:
            move = random.choice(valid_moves)
            
        board = make_move(board, move, current_player)
        current_player = 'A' if current_player == 'V' else 'V'
        winner = check_winner(board)
        
    if winner == 'V': return 1.0
    elif winner == 'A': return 0.0
    return 0.5

def backpropagate(node, result):
    """Fase 4: Retropropagação. Sobe a árvore atualizando contadores N e W."""
    while node is not None:
        node.N += 1
        node.W += result
        node = node.parent

# ==============================================================================
# FUNÇÃO PRINCIPAL DE EXECUÇÃO MCTS
# ==============================================================================

def run_mcts(initial_board, iterations, c_param, rollout_type):
    # Nó raiz: a rodada é do 'V', então o jogador que "acabou de jogar" simulado é o 'A'
    root = MCTSNode(initial_board, 'A', None, None)
    
    start_time = time.time()
    
    for _ in range(iterations):
        node = select(root, c_param)
        
        winner = check_winner(node.board)
        if winner is None:
            node = expand(node)
            next_player = 'A' if node.player_just_moved == 'V' else 'V'
            if rollout_type == 'random':
                result = rollout_random(node.board, next_player)
            else:
                result = rollout_greedy(node.board, next_player)
        else:
            # Nó folha real da árvore do jogo
            if winner == 'V': result = 1.0
            elif winner == 'A': result = 0.0
            else: result = 0.5
            
        backpropagate(node, result)
        
    exec_time = (time.time() - start_time) * 1000 # Tempo em ms
    
    # Extrair estatísticas da raiz
    stats = {}
    for action in range(4):
        child = next((c for c in root.children if c.action == action), None)
        if child:
            n, w = child.N, child.W
            wn = w / n if n > 0 else 0.0
            uct = wn + c_param * math.sqrt(math.log(root.N) / n) if n > 0 else float('inf')
            stats[f"c{action+1}"] = (n, w, wn, uct)
        else:
            stats[f"c{action+1}"] = (0, 0, 0.0, float('inf'))
            
    # Escolha da jogada: maior N (desempate por índice)
    best_action = max(stats.keys(), key=lambda k: stats[k][0])
    
    return best_action, stats, exec_time

# ==============================================================================
# EXECUÇÃO DE EXPERIMENTOS
# ==============================================================================

def run_experiments():
    random.seed(42)
    
    initial_board = [
        ['V', 'A', '.', '.'],  # linha 0 = base
        ['A', 'V', '.', '.'],  # linha 1
        ['.', '.', '.', '.'],  # linha 2
        ['.', '.', '.', '.'],  # linha 3 = topo
    ]
    
    rollouts = ['random', 'greedy']
    cs = [0.1, 1.4, 3.0]
    iters_list = [10, 50, 200]
    
    comparative_results = []
    
    for r_type in rollouts:
        for c in cs:
            for iters in iters_list:
                best_action, stats, exec_time = run_mcts(initial_board, iters, c, r_type)
                
                print("="*60)
                print(f"=== ROLLOUT: {r_type} | C: {c} | ITERAÇÕES: {iters} ===")
                print(f"Jogada recomendada: {best_action}")
                print(f"Tempo: {exec_time:.2f} ms")
                print("| Ação | N | W | W/N | UCT final |")
                print("|------|---|---|-----|-----------|")
                for action in ['c1', 'c2', 'c3', 'c4']:
                    n, w, wn, uct = stats[action]
                    uct_str = "inf" if uct == float('inf') else f"{uct:.3f}"
                    print(f"| {action:<4} | {n:<1} | {w:<1} | {wn:<.3f} | {uct_str:<9} |")
                
                comparative_results.append((r_type, c, iters, best_action, exec_time))
                
    # Tabela Final
    print("="*60)
    print("\n| Rollout | C   | Iterações | Jogada | Tempo (ms) |")
    print("|---------|-----|-----------|--------|------------|")
    for row in comparative_results:
        print(f"| {row[0]:<7} | {row[1]:<3.1f} | {row[2]:<9} | {row[3]:<6} | {row[4]:<10.2f} |")

if __name__ == "__main__":
    run_experiments()