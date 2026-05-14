import random
import math

# ==============================================================================
# FUNÇÕES AUXILIARES GERAIS
# ==============================================================================

def calc_h(state):
    """
    Calcula a função heurística h(s): número de pares de rainhas em conflito.
    Um par conflita se está na mesma linha ou mesma diagonal.
    """
    conflitos = 0
    for i in range(8):
        for j in range(i + 1, 8):
            # Conflito de linha ou diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflitos += 1
    return conflitos

def gerar_vizinhos(state):
    """
    Gera todos os 56 vizinhos possíveis do estado atual.
    A ordem de geração é: da coluna 0 a 7, iterando as linhas de 1 a 8,
    o que garante que o desempate lexicográfico seja naturalmente atendido.
    """
    vizinhos = []
    for col in range(8):
        for row in range(1, 9):
            if row != state[col]:
                novo_estado = state[:]
                novo_estado[col] = row
                vizinhos.append((col, row, novo_estado))
    return vizinhos

def format_state(state):
    """Formata a lista do estado para exibição."""
    return f"[{','.join(map(str, state))}]"

# ==============================================================================
# 1. HILL-CLIMBING SIMPLES
# ==============================================================================

def hill_climbing_simples(start_state, silencioso=False):
    """
    Executa o algoritmo de Hill-Climbing Simples.
    Em modo silencioso, não imprime as tabelas (usado no Random Restart).
    """
    current_state = start_state[:]
    current_h = calc_h(current_state)
    passos = 0
    
    if not silencioso:
        print("=" * 60)
        print("1. HILL-CLIMBING SIMPLES")
        print("=" * 60)
        print(f"| {'Passo':^5} | {'Estado':^20} | {'h(s)':^4} |")
        print("-" * 37)
        print(f"| {passos:^5} | {format_state(current_state):^20} | {current_h:^4} |")
    
    while current_h > 0:
        vizinhos = gerar_vizinhos(current_state)
        melhor_vizinho = None
        melhor_h = current_h
        
        # Avalia todos os vizinhos
        # Como o < é estrito, vizinhos com empate de 'h' perdem para o primeiro encontrado,
        # garantindo a escolha baseada na ordem lexicográfica pedida (coluna menor, linha menor).
        for col, row, viz_state in vizinhos:
            h_n = calc_h(viz_state)
            if h_n < melhor_h:
                melhor_h = h_n
                melhor_vizinho = viz_state
        
        # Critério de parada: máximo local ou platô (nenhum vizinho melhora o h atual)
        if melhor_vizinho is None:
            break
            
        current_state = melhor_vizinho
        current_h = melhor_h
        passos += 1
        
        if not silencioso:
            print(f"| {passos:^5} | {format_state(current_state):^20} | {current_h:^4} |")
            
    if not silencioso:
        print("-" * 37)
        print(f"\n[+] Estado final: {format_state(current_state)} com h(s) = {current_h}")
        if current_h == 0:
            print("[+] Diagnóstico: Solução global encontrada!")
        else:
            print("[+] Diagnóstico: Parada em Máximo Local ou Platô (estagnação).")
            
    return current_state, current_h, passos

# ==============================================================================
# 2. RANDOM RESTART HILL-CLIMBING
# ==============================================================================

def random_restart_hill_climbing():
    """
    Executa o Hill-Climbing 20 vezes, partindo de estados aleatórios.
    """
    print("\n" + "=" * 60)
    print("2. RANDOM RESTART HILL-CLIMBING")
    print("=" * 60)
    
    # Semente fixa para reprodutibilidade apenas da primeira execução da bateria
    random.seed(42)
    
    print(f"| {'Exec.':^5} | {'Estado Inicial':^20} | {'Passos':^6} | {'h(s) final':^10} | {'Solução?':^8} |")
    print("-" * 63)
    
    solucoes_encontradas = 0
    
    for i in range(1, 21):
        estado_aleatorio = [random.randint(1, 8) for _ in range(8)]
        estado_final, h_final, passos = hill_climbing_simples(estado_aleatorio, silencioso=True)
        
        solucao = "Sim" if h_final == 0 else "Não"
        if h_final == 0:
            solucoes_encontradas += 1
            
        print(f"| {i:^5} | {format_state(estado_aleatorio):^20} | {passos:^6} | {h_final:^10} | {solucao:^8} |")
        
    taxa_sucesso = (solucoes_encontradas / 20) * 100
    print("-" * 63)
    print(f"\n[+] Total de soluções encontradas: {solucoes_encontradas}/20")
    print(f"[+] Taxa de sucesso: {taxa_sucesso:.1f}%")

# ==============================================================================
# 3. SIMULATED ANNEALING
# ==============================================================================

def simulated_annealing():
    """
    Executa o recozimento simulado.
    
    JUSTIFICATIVA DOS PARÂMETROS:
    - T0 = 10.0: O máximo de conflitos é 28. Movimentos de piora costumam 
      aumentar h(s) em 1 a 4 pontos. Com T0=10, a chance de aceitar uma piora 
      de delta=2 é P = e^(-2/10) ~ 81%, permitindo altíssima exploração inicial.
    - cooling_rate = 0.99: Permite um resfriamento lento e contínuo. 
      Com esse fator, são necessários cerca de 687 passos para ir de 10.0 a 0.01.
    """
    print("\n" + "=" * 60)
    print("3. SIMULATED ANNEALING")
    print("=" * 60)
    
    random.seed(0) # Reprodutibilidade exigida
    
    current_state = [1, 1, 1, 1, 1, 1, 1, 1]
    current_h = calc_h(current_state)
    
    T = 10.0
    T_min = 0.01
    alpha = 0.99
    passo = 0
    
    piores_aceitos = []
    
    print(">>> Resumo a cada 500 passos:")
    print(f"| {'Passo':^6} | {'h(s)':^6} | {'T':^8} |")
    print("-" * 28)
    
    while T >= T_min and current_h > 0:
        if passo % 500 == 0:
            print(f"| {passo:^6} | {current_h:^6} | {T:>8.4f} |")
            
        # Gera UM vizinho aleatório
        col = random.randint(0, 7)
        row = random.randint(1, 8)
        while row == current_state[col]:
            row = random.randint(1, 8)
            
        viz_state = current_state[:]
        viz_state[col] = row
        viz_h = calc_h(viz_state)
        
        delta_E = viz_h - current_h
        
        if delta_E < 0:
            # Melhora -> Aceita sempre
            current_state = viz_state
            current_h = viz_h
        else:
            # Piora -> Aceita com probabilidade P
            P = math.exp(-delta_E / T)
            if random.random() < P:
                if len(piores_aceitos) < 5:
                    piores_aceitos.append({
                        'passo': passo, 'h_antes': current_h, 'h_depois': viz_h, 
                        'delta': delta_E, 'T': T, 'P': P
                    })
                current_state = viz_state
                current_h = viz_h
                
        T = T * alpha
        passo += 1

    # Impressão do log se acabou fora de um múltiplo de 500
    print(f"| {passo:^6} | {current_h:^6} | {T:>8.4f} | (Fim)")
    print("-" * 28)
    
    print("\n>>> Primeiros 5 movimentos piores aceitos:")
    print(f"| {'Passo':^6} | {'h(antes)':^8} | {'h(depois)':^9} | {'delta_E':^7} | {'T':^6} | {'P':^6} |")
    print("-" * 55)
    for reg in piores_aceitos:
        print(f"| {reg['passo']:^6} | {reg['h_antes']:^8} | {reg['h_depois']:^9} | {reg['delta']:^7} | {reg['T']:>6.2f} | {reg['P']:>6.4f} |")
    
    print(f"\n[+] Estado final: {format_state(current_state)}")
    print(f"[+] h(s) final: {current_h}")
    if current_h == 0:
        print("[+] Diagnóstico: Solução encontrada com sucesso!")
    else:
        print("[+] Diagnóstico: Temperatura esgotada sem encontrar a solução ótima.")

# ==============================================================================
# MAIN
# ==============================================================================
if __name__ == "__main__":
    hill_climbing_simples([1, 1, 1, 1, 1, 1, 1, 1])
    random_restart_hill_climbing()
    simulated_annealing()