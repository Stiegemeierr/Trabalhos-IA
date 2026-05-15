


# Relatório - Algoritmos de Busca em Inteligência Artificial - GABRIEL STIEGEMEIER

---

## Questão 01 - Busca em Amplitude, Profundidade e Iterativa

### 1.1 Formulação do Problema

**a) Definição formal do estado:**
A sala atual em que o agente se encontra.

**b) Estado inicial:**
Sala A.

**c) Teste de objetivo:**
Verificar se o estado atual é a sala S.

**d) Função sucessora:**
Retorna os movimentos permitidos e as respectivas salas vizinhas alcançáveis a partir da sala atual.

**e) Função de custo:**
Custo unitário (valor 1) para cada ação de deslocamento entre salas.

---

### 1.2 Execução dos Algoritmos

#### 1.2.1 Grafo Original

#### 1. BUSCA EM AMPLITUDE/LARGURA (BFS)

| Passo | Nó expandido | Conteúdo da fronteira |
| --- | --- | --- |
| 1 | A | [B, C, D] |
| 2 | B | [C, D, E, F] |
| 3 | C | [D, E, F, G, H] |
| 4 | D | [E, F, G, H, I] |
| 5 | E | [F, G, H, I, J] |
| 6 | F | [G, H, I, J, K, L] |
| 7 | G | [H, I, J, K, L, M] |
| 8 | H | [I, J, K, L, M, N, O] |
| 9 | I | [J, K, L, M, N, O, P] |
| 10 | J | [K, L, M, N, O, P] |
| 11 | K | [L, M, N, O, P, Q] |
| 12 | L | [M, N, O, P, Q] |
| 13 | M | [N, O, P, Q, R] |
| 14 | N | [O, P, Q, R] |
| 15 | O | [P, Q, R, S] |
| 16 | P | [Q, R, S] |
| 17 | Q | [R, S] |
| 18 | R | [S] |
| 19 | S | [] |

Resultados da Busca:

* **a) Ordem completa de expansão:** A -> B -> C -> D -> E -> F -> G -> H -> I -> J -> K -> L -> M -> N -> O -> P -> Q -> R -> S
* **b) Conteúdo da fronteira:** (Visto na tabela acima passo a passo)
* **c) Árvore parcial de busca:** [A->B, A->C, A->D, B->E, B->F, C->G, C->H, D->I, E->J, F->K, F->L, G->M, H->N, H->O, I->P, K->Q, M->R, O->S]
* **d) Caminho solução encontrado:** A -> C -> H -> O -> S
* **e) Profundidade da solução:** 4
* **f) Custo da solução:** 4
* **g) Quantidade de nós gerados:** 19
* **h) Quantidade de nós expandidos:** 18

#### 2. BUSCA EM PROFUNDIDADE (DFS)

| Passo | Nó expandido | Conteúdo da fronteira |
| --- | --- | --- |
| 1 | A | [B, C, D] |
| 2 | B | [E, F, C, D] |
| 3 | E | [J, F, C, D] |
| 4 | J | [F, C, D] |
| 5 | F | [K, L, C, D] |
| 6 | K | [Q, L, C, D] |
| 7 | Q | [L, C, D] |
| 8 | L | [C, D] |
| 9 | C | [G, H, D] |
| 10 | G | [M, H, D] |
| 11 | M | [R, H, D] |
| 12 | R | [H, D] |
| 13 | H | [N, O, D] |
| 14 | N | [O, D] |
| 15 | O | [S, D] |
| 16 | S | [D] |

Resultados da Busca:

* **a) Ordem completa de expansão:** A -> B -> E -> J -> F -> K -> Q -> L -> C -> G -> M -> R -> H -> N -> O -> S
* **b) Conteúdo da fronteira:** (Visto na tabela acima passo a passo)
* **c) Árvore parcial de busca:** [O->S, H->N, H->O, M->R, G->M, C->G, C->H, K->Q, F->K, F->L, E->J, B->E, B->F, A->B, A->C, A->D]
* **d) Caminho solução encontrado:** A -> C -> H -> O -> S
* **e) Profundidade da solução:** 4
* **f) Custo da solução:** 4
* **g) Quantidade de nós gerados:** 17
* **h) Quantidade de nós expandidos:** 15

#### 3. BUSCA ITERATIVA EM PROFUNDIDADE (IDS)

#### Iteração com limite de profundidade: 0

| Passo | Nó expandido | Conteúdo da fronteira |
| --- | --- | --- |
| 1 | A (lim) | [] |

#### Iteração com limite de profundidade: 1

| Passo | Nó expandido | Conteúdo da fronteira |
| --- | --- | --- |
| 1 | A | [B, C, D] |
| 2 | B (lim) | [C, D] |
| 3 | C (lim) | [D] |
| 4 | D (lim) | [] |

#### Iteração com limite de profundidade: 2

| Passo | Nó expandido | Conteúdo da fronteira |
| --- | --- | --- |
| 1 | A | [B, C, D] |
| 2 | B | [E, F, C, D] |
| 3 | E (lim) | [F, C, D] |
| 4 | F (lim) | [C, D] |
| 5 | C | [G, H, D] |
| 6 | G (lim) | [H, D] |
| 7 | H (lim) | [D] |
| 8 | D | [I] |
| 9 | I (lim) | [] |

#### Iteração com limite de profundidade: 3

| Passo | Nó expandido | Conteúdo da fronteira |
| --- | --- | --- |
| 1 | A | [B, C, D] |
| 2 | B | [E, F, C, D] |
| 3 | E | [J, F, C, D] |
| 4 | J (lim) | [F, C, D] |
| 5 | F | [K, L, C, D] |
| 6 | K (lim) | [L, C, D] |
| 7 | L (lim) | [C, D] |
| 8 | C | [G, H, D] |
| 9 | G | [M, H, D] |
| 10 | M (lim) | [H, D] |
| 11 | H | [N, O, D] |
| 12 | N (lim) | [O, D] |
| 13 | O (lim) | [D] |
| 14 | D | [I] |
| 15 | I | [P] |
| 16 | P (lim) | [] |

#### Iteração com limite de profundidade: 4

| Passo | Nó expandido | Conteúdo da fronteira |
| --- | --- | --- |
| 1 | A | [B, C, D] |
| 2 | B | [E, F, C, D] |
| 3 | E | [J, F, C, D] |
| 4 | J | [F, C, D] |
| 5 | F | [K, L, C, D] |
| 6 | K | [Q, L, C, D] |
| 7 | Q (lim) | [L, C, D] |
| 8 | L | [C, D] |
| 9 | C | [G, H, D] |
| 10 | G | [M, H, D] |
| 11 | M | [R, H, D] |
| 12 | R (lim) | [H, D] |
| 13 | H | [N, O, D] |
| 14 | N | [O, D] |
| 15 | O | [S, D] |
| 16 | S | [D] |

Resultados da Busca:

* **a) Ordem completa de expansão:** A -> B -> E -> J -> F -> K -> Q -> L -> C -> G -> M -> R -> H -> N -> O -> S
* **b) Conteúdo da fronteira:** (Visto na tabela acima passo a passo)
* **c) Árvore parcial de busca:** [O->S, H->N, H->O, M->R, G->M, C->G, C->H, K->Q, F->K, F->L, E->J, B->E, B->F, A->B, A->C, A->D]
* **d) Caminho solução encontrado:** A -> C -> H -> O -> S
* **e) Profundidade da solução:** 4
* **f) Custo da solução:** 4
* **g) Quantidade de nós gerados:** 47
* **h) Quantidade de nós expandidos:** 27

#### 1.2.2 Grafo Modificado

#### 1. BUSCA EM AMPLITUDE/LARGURA (BFS)

| Passo | Nó expandido | Conteúdo da fronteira |
| --- | --- | --- |
| 1 | A | [D, C, B] |
| 2 | D | [C, B, I] |
| 3 | C | [B, I, H, G] |
| 4 | B | [I, H, G, E, F] |
| 5 | I | [H, G, E, F, P] |
| 6 | H | [G, E, F, P, N, O] |
| 7 | G | [E, F, P, N, O, M] |
| 8 | E | [F, P, N, O, M, J] |
| 9 | F | [P, N, O, M, J, K, L] |
| 10 | P | [N, O, M, J, K, L] |
| 11 | N | [O, M, J, K, L] |
| 12 | O | [M, J, K, L, S] |
| 13 | M | [J, K, L, S, R] |
| 14 | J | [K, L, S, R] |
| 15 | K | [L, S, R, Q] |
| 16 | L | [S, R, Q] |
| 17 | S | [R, Q] |

Resultados da Busca:

* **a) Ordem completa de expansão:** A -> D -> C -> B -> I -> H -> G -> E -> F -> P -> N -> O -> M -> J -> K -> L -> S
* **b) Conteúdo da fronteira:** (Visto na tabela acima passo a passo)
* **c) Árvore parcial de busca:** [A->D, A->C, A->B, D->I, C->H, C->G, B->E, B->F, I->P, H->N, H->O, G->M, E->J, F->K, F->L, O->S, M->R, K->Q]
* **d) Caminho solução encontrado:** A -> C -> H -> O -> S
* **e) Profundidade da solução:** 4
* **f) Custo da solução:** 4
* **g) Quantidade de nós gerados:** 19
* **h) Quantidade de nós expandidos:** 16

#### 2. BUSCA EM PROFUNDIDADE (DFS)

| Passo | Nó expandido | Conteúdo da fronteira |
| --- | --- | --- |
| 1 | A | [D, C, B] |
| 2 | D | [I, C, B] |
| 3 | I | [P, C, B] |
| 4 | P | [C, B] |
| 5 | C | [H, G, B] |
| 6 | H | [N, O, G, B] |
| 7 | N | [O, G, B] |
| 8 | O | [S, G, B] |
| 9 | S | [G, B] |

Resultados da Busca:

* **a) Ordem completa de expansão:** A -> D -> I -> P -> C -> H -> N -> O -> S
* **b) Conteúdo da fronteira:** (Visto na tabela acima passo a passo)
* **c) Árvore parcial de busca:** [O->S, H->N, H->O, C->H, C->G, I->P, D->I, A->D, A->C, A->B]
* **d) Caminho solução encontrado:** A -> C -> H -> O -> S
* **e) Profundidade da solução:** 4
* **f) Custo da solução:** 4
* **g) Quantidade de nós gerados:** 11
* **h) Quantidade de nós expandidos:** 8

#### 3. BUSCA ITERATIVA EM PROFUNDIDADE (IDS)

#### Iteração com limite de profundidade: 0

| Passo | Nó expandido | Conteúdo da fronteira |
| --- | --- | --- |
| 1 | A (lim) | [] |

#### Iteração com limite de profundidade: 1

| Passo | Nó expandido | Conteúdo da fronteira |
| --- | --- | --- |
| 1 | A | [D, C, B] |
| 2 | D (lim) | [C, B] |
| 3 | C (lim) | [B] |
| 4 | B (lim) | [] |

#### Iteração com limite de profundidade: 2

| Passo | Nó expandido | Conteúdo da fronteira |
| --- | --- | --- |
| 1 | A | [D, C, B] |
| 2 | D | [I, C, B] |
| 3 | I (lim) | [C, B] |
| 4 | C | [H, G, B] |
| 5 | H (lim) | [G, B] |
| 6 | G (lim) | [B] |
| 7 | B | [E, F] |
| 8 | E (lim) | [F] |
| 9 | F (lim) | [] |

#### Iteração com limite de profundidade: 3

| Passo | Nó expandido | Conteúdo da fronteira |
| --- | --- | --- |
| 1 | A | [D, C, B] |
| 2 | D | [I, C, B] |
| 3 | I | [P, C, B] |
| 4 | P (lim) | [C, B] |
| 5 | C | [H, G, B] |
| 6 | H | [N, O, G, B] |
| 7 | N (lim) | [O, G, B] |
| 8 | O (lim) | [G, B] |
| 9 | G | [M, B] |
| 10 | M (lim) | [B] |
| 11 | B | [E, F] |
| 12 | E | [J, F] |
| 13 | J (lim) | [F] |
| 14 | F | [K, L] |
| 15 | K (lim) | [L] |
| 16 | L (lim) | [] |

#### Iteração com limite de profundidade: 4

| Passo | Nó expandido | Conteúdo da fronteira |
| --- | --- | --- |
| 1 | A | [D, C, B] |
| 2 | D | [I, C, B] |
| 3 | I | [P, C, B] |
| 4 | P | [C, B] |
| 5 | C | [H, G, B] |
| 6 | H | [N, O, G, B] |
| 7 | N | [O, G, B] |
| 8 | O | [S, G, B] |
| 9 | S | [G, B] |

Resultados da Busca:

* **a) Ordem completa de expansão:** A -> D -> I -> P -> C -> H -> N -> O -> S
* **b) Conteúdo da fronteira:** (Visto na tabela acima passo a passo)
* **c) Árvore parcial de busca:** [O->S, H->N, H->O, C->H, C->G, I->P, D->I, A->D, A->C, A->B]
* **d) Caminho solução encontrado:** A -> C -> H -> O -> S
* **e) Profundidade da solução:** 4
* **f) Custo da solução:** 4
* **g) Quantidade de nós gerados:** 41
* **h) Quantidade de nós expandidos:** 22

---

### 1.3 Análise do Impacto da Ordem dos Sucessores

**a) O caminho solução mudou:**  
Não. Todos os algoritmos encontraram o mesmo caminho: A -> C -> H -> O -> S, com profundidade e custo iguais a 4.

**b) A quantidade de nós expandidos mudou:**  
Sim.  
- BFS: de 18 para 16 nós expandidos.  
- DFS: de 15 para 8 nós expandidos.  
- IDS: de 27 para 22 nós expandidos.

**c) Algum algoritmo foi mais sensível à ordem dos sucessores:**  
Sim. O DFS foi o mais sensível à ordem dos sucessores, reduzindo a expansão de 15 para 8 nós. O BFS teve pouca variação, indo de 18 para 16 nós.

**d) Qual algoritmo apresentou maior consumo de memória:**  
O BFS apresentou maior consumo de memória. Sua fronteira chegou a conter até 7 nós simultaneamente nas execuções.

**e) Qual algoritmo encontrou a solução mais rapidamente:**  
O DFS encontrou a solução mais rapidamente. No grafo modificado, expandiu apenas 8 nós, contra 16 do BFS e 22 do IDS.

---

### 1.4 Comparação Teórica dos Algoritmos

| **Critério** | **BFS (Largura)** | **DFS (Profundidade)** | **IDS (Aprof. Iterativo)** |
| --- | --- | --- | --- |
| **a) Completude** | Sim | Sim (em árvores finitas) | Sim |
| **b) Otimalidade** | Sim (custos unitários) | Não | Sim (custos unitários) |
| **c) Complexidade de tempo** | $O(b^d)$ | $O(b^m)$ | $O(b^d)$ |
| **d) Complexidade de espaço** | $O(b^d)$ | $O(bm)$ | $O(bd)$ |
| **e) Dependência da ordem** | Baixa | Alta | Alta |
| **f) Comportamento (árvores profundas)** | Estoura a memória rapidamente | Pode se perder no caminho mais profundo | Controlado e seguro |
| **g) Adequação para problemas grandes** | Ruim | Ruim / Risco de loops | Excelente |

**Justificativas:**

**c) Complexidade de tempo:** BFS e IDS exploram o espaço até a profundidade da solução ($d$), processando um total de nós proporcional a $b^d$. DFS explora os ramos até a profundidade máxima ($m$), podendo processar $b^m$ nós no pior cenário.

**d) Complexidade de espaço:** BFS armazena todos os nós do nível atual na fronteira, exigindo memória exponencial $O(b^d)$. DFS e IDS armazenam apenas o ramo atual explorado, resultando em consumo de memória linear.

**f) Comportamento em árvores profundas:** BFS esgota a memória RAM antes de alcançar soluções muito profundas. DFS mergulha em caminhos longos ou infinitos irrelevantes, enquanto o IDS limita a busca gradativamente, contornando a falha de ambos.

**g) Adequação para problemas grandes:** IDS é o mais adequado porque combina a garantia de otimalidade (do BFS) com o baixo consumo de memória (do DFS). O BFS falha por falta de espaço, e o DFS pode não encontrar a solução ideal de forma eficiente.

---
---

## Questão 02 - Busca Gulosa e A*

### 2.1 Formulação do Problema

**a) Representação dos estados:**
A posição atual do agente no ambiente (nó).

**b) Estado inicial:**
Nó A.

**c) Teste de objetivo:**
Verificar se a posição atual do agente é o nó T.

**d) Função sucessora:**
Retorna os nós vizinhos alcançáveis a partir do nó atual, acompanhados de seus custos de transição.

**e) Função de custo:**
Soma do custo das arestas percorridas do estado inicial até o estado atual.

**f) Interpretação da heurística h(n):**
Estimativa do custo (ou distância) da posição atual até a posição objetivo T. Observando o grafo, a heurística se mostra admissível, pois para qualquer nó $n$, $h(n)$ nunca superestima o custo real mínimo para alcançar o objetivo a partir de $n$ (ex: $h(A) = 10$, custo real $A \to C \to H \to O \to T = 19$; $h(H) = 4$, custo real $H \to O \to T = 9$).

---

### 2.2 Execução dos Algoritmos

#### 2.2.1 Heurística Original

#### 2.2.1.1 GREEDY BEST-FIRST SEARCH

| Passo | Nó expandido | h(n) | Fronteira |
| --- | --- | --- | --- |
| 1 | A | 10 | [C(7), B(8), D(9)] |
| 2 | C | 7 | [H(4), G(6), B(8), D(9)] |
| 3 | H | 4 | [O(1), N(4), G(6), B(8), D(9)] |
| 4 | O | 1 | [T(0), N(4), G(6), B(8), D(9)] |
| 5 | T | 0 | [N(4), G(6), B(8), D(9)] |

* **Ordem de expansão:** A -> C -> H -> O -> T
* **Caminho solução:** A -> C -> H -> O -> T
* **Custo da solução:** 19
* **Nós gerados:** 9 | Nós expandidos: 5

#### 2.2.1.2 A* SEARCH

| Passo | Nó | g(n) | h(n) | f(n) | Fronteira |
| --- | --- | --- | --- | --- | --- |
| 1 | A | 0 | 10 | 10 | [B(10), C(11), D(12)] |
| 2 | B | 2 | 8 | 10 | [C(11), E(11), D(12), F(12)] |
| 3 | C | 4 | 7 | 11 | [E(11), D(12), F(12), G(14), H(14)] |
| 4 | E | 5 | 6 | 11 | [D(12), F(12), G(14), H(14), J(14)] |
| 5 | D | 3 | 9 | 12 | [F(12), I(12), G(14), H(14), J(14)] |
| 6 | F | 7 | 5 | 12 | [I(12), K(13), G(14), H(14), J(14), L(18)] |
| 7 | I | 5 | 7 | 12 | [K(13), G(14), H(14), J(14), L(18), P(18)] |
| 8 | K | 10 | 3 | 13 | [G(14), H(14), J(14), R(15), L(18), P(18)] |
| 9 | G | 8 | 6 | 14 | [H(14), J(14), R(15), M(17), L(18), P(18)] |
| 10 | H | 10 | 4 | 14 | [J(14), R(15), O(15), M(17), N(17), L(18), P(18)] |
| 11 | J | 9 | 5 | 14 | [R(15), O(15), M(17), N(17), Q(17), L(18), P(18)] |
| 12 | R | 13 | 2 | 15 | [O(15), M(17), N(17), Q(17), T(17), L(18), P(18)] |
| 13 | O | 14 | 1 | 15 | [M(17), N(17), Q(17), T(17), L(18), P(18), T(19)] |
| 14 | M | 14 | 3 | 17 | [N(17), Q(17), T(17), S(17), L(18), P(18), T(19)] |
| 15 | N | 13 | 4 | 17 | [Q(17), T(17), S(17), L(18), P(18), T(19)] |
| 16 | Q | 13 | 4 | 17 | [T(17), S(17), L(18), P(18), T(19)] |
| 17 | T | 17 | 0 | 17 | [S(17), L(18), P(18), T(19)] |

* **Ordem de expansão:** A -> B -> C -> E -> D -> F -> I -> K -> G -> H -> J -> R -> O -> M -> N -> Q -> T
* **Caminho solução:** A -> B -> F -> K -> R -> T
* **Custo da solução:** 17
* **Nós gerados:** 21 | Nós expandidos: 17

#### 2.2.2 Heurística Modificada

#### 2.2.2.1 GREEDY BEST-FIRST SEARCH

| Passo | Nó expandido | h(n) | Fronteira |
| --- | --- | --- | --- |
| 1 | A | 10 | [C(2), D(9), B(20)] |
| 2 | C | 2 | [G(6), D(9), H(15), B(20)] |
| 3 | G | 6 | [M(3), D(9), H(15), B(20)] |
| 4 | M | 3 | [S(1), D(9), H(15), B(20)] |
| 5 | S | 1 | [T(0), D(9), H(15), B(20)] |
| 6 | T | 0 | [D(9), H(15), B(20)] |

* **Ordem de expansão:** A -> C -> G -> M -> S -> T
* **Caminho solução:** A -> C -> G -> M -> S -> T
* **Custo da solução:** 19
* **Nós gerados:** 9 | Nós expandidos: 6

#### 2.2.2.2 A* SEARCH

| Passo | Nó | g(n) | h(n) | f(n) | Fronteira |
| --- | --- | --- | --- | --- | --- |
| 1 | A | 0 | 10 | 10 | [C(6), D(12), B(22)] |
| 2 | C | 4 | 2 | 6 | [D(12), G(14), B(22), H(25)] |
| 3 | D | 3 | 9 | 12 | [I(12), G(14), B(22), H(25)] |
| 4 | I | 5 | 7 | 12 | [G(14), P(18), B(22), H(25)] |
| 5 | G | 8 | 6 | 14 | [M(17), P(18), B(22), H(25)] |
| 6 | M | 14 | 3 | 17 | [S(17), P(18), B(22), H(25)] |
| 7 | S | 16 | 1 | 17 | [P(18), T(19), B(22), H(25)] |
| 8 | P | 10 | 8 | 18 | [T(19), B(22), H(25)] |
| 9 | T | 19 | 0 | 19 | [B(22), H(25)] |

* **Ordem de expansão:** A -> C -> D -> I -> G -> M -> S -> P -> T
* **Caminho solução:** A -> C -> G -> M -> S -> T
* **Custo da solução:** 19
* **Nós gerados:** 11 | Nós expandidos: 9

---

### 2.3 Análise do Impacto da Heurística

**a) A solução encontrada mudou:**  
Sim.  
- Greedy: de A -> C -> H -> O -> T para A -> C -> G -> M -> S -> T.  
- A*: de A -> B -> F -> K -> R -> T para A -> C -> G -> M -> S -> T.

**b) O custo da solução mudou:**  
Sim.  
- Greedy manteve custo 19 nas duas heurísticas.  
- A* mudou de custo 17 para 19.

**c) A busca gulosa encontrou solução ótima:**  
Não. O custo ótimo real do grafo original é 17, mas a busca gulosa encontrou custo 19 em ambas as heurísticas.

**d) O A* encontrou solução ótima:**  
Com a heurística original, sim, encontrou custo 17.  
Com a heurística inadmissível, não, encontrou custo 19.

**e) Qual algoritmo expandiu menos nós:**  
A busca gulosa expandiu menos nós.  
- Heurística original: 5 nós contra 17 do A*.  
- Heurística modificada: 6 nós contra 9 do A*.

**f) Qual algoritmo foi mais sensível à heurística:**  
O A* foi mais sensível à heurística. Seu caminho mudou e o custo piorou de 17 para 19, além da ordem de expansão cair de 17 para 9 nós expandidos.

---

### 2.4 Comparação Teórica dos Algoritmos

| **Critério** | **Greedy Best-First Search (Gulosa)** | **A* (A-Star)** |
| --- | --- | --- |
| **a) Completude** | Sim (em grafos finitos com lista fechada) | Sim |
| **b) Otimalidade** | Não | Sim (se $h(n)$ for admissível) |
| **c) Consumo de memória** | Alto | Alto |
| **d) Dependência da heurística** | Total (exclusiva) | Parcial (balanceada) |
| **e) Custo computacional** | Geralmente baixo (rápido) | Moderado a Alto (expande mais nós) |
| **f) Qualidade das soluções** | Subótima (ignora custos das arestas) | Ótima (menor custo total possível) |
| **g) Comportamento em grafos grandes** | Rápido, mas entrega soluções piores | Frequentemente limitado pela memória RAM |

**Justificativas:**

**a) Completude:** Ambos encontram a solução se ela existir, desde que utilizem lista fechada para evitar ciclos em grafos finitos. Sem controle de estados repetidos, o algoritmo guloso pode ficar preso em loops irrelevantes.

**b) Otimalidade:** O Greedy foca apenas na distância estimada até o alvo, ignorando o peso do trajeto já feito, o que gera caminhos mais caros. O A* garante a rota mais barata possível, condicionada ao uso de uma heurística que não minta para cima.

**c) Consumo de memória:** Ambos os algoritmos mantêm todos os nós visitados e gerados em memória (fronteira e lista fechada). Esse crescimento de dados é exponencial, sendo o principal gargalo técnico de ambos.

**d) Dependência da heurística:** O Greedy usa apenas $h(n)$ para guiar a busca, sendo facilmente enganado por estimativas ruins. O A* usa a fórmula $f(n) = g(n) + h(n)$, mitigando falhas da heurística ao considerar o custo real $g(n)$ já pago.

**e) Custo computacional:** O Greedy tende a ir direto ao alvo, expandindo um número menor de nós e economizando ciclos de CPU. O A* processa e explora diversas ramificações paralelas para comprovar que nenhuma é mais barata, exigindo mais tempo de máquina.

**f) Qualidade das soluções:** O Greedy é míope e frequentemente entrega caminhos de alto custo porque se atrai cegamente por nós com heurística baixa. O A* entrega sempre o caminho perfeito e de menor custo global.

**g) Comportamento em grafos grandes:** O Greedy é útil para encontrar rapidamente "qualquer caminho" em malhas imensas. O A* tenta varrer muitas frentes promissoras para garantir o melhor caminho, correndo sério risco de esgotar a memória antes do fim.

**Observação final sobre admissibilidade:** Quando a heurística $h(n)$ deixa de ser admissível (ou seja, passa a superestimar o custo real até o objetivo), o algoritmo A* perde sua garantia matemática de otimalidade. Ao inflacionar falsamente o custo $f(n)$ de caminhos que fazem parte da rota ótima, o A* é enganado, descarta precocemente as melhores opções e acaba retornando uma solução subótima (comportando-se de maneira muito semelhante ao algoritmo guloso).


---
---

## Questão 03 - Busca Local: Hill-Climbing e Simulated Annealing

### 3.1 Formulação do Problema

**a) Representação do estado:**
Vetor de 8 posições `[s1, s2, ..., s8]`, onde cada elemento indica a linha ocupada pela rainha em sua respectiva coluna.

**b) Definição de vizinho:**
Estado resultante do deslocamento de exatamente uma rainha para uma nova linha dentro da sua mesma coluna.

**c) Função de avaliação:**
A heurística $h(s)$, que quantifica o número total de pares de rainhas se atacando simultaneamente no tabuleiro.

**d) Critério de parada:**
Atingir o valor ótimo da função de avaliação correspondente a zero conflitos, ou seja, $h(s) = 0$.

**e) Interpretação da superfície de busca:**
Paisagem topológica onde cada ponto é um estado possível e a altura é o número de conflitos $h(s)$, consistindo em uma descida para encontrar o mínimo global.

---

### 3.2 Hill-Climbing: Execução Manual

### Tabela resumo

| Iteração | Estado | h(s) |
| --- | --- | --- |
| 0 | [1, 1, 1, 1, 1, 1, 1, 1] | 28 |
| 1 | [2, 8, 1, 1, 1, 1, 1, 1] | 21 |
| 2 | [2, 8, 1, 7, 1, 1, 1, 1] | 15 |
| 3 | [2, 8, 1, 7, 1, 6, 1, 1] | 10 |
| 4 | [2, 8, 1, 7, 1, 6, 1, 5] | 6 |
| 5 | [2, 8, 1, 7, 4, 6, 1, 5] | 3 |
| 6 | [2, 8, 1, 7, 4, 6, 1, 5] | 1 |

---

### Por iteração

**Iteração 0:**

* Estado atual: [1, 1, 1, 1, 1, 1, 1, 1]
* h(s) atual: 28
* 5 melhores vizinhos:

| Col. movida | Nova linha | Estado vizinho | h(s) |
| --- | --- | --- | --- |
| 2 | 8 | [1, 8, 1, 1, 1, 1, 1, 1] | 21 |
| 3 | 7 | [1, 1, 7, 1, 1, 1, 1, 1] | 21 |
| 3 | 8 | [1, 1, 8, 1, 1, 1, 1, 1] | 21 |
| 4 | 6 | [1, 1, 1, 6, 1, 1, 1, 1] | 21 |
| 4 | 7 | [1, 1, 1, 7, 1, 1, 1, 1] | 21 |

* Estado escolhido: [1, 8, 1, 1, 1, 1, 1, 1]
* Motivo: Possui o menor h(s) empatado e é o primeiro na ordem lexicográfica (menor coluna, menor linha).

**Iteração 1:**

* Estado atual: [1, 8, 1, 1, 1, 1, 1, 1]
* h(s) atual: 21
* 5 melhores vizinhos:

| Col. movida | Nova linha | Estado vizinho | h(s) |
| --- | --- | --- | --- |
| 1 | 2 | [2, 8, 1, 1, 1, 1, 1, 1] | 15 |
| 4 | 7 | [1, 8, 1, 7, 1, 1, 1, 1] | 15 |
| 5 | 6 | [1, 8, 1, 1, 6, 1, 1, 1] | 15 |
| 5 | 7 | [1, 8, 1, 1, 7, 1, 1, 1] | 15 |
| 6 | 7 | [1, 8, 1, 1, 1, 7, 1, 1] | 15 |

* Estado escolhido: [2, 8, 1, 1, 1, 1, 1, 1]
* Motivo: Minimiza h(s) para 15 e vence o desempate lexicográfico pela coluna 1.

**Iteração 2:**

* Estado atual: [2, 8, 1, 1, 1, 1, 1, 1]
* h(s) atual: 15
* 5 melhores vizinhos:

| Col. movida | Nova linha | Estado vizinho | h(s) |
| --- | --- | --- | --- |
| 4 | 7 | [2, 8, 1, 7, 1, 1, 1, 1] | 10 |
| 5 | 7 | [2, 8, 1, 1, 7, 1, 1, 1] | 10 |
| 6 | 5 | [2, 8, 1, 1, 1, 5, 1, 1] | 10 |
| 6 | 6 | [2, 8, 1, 1, 1, 6, 1, 1] | 10 |
| 7 | 6 | [2, 8, 1, 1, 1, 1, 6, 1] | 10 |

* Estado escolhido: [2, 8, 1, 7, 1, 1, 1, 1]
* Motivo: Remove 5 conflitos da primeira linha sem gerar novos ataques com as rainhas já posicionadas, vencendo no desempate.

**Iteração 3:**

* Estado atual: [2, 8, 1, 7, 1, 1, 1, 1]
* h(s) atual: 10
* 5 melhores vizinhos:

| Col. movida | Nova linha | Estado vizinho | h(s) |
| --- | --- | --- | --- |
| 6 | 6 | [2, 8, 1, 7, 1, 6, 1, 1] | 6 |
| 7 | 6 | [2, 8, 1, 7, 1, 1, 6, 1] | 6 |
| 8 | 5 | [2, 8, 1, 7, 1, 1, 1, 5] | 6 |
| 3 | 6 | [2, 8, 6, 7, 1, 1, 1, 1] | 7 |
| 3 | 8 | [2, 8, 8, 7, 1, 1, 1, 1] | 7 |

* Estado escolhido: [2, 8, 1, 7, 1, 6, 1, 1]
* Motivo: Alcança o menor h(s) possível (6) ao encontrar um espaço vazio nas diagonais e linhas, sendo priorizado pela regra lexicográfica.

**Iteração 4:**

* Estado atual: [2, 8, 1, 7, 1, 6, 1, 1]
* h(s) atual: 6
* 5 melhores vizinhos:

| Col. movida | Nova linha | Estado vizinho | h(s) |
| --- | --- | --- | --- |
| 8 | 5 | [2, 8, 1, 7, 1, 6, 1, 5] | 3 |
| 3 | 5 | [2, 8, 5, 7, 1, 6, 1, 1] | 4 |
| 5 | 5 | [2, 8, 1, 7, 5, 6, 1, 1] | 4 |
| 7 | 4 | [2, 8, 1, 7, 1, 6, 4, 1] | 4 |
| 8 | 3 | [2, 8, 1, 7, 1, 6, 1, 3] | 4 |

* Estado escolhido: [2, 8, 1, 7, 1, 6, 1, 5]
* Motivo: É o único vizinho capaz de baixar os conflitos para 3, tornando-se a escolha obrigatória.

**Iteração 5:**

* Estado atual: [2, 8, 1, 7, 1, 6, 1, 5]
* h(s) atual: 3
* 5 melhores vizinhos:

| Col. movida | Nova linha | Estado vizinho | h(s) |
| --- | --- | --- | --- |
| 5 | 4 | [2, 8, 1, 7, 4, 6, 1, 5] | 1 |
| 3 | 4 | [2, 8, 4, 7, 1, 6, 1, 5] | 2 |
| 3 | 5 | [2, 8, 5, 7, 1, 6, 1, 5] | 2 |
| 5 | 3 | [2, 8, 1, 7, 3, 6, 1, 5] | 2 |
| 7 | 4 | [2, 8, 1, 7, 1, 6, 4, 5] | 2 |

* Estado escolhido: [2, 8, 1, 7, 4, 6, 1, 5]
* Motivo: Reduz o h(s) estritamente para 1, eliminando todos os conflitos exceto o par remanescente na linha 1.

**Iteração 6 (Critério de parada):**

* Estado atual: [2, 8, 1, 7, 4, 6, 1, 5]
* h(s) atual: 1
* 5 melhores vizinhos:

| Col. movida | Nova linha | Estado vizinho | h(s) |
| --- | --- | --- | --- |
| 3 | 3 | [2, 8, 3, 7, 4, 6, 1, 5] | 1 |
| 3 | 5 | [2, 8, 5, 7, 4, 6, 1, 5] | 1 |
| 3 | 8 | [2, 8, 8, 7, 4, 6, 1, 5] | 1 |
| 7 | 3 | [2, 8, 1, 7, 4, 6, 3, 5] | 1 |
| 7 | 8 | [2, 8, 1, 7, 4, 6, 8, 5] | 1 |

* Estado escolhido: Nenhum.
* Motivo: Nenhum vizinho gerou um valor estritamente menor que o h(s) atual.

---

### Diagnóstico final

* **Tipo de parada:** Platô (ou Mínimo Local).
* **Por que ocorreu:** Nenhum movimento único de uma rainha conseguiu eliminar o conflito final sem gerar um ou mais novos conflitos com as rainhas já bem posicionadas.
* **Como afetou a busca:** O algoritmo estagnou de forma subótima e parou antes de encontrar a solução global (h=0).
* **Como poderia ser evitado:** Permitindo movimentos laterais (para navegar no platô), reinícios aleatórios (Random-Restart Hill Climbing) ou aceitando pioras temporárias (Simulated Annealing).


---

### 3.3 Execução dos Algoritmos

#### 3.3.1 Hill-Climbing Simples

| Passo | Estado | h(s) |
| --- | --- | --- |
| 0 | [1,1,1,1,1,1,1,1] | 28 |
| 1 | [1,8,1,1,1,1,1,1] | 21 |
| 2 | [2,8,1,1,1,1,1,1] | 15 |
| 3 | [2,8,1,7,1,1,1,1] | 10 |
| 4 | [2,8,1,7,1,6,1,1] | 6 |
| 5 | [2,8,1,7,1,6,1,5] | 3 |
| 6 | [2,8,1,7,4,6,1,5] | 1 |

* **Estado final:** [2,8,1,7,4,6,1,5] com h(s) = 1
* **Diagnóstico:** Parada em Máximo Local ou Platô (estagnação).

#### 3.3.2 Random Restart Hill-Climbing (20 execuções)

| Exec. | Estado Inicial | Passos | h(s) final | Solução? |
| --- | --- | --- | --- | --- |
| 1 | [2,1,5,4,4,3,2,2] | 4 | 1 | Não |
| 2 | [7,1,1,2,4,4,1,4] | 5 | 0 | Sim |
| 3 | [7,4,8,5,1,3,7,6] | 2 | 2 | Não |
| 4 | [5,3,4,6,2,2,7,2] | 2 | 1 | Não |
| 5 | [6,6,5,1,8,2,7,2] | 4 | 0 | Sim |
| 6 | [5,6,4,2,1,4,5,2] | 3 | 1 | Não |
| 7 | [4,2,7,5,8,6,3,6] | 1 | 2 | Não |
| 8 | [6,4,5,2,3,4,3,8] | 3 | 1 | Não |
| 9 | [7,5,4,6,1,4,1,6] | 4 | 1 | Não |
| 10 | [7,5,2,4,6,4,8,7] | 2 | 2 | Não |
| 11 | [8,3,5,3,4,5,7,7] | 4 | 1 | Não |
| 12 | [6,4,3,8,2,1,2,3] | 3 | 1 | Não |
| 13 | [3,7,2,7,7,8,5,1] | 2 | 2 | Não |
| 14 | [2,5,6,2,5,7,3,8] | 3 | 2 | Não |
| 15 | [1,5,3,2,5,4,3,6] | 3 | 2 | Não |
| 16 | [3,1,6,8,1,2,6,5] | 2 | 1 | Não |
| 17 | [4,1,4,2,2,8,2,3] | 3 | 1 | Não |
| 18 | [3,8,3,5,7,4,4,5] | 3 | 1 | Não |
| 19 | [7,6,8,8,2,4,4,2] | 4 | 2 | Não |
| 20 | [6,1,4,4,1,2,1,4] | 5 | 1 | Não |

* **Total de soluções encontradas:** 2/20
* **Taxa de sucesso:** 10.0%

#### 3.3.3 Simulated Annealing

Resumo a cada 500 passos:

| Passo | h(s) | T |
| --- | --- | --- |
| 0 | 28 | 10.0000 |
| 500 | 1 | 0.0657 |
| 688 | 1 | 0.0099 (Fim) |

Primeiros 5 movimentos piores aceitos:

| Passo | h(antes) | h(depois) | delta_E | T | P |
| --- | --- | --- | --- | --- | --- |
| 6 | 4 | 6 | 2 | 9.41 | 0.8086 |
| 7 | 6 | 7 | 1 | 9.32 | 0.8983 |
| 9 | 6 | 6 | 0 | 9.14 | 1.0000 |
| 11 | 5 | 6 | 1 | 8.95 | 0.8943 |
| 13 | 5 | 7 | 2 | 8.78 | 0.7962 |

* **Estado final:** [6,2,5,1,7,4,8,3]
* **h(s) final:** 1
* **Diagnóstico:** Temperatura esgotada sem encontrar a solução ótima.

---

### 3.4 Comparação Final dos Algoritmos

| **Critério** | **Hill-Climbing Simples** | **Random Restart Hill-Climbing** | **Simulated Annealing** |
| --- | --- | --- | --- |
| **a) Qualidade das soluções** | Baixa | Alta | Média/Baixa |
| **b) Velocidade de convergência** | Muito alta | Muito alta (por rodada) | Baixa |
| **c) Sensibilidade ao estado inicial** | Total | Alta (explorada a favor) | Baixa |
| **d) Capacidade de escapar de máximos locais** | Nula | Alta (via reinício) | Média (via probabilidade) |
| **e) Custo computacional** | Muito baixo | Baixo a Médio | Alto |
| **f) Estabilidade dos resultados** | Constante (determinístico) | Variável (depende da sorte inicial) | Variável (estocástico) |

**a) Qualidade das soluções:** O Random Restart foi o único capaz de encontrar a solução global perfeita ($h=0$) em 2 de suas 20 execuções. O Hill-Climbing e o Simulated Annealing falharam em encontrar o ótimo global, encerrando com 1 conflito restante ($h=1$).

**b) Velocidade de convergência:** O Hill-Climbing clássico e as execuções isoladas do Random Restart precisaram de pouquíssimas iterações para estagnar (entre 1 e 6 passos). O Simulated Annealing foi consideravelmente mais lento, iterando 688 vezes até a temperatura cair de $10.0$ para $0.0099$.

**c) Sensibilidade ao estado inicial:** O Hill-Climbing evidenciou sua dependência extrema, falhando irreversivelmente ao iniciar em `[1,1,1,1,1,1,1,1]`. O Random Restart validou essa premissa: bastou mudar o estado inicial aleatoriamente para o algoritmo contornar as topologias ruins e resolver o problema (execuções 2 e 5).

**d) Capacidade de escapar de máximos locais:** O Hill-Climbing ficou totalmente preso no passo 6 sem conseguir piorar o estado para sair do platô. O Simulated Annealing executou movimentos reais de fuga (como aceitar a piora de $h=4$ para $6$ com probabilidade de $80.86\%$), mas ainda assim falhou, enquanto o Random Restart escapou pelo simples ato de recomeçar do zero.

**e) Custo computacional:** O Hill-Climbing exigiu o cálculo de vizinhos por apenas 6 passos. O Random Restart teve um custo cumulativo baixo (~60 passos somando as 20 execuções), enquanto o Simulated Annealing realizou 688 expansões iterativas calculando exponenciais complexas para gerar um resultado insatisfatório.

**f) Estabilidade dos resultados:** O Hill-Climbing sempre retornará exatamente a mesma resposta subótima para o mesmo estado inicial. O Random Restart obteve uma estabilidade baixa (apenas 10% de sucesso), provando que a topologia das 8-Rainhas é severamente minada de platôs.

O **Random Restart Hill-Climbing** é o algoritmo mais adequado e eficiente para este problema específico. Como a superfície de busca das 8-Rainhas é repleta de vales subótimos severos, a estratégia de realizar reinícios rápidos de pontos aleatórios garante a descoberta da solução global ($10\%$ de sucesso) gastando infinitamente menos processamento do que técnicas de resfriamento complexas e lentas.

---
---

## Questão 04 - CSP e Otimizações de Busca

### 4.1 Modelagem CSP

**a) Conjunto de variáveis:**
$X = \{T_1, T_2, T_3, T_4, T_5, T_6\}$.

**b) Domínio de cada variável:**
$D_i = \{A, B, C, D\}$ para todo $T_i \in X$.

**c) Restrições unárias:**

* $T_3 \neq A$
**Justificativa:** Limita o domínio de apenas uma variável individualmente ($T_3$).

**d) Restrições binárias:**

* $T_1 \neq T_2, T_2 \neq T_3, T_3 \neq T_4, T_4 \neq T_5, T_5 \neq T_6$
* $T_1 = B \lor T_2 = B$
* $\neg(T_2 = C \land T_3 = C)$ *(Nota: Esta é redundante com $T_2 \neq T_3$, mas formalmente modelada aqui)*
**Justificativa:** Todas avaliam o estado de exatamente duas variáveis simultaneamente para verificar a validade da atribuição.

**e) Restrições globais:**

* $Count(\{T_1, T_2, T_3, T_4, T_5, T_6\}, D) \leq 2$
**Justificativa:** Envolve o conjunto completo de variáveis simultaneamente para calcular uma propriedade agregada (frequência máxima).

**f) Representação do grafo de restrições:**

* **Nós:** $T_1, T_2, T_3, T_4, T_5, T_6$ (representando as variáveis).
* **Arestas binárias (ligam 2 nós):** * $(T_1, T_2)$ -> Representa o limite de turnos consecutivos e a exigência do médico B.
* $(T_2, T_3)$ -> Representa o limite de turnos consecutivos e a restrição do médico C.
* $(T_3, T_4)$, $(T_4, T_5)$, $(T_5, T_6)$ -> Representam os limites de turnos consecutivos.


* **Hiperaresta (liga todos os nós):** Uma aresta global conectando $\{T_1, T_2, T_3, T_4, T_5, T_6\}$ para representar a restrição de limite total do médico D.

---

### 4.2 Backtracking Manual e Análise de MRV e Degree

### BACKTRACKING SIMPLES

| Passo | Variável | Valor | Estado parcial | Resultado |
| --- | --- | --- | --- | --- |
| 1 | T1 | A | {T1=A} | ok |
| 2 | T2 | A | {T1=A, T2=A} | conflito R1 |
| 3 | T2 | B | {T1=A, T2=B} | ok |
| 4 | T3 | A | {T1=A, T2=B, T3=A} | conflito R2 |
| 5 | T3 | B | {T1=A, T2=B, T3=B} | conflito R1 |
| 6 | T3 | C | {T1=A, T2=B, T3=C} | ok |
| 7 | T4 | A | {T1=A, T2=B, T3=C, T4=A} | ok |
| 8 | T5 | A | {T1=A, T2=B, T3=C, T4=A, T5=A} | conflito R1 |
| 9 | T5 | B | {T1=A, T2=B, T3=C, T4=A, T5=B} | ok |
| 10 | T6 | A | {T1=A, T2=B, T3=C, T4=A, T5=B, T6=A} | ok |

**Resumo da Busca:**

* **Solução encontrada:** `{T1=A, T2=B, T3=C, T4=A, T5=B, T6=A}`
* **Total de passos:** 10
* **Total de conflitos:** 4
* **Total de retrocessos (backtracks para mudar valor da mesma variável):** 4

*(Nota: Nesta execução, a restrição global R5 do médico D não foi violada, pois D não foi atribuído nenhuma vez. A restrição R3 foi satisfeita no passo 3. A restrição R4 foi evitada pois T2=B e T3=C. Os retrocessos ocorreram apenas localmente nas variáveis sendo testadas sem precisar voltar para a variável anterior no histórico).*

---

### MRV + DEGREE HEURISTIC

**Análise do Estado Inicial:**

* **Domínios iniciais após aplicar restrições unárias:**
* $D(T_1) = \{A, B, C, D\}$ (tamanho 4)
* $D(T_2) = \{A, B, C, D\}$ (tamanho 4)
* $D(T_3) = \{B, C, D\}$ (tamanho 3, pois $T_3 \neq A$ pela R2)
* $D(T_4) = \{A, B, C, D\}$ (tamanho 4)
* $D(T_5) = \{A, B, C, D\}$ (tamanho 4)
* $D(T_6) = \{A, B, C, D\}$ (tamanho 4)


* **Grafo de restrições (Degree / Arestas incidentes):**
* $T_1$: conectada a $T_2$ (R1, R3).
* $T_2$: conectada a $T_1$ (R1, R3), $T_3$ (R1, R4).
* $T_3$: conectada a $T_2$ (R1, R4), $T_4$ (R1).
* $T_4$: conectada a $T_3$ (R1), $T_5$ (R1).
* $T_5$: conectada a $T_4$ (R1), $T_6$ (R1).
* $T_6$: conectada a $T_5$ (R1).
*(A restrição global R5 envolve todas as variáveis).*



**Passo a passo da escolha:**

1. **Variável escolhida:** $T_3$.
* **Por que:** Tem o menor domínio disponível (MRV = 3 valores). Todas as outras variáveis têm 4 valores no domínio.
* **Ação:** Atribuímos $T_3 = B$ (primeiro valor em ordem alfabética do seu domínio). Isso aciona a Forward Checking/Propagação de restrições: $B$ é removido do domínio de $T_2$ e $T_4$ (devido à R1).


2. **Variável escolhida:** $T_2$.
* **Por que:** Os domínios atualizados são: $T_2 = \{A, C, D\}$ (MRV=3), $T_4 = \{A, C, D\}$ (MRV=3), os demais têm 4. Há empate no MRV entre $T_2$ e $T_4$. Aplicamos a Degree Heuristic. $T_2$ possui restrições ativas com as variáveis não atribuídas $T_1$ (R1, R3), enquanto $T_4$ possui restrições com $T_5$ (R1). $T_2$ é a variável mais restritiva (maior grau não atribuído).
* **Ação:** Atribuímos $T_2 = A$. Propagação: remove $A$ de $T_1$.


3. **Variável escolhida:** $T_1$.
* **Por que:** Domínios atualizados: $T_1 = \{B, C, D\}$ (MRV=3). $T_4 = \{A, C, D\}$ (MRV=3). O restante tem 4. Empate MRV. Pela Degree Heuristic, $T_1$ está ligada a zero variáveis não atribuídas (R3 já foi violada parcialmente, pois precisamos de B em $T_1$ ou $T_2$). $T_4$ está conectada a $T_5$. A Degree priorizaria $T_4$. No entanto, se o algoritmo for sofisticado o suficiente para perceber a R3 global precocemente, ele focaria em $T_1$. Vamos seguir a Degree estrutural clássica: $T_4$ é escolhida.
* **Ação:** Atribuímos $T_4 = A$. Propagação: remove $A$ de $T_5$.


4. **Variável escolhida:** $T_5$.
* **Por que:** Domínios atualizados: $T_1 = \{B, C, D\}$ (MRV=3), $T_5 = \{B, C, D\}$ (MRV=3). Empate MRV. Degree de $T_1$ (conectado a zero não atribuídas). Degree de $T_5$ (conectado a $T_6$). Escolhemos $T_5$.
* **Ação:** Atribuímos $T_5 = B$. Propagação: remove $B$ de $T_6$.


5. **Variável escolhida:** $T_1$.
* **Por que:** Domínios atualizados: $T_1 = \{B, C, D\}$ (MRV=3), $T_6 = \{A, C, D\}$ (MRV=3). Degree é empate (zero). Desempate lexicográfico para $T_1$.
* **Ação:** Como R3 exige que $T_1$ ou $T_2$ seja B, e $T_2=A$, $T_1$ DEVE ser $B$. Atribuímos $T_1 = B$.


6. **Variável escolhida:** $T_6$.
* **Por que:** Última variável restante. MRV=3.
* **Ação:** Atribuímos $T_6 = A$.



**Análise do impacto dos critérios:**

* **MRV (Minimum Remaining Values):** Reduziu drasticamente o espaço de busca e o risco de retrocesso ao forçar a resolução antecipada de $T_3$, o ponto de falha mais provável devido à restrição unária que já limitava suas opções no estado inicial.
* **Degree Heuristic:** Atuou perfeitamente como tie-breaker para o MRV. Ao priorizar as variáveis conectadas à maior parte da rede ainda não resolvida ($T_2$ e $T_4$), ela garantiu que as propagação de restrições reduzissem os domínios das variáveis restantes (como $T_1$ e $T_5$) o mais cedo possível no topo da árvore de busca.


---

### 4.3 Análise Manual de Forward Checking e Backjumping

#### 4.3.1 BACKTRACKING SIMPLES

* **Solução:** {'T1': 'A', 'T2': 'B', 'T3': 'C', 'T4': 'A', 'T5': 'B', 'T6': 'A'}
* **Estados explorados:** 10
* **Retrocessos:** 0
* **Tempo:** 0.6154 ms

#### 4.3.2 BACKTRACKING + MRV

* **Solução:** {'T3': 'B', 'T2': 'A', 'T1': 'B', 'T4': 'A', 'T5': 'B', 'T6': 'A'}
* **Estados explorados:** 9
* **Retrocessos:** 0
* **Tempo:** 0.1442 ms

#### 4.3.3 BACKTRACKING + DEGREE

* **Solução:** {'T2': 'A', 'T4': 'A', 'T5': 'B', 'T1': 'B', 'T3': 'B', 'T6': 'A'}
* **Estados explorados:** 9
* **Retrocessos:** 0
* **Tempo:** 0.1023 ms

#### 4.3.4 FORWARD CHECKING

* **Solução:** {'T1': 'A', 'T2': 'B', 'T3': 'C', 'T4': 'A', 'T5': 'B', 'T6': 'A'}
* **Estados explorados:** 6
* **Retrocessos:** 0
* **Tempo:** 0.0820 ms

#### 4.3.5 BACKJUMPING

* **Solução:** {'T1': 'A', 'T2': 'B', 'T3': 'C', 'T4': 'A', 'T5': 'B', 'T6': 'A'}
* **Estados explorados:** 10
* **Retrocessos:** 0
* **Tempo:** 0.0539 ms

| Algoritmo | Estados explorados | Retrocessos | Tempo (ms) |
| --- | --- | --- | --- |
| 1. BACKTRACKING SIMPLES | 10 | 0 | 0.6154 |
| 2. BACKTRACKING + MRV | 9 | 0 | 0.1442 |
| 3. BACKTRACKING + DEGREE | 9 | 0 | 0.1023 |
| 4. FORWARD CHECKING | 6 | 0 | 0.0820 |
| 5. BACKJUMPING | 10 | 0 | 0.0539 |

---

### 4.4 Execução dos Algoritmos

### FORWARD CHECKING

| Passo | Atribuição | T1 | T2 | T3 | T4 | T5 | T6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | (inicial) | {A,B,C,D} | {A,B,C,D} | {B,C,D} | {A,B,C,D} | {A,B,C,D} | {A,B,C,D} |
| 1 | T1=A | {A} | {B,C,D} | {B,C,D} | {A,B,C,D} | {A,B,C,D} | {A,B,C,D} |
| 2 | T2=B | {A} | {B} | {C,D} | {A,B,C,D} | {A,B,C,D} | {A,B,C,D} |
| 3 | T3=C | {A} | {B} | {C} | {A,B,D} | {A,B,C,D} | {A,B,C,D} |

**Análise de Domínio Vazio e Inconsistências:**
Neste problema específico, **nenhum domínio ficará vazio** nas etapas iniciais mostradas. O domínio (tamanho 4) é muito grande em relação ao grau de restrições futuras (no máximo 1 valor removido por R1 a cada passo).
As inconsistências detectadas e podadas antecipadamente foram:

* $T_2 = A$ (evitada pela propagação de R1 após $T_1=A$).
* $T_3 = A$ (evitada no passo 0 pela restrição unária R2).
* $T_3 = B$ (evitada pela propagação de R1 após $T_2=B$).

**Comparação com Backtracking simples:**
Neste trecho até $T_3$, o Forward Checking detectou os conflitos e economizou **3 tentativas de atribuição (passos)**. O Backtracking tradicional teria fisicamente atribuído e falhado em $T_2=A$, $T_3=A$ e $T_3=B$ antes de chegar em $T_3=C$.

---

### BACKJUMPING

**Nota Técnica:** Como a restrição R1 ($T_i \neq T_{i+1}$) afeta variáveis adjacentes, o vizinho imediatamente anterior ($T_{i-1}$) sempre entra no conflict set se um valor for bloqueado por ele. Logo, o salto inicial é sempre de distância 1. Salto múltiplo (> 1 variável) ocorre por **cascata (absorção de conflict sets)** quando uma variável esgota seus valores ao receber um recuo.

**a) Sequência de atribuições que levou ao conflito:**
$T_1=D$, $T_2=B$, $T_3=D$, $T_4=C$.
*(O limite de 'D's da restrição global R5 já foi atingido por $T_1$ e $T_3$)*.

**b) Conflict set da variável em falha:**
Suponha que $T_5$ tente seus valores e esgote o domínio.

* A tentativa 'C' falha por R1 (conflito: $T_4$).
* A tentativa 'D' falha por R5 (conflito: $\{T_1, T_3\}$).
* Assumindo hipoteticamente que 'A' e 'B' falhem por outras amarrações do estado.
O conflict set acumulado de $T_5$ resulta em: **$\{T_1, T_3, T_4\}$**.

**c) Para qual variável o algoritmo salta (e por quê):**

1. O primeiro salto de $T_5$ vai para o elemento mais recente de seu conflict set: **$T_4$**.
2. Ao saltar para $T_4$, o conflict set de $T_5$ é absorvido por $T_4$. Agora, o conflict set de $T_4$ contém $\{T_1, T_3\}$.
3. Se $T_4$ também esgotar seus valores restantes devido a esse retrocesso, ele buscará o maior índice em seu novo conflict set atualizado e **saltará diretamente para $T_3$**, pois é a raiz real do conflito (o excesso de 'D's).

**d) Quantas variáveis intermediárias foram ignoradas:**
No salto secundário (de $T_4$ para $T_3$ engatilhado pela falha de $T_5$), **1 variável intermediária foi ignorada** (a exploração de novos caminhos estéreis e valores alternativos em $T_4$).

**e) Como isso difere do backtracking tradicional:**
O backtracking tradicional não possui memória de conflitos. Se falhasse em $T_5$, ele voltaria para $T_4$ e passaria horas testando exaustivamente outras opções viáveis em $T_4$ (como 'A' ou 'B'), descendo a árvore apenas para falhar em $T_5$ novamente, pois a verdadeira causa do erro (o limite de médicos D) ocorreu lá atrás em $T_1$ e $T_3$. O Backjumping identifica as verdadeiras variáveis culpadas e salta o espaço de busca inútil.


---

### 4.5 Comparação Final dos Algoritmos


| **Critério** | **1. BT Simples** | **2. BT + MRV** | **3. BT + Degree** | **4. Forward Checking** | **5. Backjumping** |
| --- | --- | --- | --- | --- | --- |
| **a) Estados explorados** | 10 | 9 | 9 | 6 | 10 |
| **b) Retrocessos** | 0 | 0 | 0 | 0 | 0 |
| **c) Velocidade (ms)** | 0.6154 | 0.1442 | 0.1023 | 0.0820 | 0.0539 |
| **d) Consumo de memória** | Baixo | Baixo | Baixo | Alto | Médio |
| **e) Facilidade de implementação** | Alto | Médio | Médio | Médio | Baixo |
| **f) Eficiência prática** | Baixo | Médio | Médio | Alto | Alto |

**a) Número de estados explorados:**
O Forward Checking explorou o menor número de estados (apenas 6), conseguindo podar inconsistências antes mesmo de tentar atribuí-las. BT Simples e Backjumping realizaram a busca completa sem predição, atingindo o máximo de exploração (10 estados).

**b) Número de retrocessos:**
Todos os algoritmos registraram 0 retrocessos neste cenário específico. Isso indica que a densidade de soluções do problema era alta o suficiente para que o primeiro caminho aprofundado levasse diretamente a uma resposta válida, sem necessidade de recuar.

**c) Velocidade de execução:**
O Backjumping foi o mais rápido absoluto com 0.0539 ms, seguido de perto pelo Forward Checking (0.0820 ms). O BT Simples apresentou a pior performance temporal (0.6154 ms), sendo mais de 11 vezes mais lento que o Backjumping.

**d) Consumo de memória:**
O Forward Checking possui Alto consumo porque exige a clonagem e manutenção do domínio de todas as variáveis não atribuídas a cada passo da recursão. O Backjumping exige consumo Médio para manter os *conflict sets*, enquanto as heurísticas puras e o BT Simples usam memória Baixa por avaliarem apenas o estado atual.

**e) Facilidade de implementação:**
O BT Simples tem Alta facilidade, exigindo apenas um loop recursivo com checagem direta. O Backjumping apresenta Baixa facilidade devido à alta complexidade lógica para rastrear, atualizar e propagar corretamente os conjuntos de conflito durante a recursão profunda.

**f) Eficiência prática:**
Backjumping e Forward Checking demonstraram Alta eficiência ao resolver o problema em tempos sub-milissegundos (< 0.09 ms). O BT Simples obteve Baixa eficiência, pois sua ausência de inteligência na escolha e na poda gerou o maior gasto de tempo e de estados no problema.

**Ranking de eficiência: Backjumping > Forward Checking > BT + Degree > BT + MRV > BT Simples.**
Embora o Forward Checking tenha sido o algoritmo mais cirúrgico ao visitar apenas 6 estados, o Backjumping obteve o menor tempo real de execução no hardware (0.0539 ms). As heurísticas MRV e Degree apresentaram melhorias sólidas em relação ao método puramente cego, mas o BT Simples amargou o último lugar por apresentar a pior marca temporal geral (0.6154 ms).

---
---

## Questão 05 - Minimax e Poda Alpha-Beta

### 5.1 Conceitos Teóricos

**a) Objetivo do algoritmo Minimax:**
Determinar a jogada ótima para um jogador em jogos de soma zero com informação perfeita. Ele explora a árvore de busca completa antecipando todos os movimentos possíveis até o final do jogo.

**b) Diferença entre nós MAX e MIN:**
Os nós MAX representam o turno do jogador principal, que busca maximizar o ganho, escolhendo a jogada com o maior valor possível. Os nós MIN representam o turno do oponente, que busca minimizar o ganho do jogador MAX, escolhendo a jogada com o menor valor.

**c) Conceito de utilidade:**
É o valor numérico atribuído a um estado terminal (folha da árvore) que indica o resultado final do jogo. Valores positivos favorecem o jogador MAX (ex: +1 para vitória), valores negativos favorecem MIN (ex: -1 para derrota) e zero indica empate.

**d) Propagação de valores na árvore:**
Os valores de utilidade sobem da base da árvore (nós folha) até a raiz. Cada nó intermediário assume o valor do seu melhor sucessor de acordo com sua função (máximo para nós MAX, mínimo para nós MIN), definindo o valor esperado daquele estado.

**e) Hipótese de adversário perfeito:**
O algoritmo assume que o oponente sempre fará a jogada que mais prejudica o jogador MAX, sem cometer erros. Se o oponente jogar de forma subótima, o desempenho do jogador MAX será igual ou melhor do que o esperado.

**f) Objetivo da poda Alpha-Beta:**
Reduzir o número de nós avaliados pelo algoritmo Minimax, cortando ramos da árvore de busca que não podem influenciar a decisão final. Isso diminui o tempo de processamento sem alterar a escolha da jogada ótima.

---

### 5.2 Execução Manual: Minimax e Alpha-Beta

### MINIMAX COMPLETO

| Nó | Tipo | Filhos e valores | Valor Minimax |
| --- | --- | --- | --- |
| D | MAX | 3, 5 | 5 |
| E | MAX | 6, 9 | 9 |
| B | MIN | D=5, E=9 | 5 |
| F | MAX | 1, 2 | 2 |
| G | MAX | 0, -1 | 0 |
| C | MIN | F=2, G=0 | 0 |
| I | MAX | 7, 4 | 7 |
| J | MAX | 5, 6 | 6 |
| H | MIN | I=7, J=6 | 6 |
| A | MAX | B=5, C=0, H=6 | 6 |

**Decisão final de A:**
A escolhe o filho **H**. Sendo um nó MAX, A escolhe a opção que maximiza o seu ganho final, sendo 6 o maior valor retornado entre as três ramificações possíveis (B=5, C=0, H=6).

**Resumo da Busca:**

* Caminho escolhido: **A → H** (com resposta ótima em J → 6)
* Valor final obtido: **6**

---

### PODA ALPHA-BETA

| Passo | Nó | α | β | Poda? | Motivo |
| --- | --- | --- | --- | --- | --- |
| 1 | A | -∞ | +∞ | não | Inicialização na raiz |
| 2 | B | -∞ | +∞ | não | Herda os valores de A |
| 3 | D | -∞ | +∞ | não | Herda os valores de B |
| 4 | B | -∞ | 5 | não | Recebe 5 de D (MIN atualiza β = 5) |
| 5 | E | -∞ | 5 | sim | E avalia a primeira folha 6 (MAX atualiza α = 6). Como α=6 >= β=5, poda o ramo restante |
| 6 | A | 5 | +∞ | não | Recebe 5 de B (MAX atualiza α = 5) |
| 7 | C | 5 | +∞ | não | Herda os valores de A |
| 8 | F | 5 | +∞ | não | Herda os valores de C |
| 9 | C | 5 | 2 | sim | Recebe 2 de F (MIN atualiza β = 2). Como β=2 <= α=5, poda o ramo restante |
| 10 | H | 5 | +∞ | não | Herda os valores atualizados de A |
| 11 | I | 5 | +∞ | não | Herda os valores de H |
| 12 | H | 5 | 7 | não | Recebe 7 de I (MIN atualiza β = 7) |
| 13 | J | 5 | 7 | não | Herda os valores de H |
| 14 | H | 5 | 6 | não | Recebe 6 de J (MIN atualiza β de 7 para 6) |
| 15 | A | 6 | +∞ | não | Recebe 6 de H (MAX atualiza α de 5 para 6) |

**Estatísticas Finais da Poda:**

* **Total de podas ocorridas:** 2
* **Nós/folhas NÃO explorados:** Folha 9 (filha de E), Nó G (filho de C) e suas respectivas folhas (0 e -1).
* **Quantidade de nós não explorados:** 4 (1 nó interno + 3 folhas).

---

### 5.3 Reordenação e Minimax com Profundidade Limitada

**a) Nova ordem escolhida e justificativa**
A ordem ideal no Alpha-Beta é explorar primeiro os lances mais promissores (maiores valores para MAX, menores para MIN).

* Para o nó A (MAX), o melhor filho é H (valor 6), seguido de B (5) e C (0). Nova ordem de A: **H, B, C**.
* Para o nó H (MIN), o melhor filho é J (valor 6) frente a I (7). Nova ordem de H: **J, I**.
* Para o nó B (MIN), o melhor filho é D (valor 5) frente a E (9). Nova ordem de B: **D, E**.
* Para o nó C (MIN), o melhor filho é G (valor 0) frente a F (2). Nova ordem de C: **G, F**.

**b) Tabela Alpha-Beta com a nova ordem:**

| Passo | Nó | α | β | Poda? | Motivo |
| --- | --- | --- | --- | --- | --- |
| 1 | A | -∞ | +∞ | não | Inicialização |
| 2 | H | -∞ | +∞ | não | Herda de A |
| 3 | J | -∞ | +∞ | não | Herda de H |
| 4 | H | -∞ | 6 | não | J avalia 5 e 6, retorna 6. MIN atualiza β=6 |
| 5 | I | -∞ | 6 | sim | I avalia a primeira folha (7). MAX atualiza α=7. Como α=7 >= β=6, poda a folha 4 |
| 6 | A | 6 | +∞ | não | H retorna 6. MAX atualiza α=6 |
| 7 | B | 6 | +∞ | não | Herda de A |
| 8 | D | 6 | +∞ | não | Herda de B |
| 9 | B | 6 | 5 | sim | D avalia 3 e 5, retorna 5. MIN atualiza β=5. Como β=5 <= α=6, poda o nó inteiro E |
| 10 | C | 6 | +∞ | não | Herda de A |
| 11 | G | 6 | +∞ | não | Herda de C |
| 12 | C | 6 | 0 | sim | G avalia 0 e -1, retorna 0. MIN atualiza β=0. Como β=0 <= α=6, poda o nó inteiro F |

**c) Total de podas com a ordem original:** 2
**d) Total de podas com a nova ordem:** 3 (com volume de poda muito maior, cortando ramos inteiros precocemente).

**e) Por que a nova ordem melhora a eficiência:**
Ao descobrir rapidamente o melhor lance global (o valor 6 de H), o nó MAX (A) eleva seu "piso" de garantia (α) logo no início. Quando os demais nós (B e C) começam a ser explorados, qualquer evidência inicial de que o oponente (MIN) conseguirá forçar um valor inferior a 6 (como o 5 retornado por D ou o 0 retornado por G) é suficiente para abortar a busca naquele ramo instantaneamente, economizando o cálculo de todos os irmãos restantes.

**f) Relação geral entre ordenação e desempenho:**
O Alpha-Beta com ordenação aleatória poda pouco e tem complexidade $O(b^d)$. Com a ordenação perfeita (melhores lances primeiro), o algoritmo atinge sua máxima eficiência temporal, caindo para $O(b^{d/2})$, permitindo buscar no dobro da profundidade com o mesmo tempo de processamento.

---

### MINIMAX COM PROFUNDIDADE LIMITADA (limite = 2)

**a) Tabela com valores heurísticos usados e propagados**

* **Profundidade 2 (Folhas da busca):** Valores fornecidos pela função heurística $h(n)$.
* $h(D) = 4$
* $h(E) = 7$
* $h(F) = 2$
* $h(G) = 5$
* $h(I) = 6$
* $h(J) = 1$



| Nó | Tipo (Profundidade) | Filhos e valores (Heurística) | Valor Minimax |
| --- | --- | --- | --- |
| B | MIN (1) | D=4, E=7 | 4 |
| C | MIN (1) | F=2, G=5 | 2 |
| H | MIN (1) | I=6, J=1 | 1 |
| A | MAX (0) | B=4, C=2, H=1 | 4 |

**b) Decisão tomada por A com Minimax limitado:**
A escolhe o filho **B**.

**c) Comparação com a decisão do Minimax completo:**

* **A decisão mudou?** Sim. Mudou de H para B.
* **O valor obtido é maior, menor ou igual?** O valor real obtido jogando B seria 5 (visto na Parte 1), o que é menor que o valor ótimo 6 (que seria obtido jogando H). O valor estimado (4) também é diferente e pior que o real ótimo.

**d) Discussão: erros da heurística**
O erro principal, conhecido como Efeito de Horizonte, ocorre quando a função heurística não consegue prever uma mudança drástica de vantagem (como uma captura de peça) que acontece logo após o limite da profundidade de busca. Neste exemplo, a heurística estimou mal o nó H (dando peso 1 a J, quando na realidade J levaria aos valores reais 5 e 6). Ao estagnar a busca artificialmente, o algoritmo confia cegamente em estimativas estáticas imprecisas, descartando caminhos que a longo prazo seriam vitoriosos e preferindo caminhos que parecem bons a curto prazo, mas são subótimos.

---

### 5.4 Execução dos Algoritmos

#### 5.4.1 Árvore Original

#### 5.4.1.1 MINIMAX COMPLETO

* **Valor na raiz:** 6
* **Caminho ótimo:** A -> H -> J -> J2
* **Nós explorados:** 22
* **Decisão de A:** filho H

#### 5.4.1.2 ALPHA-BETA

* **Valor na raiz:** 6
* **Caminho ótimo:** A -> H -> J -> J2
* **Nós explorados:** 18
* **Podas:** 2
* No nó E, filhos ['E2'] podados (motivo: valor 6 >= beta 5)
* No nó C, filhos ['G'] podados (motivo: valor 2 <= alpha 5)


* **Decisão de A:** filho H

#### 5.4.1.3 MINIMAX DEPTH-LIMITED (L=2)

* **Valor na raiz:** 4
* **Caminho ótimo:** A -> B -> D
* **Nós explorados:** 10
* **Decisão de A:** filho B

#### 5.4.2 Árvore com Folhas Modificadas

#### 5.4.2.1 MINIMAX COMPLETO

* **Valor na raiz:** 8
* **Caminho ótimo:** A -> B -> D -> D2
* **Nós explorados:** 22
* **Decisão de A:** filho B

#### 5.4.2.2 ALPHA-BETA

* **Valor na raiz:** 8
* **Caminho ótimo:** A -> B -> D -> D2
* **Nós explorados:** 16
* **Podas:** 2
* No nó C, filhos ['G'] podados (motivo: valor 2 <= alpha 8)
* No nó H, filhos ['J'] podados (motivo: valor 4 <= alpha 8)


* **Decisão de A:** filho B

#### 5.4.2.3 MINIMAX DEPTH-LIMITED (L=2)

* **Valor na raiz:** 4
* **Caminho ótimo:** A -> B -> D
* **Nós explorados:** 10
* **Decisão de A:** filho B

| Algoritmo | Árvore | Valor raiz | Nós explorados | Podas | Decisão A |
| --- | --- | --- | --- | --- | --- |
| Minimax Comp. | ÁRVORE ORIGINAL | 6 | 22 | - | H |
| Alpha-Beta | ÁRVORE ORIGINAL | 6 | 18 | 2 | H |
| Depth-Lim(2) | ÁRVORE ORIGINAL | 4 | 10 | - | B |
| Minimax Comp. | ÁRVORE MODIFICADA | 8 | 22 | - | B |
| Alpha-Beta | ÁRVORE MODIFICADA | 8 | 16 | 2 | B |
| Depth-Lim(2) | ÁRVORE MODIFICADA | 4 | 10 | - | B |

---

### 5.5 Análise do Experimento e Comparação Final


**a) A decisão final de A mudou com as folhas modificadas:**  
Sim.  
- Minimax Completo: de H para B.  
- Alpha-Beta: de H para B.  
- Depth-Limited já escolhia B e permaneceu igual.

**b) O valor calculado na raiz mudou? Em quanto:**  
Sim.  
- Minimax Completo: de 6 para 8 (+2).  
- Alpha-Beta: de 6 para 8 (+2).  
- Depth-Limited permaneceu em 4.

**c) O Alpha-Beta manteve a mesma decisão que o Minimax:**  
Sim. Em ambas as árvores, Alpha-Beta tomou exatamente a mesma decisão do Minimax Completo.  
- Árvore original: ambos escolheram H.  
- Árvore modificada: ambos escolheram B.

**d) Análise da sensibilidade:**  
As folhas mais impactantes foram as ligadas ao ramo B -> D -> D2, pois a alteração elevou o valor da raiz de 6 para 8 e mudou a decisão final de H para B.  
Folhas mais profundas e em ramos podados tiveram menor impacto, porque algumas nem chegaram a ser exploradas pelo Alpha-Beta.

---

# COMPARAÇÃO MINIMAX vs ALPHA-BETA

| Critério | Minimax | Alpha-Beta |
|---|---|---|
| **a) Número de nós explorados** | 22 nós na árvore original e modificada | 18 nós na original e 16 na modificada |
| **b) Quantidade de podas** | Não realiza podas | 2 podas em ambas as árvores |
| **c) Custo computacional** | Alto | Médio |
| **d) Consumo de memória** | Alto | Médio |
| **e) Impacto da ordenação dos movimentos** | Baixo | Alto |
| **f) Qualidade das decisões** | Ótima | Ótima |

### Justificativas

**a) Número de nós explorados:**  
O Alpha-Beta explorou menos nós em ambos os casos.  
- Original: 18 contra 22.  
- Modificada: 16 contra 22.

**b) Quantidade de podas:**  
O Minimax avalia toda a árvore e não faz podas.  
O Alpha-Beta realizou 2 podas nas duas execuções.

**c) Custo computacional:**  
O Minimax possui maior custo por visitar todos os nós.  
O Alpha-Beta reduz processamento ao eliminar ramos desnecessários.

**d) Consumo de memória:**  
O Minimax mantém mais estados ativos devido à exploração completa.  
O Alpha-Beta reduz armazenamento ao interromper partes da busca.

**e) Impacto da ordenação dos movimentos:**  
No Minimax, a ordem dos filhos não altera o número de nós visitados.  
No Alpha-Beta, uma boa ordenação aumenta as podas e reduz explorações.

**f) Qualidade das decisões:**  
Os dois algoritmos encontraram exatamente a mesma decisão final nas duas árvores.  
Alpha-Beta preservou a optimalidade do Minimax.

### Cenário em que Alpha-Beta perde vantagem

O Alpha-Beta perde vantagem quando a ordenação dos movimentos é ruim e poucas podas acontecem.  
Nesse caso, ele pode acabar explorando quase a mesma quantidade de nós que o Minimax.

---
---

## Questão 06 - Monte Carlo Tree Search (MCTS)

### 6.1 Conceitos Teóricos

**a) Seleção:**
O algoritmo desce pela árvore de jogo partindo da raiz, escolhendo a cada passo o nó filho que apresenta o maior valor segundo uma fórmula de balanceamento (como a UCT). Este processo continua recursivamente até alcançar um nó folha que ainda não foi totalmente expandido.

**b) Expansão:**
Ao chegar a um nó folha não terminal, caso esse nó tenha sido visitado pelo menos uma vez, ele é expandido com a adição de um (ou mais) de seus filhos à árvore. No Connect-4, isso significaria criar um novo nó representando a jogada em uma coluna válida (ex: jogar na $c_1$).

**c) Simulação (rollout):**
A partir do nó recém-expandido, o MCTS realiza jogadas aleatórias (ou baseadas em heurísticas simples) para ambos os jogadores até que o jogo atinja um estado terminal (vitória, derrota ou empate). Essa simulação rápida serve para estimar o valor real daquele estado sem precisar construir a árvore inteira.

**d) Retropropagação:**
O resultado final obtido na simulação (ex: +1 para vitória, -1 para derrota) é propagado de volta, subindo do nó expandido até a raiz da árvore. Durante a subida, as estatísticas de todos os nós ancestrais que fazem parte desse caminho são atualizadas com o novo resultado.

**e) Papel do número de visitas N(s):**
Representa a quantidade de vezes que o estado $s$ (ou nó) foi selecionado para participar de uma simulação. O aumento de $N(s)$ indica que o algoritmo está acumulando mais informações sobre aquele nó, aumentando a confiabilidade estatística de sua avaliação.

**f) Papel do número de vitórias W(s):**
É o saldo acumulado das recompensas retropropagadas por todas as simulações que passaram pelo estado $s$. A divisão $W(s) / N(s)$ define a taxa de vitória empírica (ou utilidade esperada) daquele nó, servindo de base para o MCTS avaliar se a jogada é promissora (explotação).

**g) Diferença entre exploração e explotação:**
A explotação prefere nós com alta taxa de vitória ($W/N$), focando nas jogadas que já provaram ser boas. A exploração prefere nós com poucas visitas ($N(s)$ baixo), incentivando a descoberta de caminhos desconhecidos para evitar a estagnação em máximos locais. Na fórmula UCT, o parâmetro constante $C$ (peso de exploração) controla esse balanço: valores altos de $C$ forçam o algoritmo a explorar ramos ignorados, enquanto valores próximos a zero forçam a focar quase exclusivamente no ramo de maior taxa de vitória atual.

---

### 6.2 Execução Manual: 10 Iterações com C = 1.4


**Iteração 1:**

* Seleção: raiz
* Nó expandido: c1
* Resultado do rollout: V (valor: 1)
* Atualizações: nó raiz→c1 (N=1, W=1), raiz (N=1, W=1)
* Árvore após iteração:
| Ação | N | W | UCT (se N>0) |
| --- | --- | --- | --- |
| c1 | 1 | 1 | 1.000 |
| c2 | 0 | 0 | ∞ |
| c3 | 0 | 0 | ∞ |
| c4 | 0 | 0 | ∞ |



**Iteração 2:**

* Seleção: raiz
* Nó expandido: c2
* Resultado do rollout: A (valor: 0)
* Atualizações: nó raiz→c2 (N=1, W=0), raiz (N=2, W=1)
* Árvore após iteração:
| Ação | N | W | UCT (se N>0) |
| --- | --- | --- | --- |
| c1 | 1 | 1 | 2.166 |
| c2 | 1 | 0 | 1.166 |
| c3 | 0 | 0 | ∞ |
| c4 | 0 | 0 | ∞ |



**Iteração 3:**

* Seleção: raiz
* Nó expandido: c3
* Resultado do rollout: V (valor: 1)
* Atualizações: nó raiz→c3 (N=1, W=1), raiz (N=3, W=2)
* Árvore após iteração:
| Ação | N | W | UCT (se N>0) |
| --- | --- | --- | --- |
| c1 | 1 | 1 | 2.467 |
| c2 | 1 | 0 | 1.467 |
| c3 | 1 | 1 | 2.467 |
| c4 | 0 | 0 | ∞ |



**Iteração 4:**

* Seleção: raiz
* Nó expandido: c4
* Resultado do rollout: A (valor: 0)
* Atualizações: nó raiz→c4 (N=1, W=0), raiz (N=4, W=2)
* Árvore após iteração:
| Ação | N | W | UCT (se N>0) |
| --- | --- | --- | --- |
| c1 | 1 | 1 | 2.648 |
| c2 | 1 | 0 | 1.648 |
| c3 | 1 | 1 | 2.648 |
| c4 | 1 | 0 | 1.648 |



**Iteração 5:**

* Seleção: raiz → c1 (desempate pelo menor índice entre c1 e c3)
* Nó expandido: c1 (primeiro filho não visitado de c1)
* Resultado do rollout: V (valor: 1)
* Atualizações: nó raiz→c1→c1 (N=1, W=1), nó raiz→c1 (N=2, W=2), raiz (N=5, W=3)
* Árvore após iteração:
| Ação | N | W | UCT (se N>0) |
| --- | --- | --- | --- |
| c1 | 2 | 2 | 2.256 |
| c2 | 1 | 0 | 1.776 |
| c3 | 1 | 1 | 2.776 |
| c4 | 1 | 0 | 1.776 |



**Iteração 6:**

* Seleção: raiz → c3
* Nó expandido: c1 (primeiro filho não visitado de c3)
* Resultado do rollout: A (valor: 0)
* Atualizações: nó raiz→c3→c1 (N=1, W=0), nó raiz→c3 (N=2, W=1), raiz (N=6, W=3)
* Árvore após iteração:
| Ação | N | W | UCT (se N>0) |
| --- | --- | --- | --- |
| c1 | 2 | 2 | 2.325 |
| c2 | 1 | 0 | 1.874 |
| c3 | 2 | 1 | 1.825 |
| c4 | 1 | 0 | 1.874 |



**Iteração 7:**

* Seleção: raiz → c1
* Nó expandido: c2 (próximo filho não visitado de c1)
* Resultado do rollout: V (valor: 1)
* Atualizações: nó raiz→c1→c2 (N=1, W=1), nó raiz→c1 (N=3, W=3), raiz (N=7, W=4)
* Árvore após iteração:
| Ação | N | W | UCT (se N>0) |
| --- | --- | --- | --- |
| c1 | 3 | 3 | 2.128 |
| c2 | 1 | 0 | 1.953 |
| c3 | 2 | 1 | 1.881 |
| c4 | 1 | 0 | 1.953 |



**Iteração 8:**

* Seleção: raiz → c1
* Nó expandido: c3 (próximo filho não visitado de c1)
* Resultado do rollout: A (valor: 0)
* Atualizações: nó raiz→c1→c3 (N=1, W=0), nó raiz→c1 (N=4, W=3), raiz (N=8, W=4)
* Árvore após iteração:
| Ação | N | W | UCT (se N>0) |
| --- | --- | --- | --- |
| c1 | 4 | 3 | 1.759 |
| c2 | 1 | 0 | 2.019 |
| c3 | 2 | 1 | 1.928 |
| c4 | 1 | 0 | 2.019 |



**Iteração 9:**

* Seleção: raiz → c2 (desempate pelo menor índice entre c2 e c4)
* Nó expandido: c1 (primeiro filho não visitado de c2)
* Resultado do rollout: A (valor: 0)
* Atualizações: nó raiz→c2→c1 (N=1, W=0), nó raiz→c2 (N=2, W=0), raiz (N=9, W=4)
* Árvore após iteração:
| Ação | N | W | UCT (se N>0) |
| --- | --- | --- | --- |
| c1 | 4 | 3 | 1.788 |
| c2 | 2 | 0 | 1.467 |
| c3 | 2 | 1 | 1.967 |
| c4 | 1 | 0 | 2.075 |



**Iteração 10:**

* Seleção: raiz → c4
* Nó expandido: c1 (primeiro filho não visitado de c4)
* Resultado do rollout: V (valor: 1)
* Atualizações: nó raiz→c4→c1 (N=1, W=1), nó raiz→c4 (N=2, W=1), raiz (N=10, W=5)
* Árvore após iteração:
| Ação | N | W | UCT (se N>0) |
| --- | --- | --- | --- |
| c1 | 4 | 3 | 1.812 |
| c2 | 2 | 0 | 1.502 |
| c3 | 2 | 1 | 2.002 |
| c4 | 2 | 1 | 2.002 |



---

### Tabela Final

| Ação | N | W | UCT Final |
| --- | --- | --- | --- |
| c1 | 4 | 3 | 1.812 |
| c2 | 2 | 0 | 1.502 |
| c3 | 2 | 1 | 2.002 |
| c4 | 2 | 1 | 2.002 |

* **Jogada recomendada:** c1.
* **Justificativa:** No MCTS, a jogada escolhida ao final do tempo/iterações limite é a raiz que possui a contagem de visitas ($N$) mais alta, pois representa o caminho mais robusto, exaustivamente testado e que se manteve promissor o suficiente para ser selecionado repetidas vezes pelo balanceamento da fórmula UCT.

---

### 6.3 Análise do Parâmetro C (0.1, 1.4 e 3.0)


**Para C = 0.1 (baixa exploração):**
a) O termo de exploração torna-se quase insignificante perto do termo de explotação (a taxa de vitória $W/N$), fazendo com que o algoritmo confie cegamente nos resultados das primeiras simulações.
b) As ações que obtiveram vitórias acidentais ou precoces nas primeiras iterações (neste caso, a ação c1) dominariam completamente as visitas, pois qualquer falha nos nós irmãos (como os zeros em c2) os faria ser punidos e ignorados pelo resto da busca.
c) A distribuição de visitas seria muito **menos** uniforme do que com C=1.4, concentrando quase todas as visitas em 1 ou 2 filhos.
d) O risco de não encontrar a jogada ótima é altíssimo (convergência prematura), pois o algoritmo estagna em um máximo local e não permite que outros ramos provem seu valor real com uma amostragem decente.

**Para C = 3.0 (alta exploração):**
a) O termo de exploração domina o termo de explotação, forçando o algoritmo a escolher repetidamente os ramos que foram menos visitados, ignorando temporariamente quem tem a maior taxa de vitórias.
b) Todas as ações tenderiam a ser visitadas um número de vezes muito parecido, pois assim que uma ação ganha uma ou duas visitas extras, seu termo $N(j)$ no denominador penaliza fortemente seu UCT, forçando a seleção das outras.
c) A distribuição de visitas seria muito **mais** uniforme do que com C=1.4, aproximando-se de uma busca em largura (Breadth-First Search).
d) O risco de desperdiçar simulações em ações ruins é extremo, pois o algoritmo passará muito tempo testando ramos comprovadamente desastrosos apenas para satisfazer a curiosidade estatística, reduzindo a profundidade alcançada no ramo ótimo.

---

### CÁLCULOS UCT (Estado final, N_pai = 10)

**Fórmula base:** $UCT(j) = \frac{W(j)}{N(j)} + C \cdot \sqrt{\frac{\ln(10)}{N(j)}}$
Dado: $\ln(10) \approx 2.3025$

#### Cálculos para C = 0.1

* **c1:** $N=4, W=3$
$\frac{3}{4} + 0.1 \cdot \sqrt{\frac{2.3025}{4}} = 0.75 + 0.1 \cdot \sqrt{0.5756} = 0.75 + 0.1 \cdot 0.7587 = 0.75 + 0.0759 = \mathbf{0.8259}$
* **c2:** $N=2, W=0$
$\frac{0}{2} + 0.1 \cdot \sqrt{\frac{2.3025}{2}} = 0 + 0.1 \cdot \sqrt{1.1512} = 0 + 0.1 \cdot 1.0729 = 0 + 0.1073 = \mathbf{0.1073}$
* **c3 e c4:** $N=2, W=1$
$\frac{1}{2} + 0.1 \cdot \sqrt{\frac{2.3025}{2}} = 0.5 + 0.1 \cdot 1.0729 = 0.5 + 0.1073 = \mathbf{0.6073}$

#### Cálculos para C = 3.0

* **c1:** $N=4, W=3$
$\frac{3}{4} + 3.0 \cdot \sqrt{\frac{2.3025}{4}} = 0.75 + 3.0 \cdot 0.7587 = 0.75 + 2.2761 = \mathbf{3.0261}$
* **c2:** $N=2, W=0$
$\frac{0}{2} + 3.0 \cdot \sqrt{\frac{2.3025}{2}} = 0 + 3.0 \cdot 1.0729 = \mathbf{3.2187}$
* **c3 e c4:** $N=2, W=1$
$\frac{1}{2} + 3.0 \cdot \sqrt{\frac{2.3025}{2}} = 0.5 + 3.0 \cdot 1.0729 = 0.5 + 3.2187 = \mathbf{3.7187}$

---

### TABELA COMPARATIVA

| C | Ação mais visitada esperada | Diversidade | Estabilidade | Qualidade |
| --- | --- | --- | --- | --- |
| 0.1 | c1 (viciada no primeiro sucesso) | Baixa | Baixa (Altamente dependente da sorte inicial) | Baixa (Risco de máximo local) |
| 1.4 | c1 (equilibrada) | Média | Alta (Convergência garantida no tempo) | Alta (Busca seletiva e confiável) |
| 3.0 | Múltiplas (busca uniforme) | Alta | Média (Não aprofunda onde deve) | Média (Desperdício em ações nulas) |

---

### 6.4 Execução dos Algoritmos

#### ROLLOUT: random | C: 0.1 | ITERAÇÕES: 10

* **Jogada recomendada:** c4
* **Tempo:** 2.97 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 1 | 0.5 | 0.500 | 0.652 |
| c2 | 1 | 0.5 | 0.500 | 0.652 |
| c3 | 1 | 0.5 | 0.500 | 0.652 |
| c4 | 7 | 5.5 | 0.786 | 0.843 |

#### ROLLOUT: random | C: 0.1 | ITERAÇÕES: 50

* **Jogada recomendada:** c1
* **Tempo:** 10.90 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 32 | 20.0 | 0.625 | 0.660 |
| c2 | 2 | 1.0 | 0.500 | 0.640 |
| c3 | 2 | 1.0 | 0.500 | 0.640 |
| c4 | 14 | 8.5 | 0.607 | 0.660 |

#### ROLLOUT: random | C: 0.1 | ITERAÇÕES: 200

* **Jogada recomendada:** c3
* **Tempo:** 44.11 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 1 | 0.0 | 0.000 | 0.230 |
| c2 | 12 | 6.0 | 0.500 | 0.566 |
| c3 | 123 | 70.0 | 0.569 | 0.590 |
| c4 | 64 | 35.0 | 0.547 | 0.576 |

#### ROLLOUT: random | C: 1.4 | ITERAÇÕES: 10

* **Jogada recomendada:** c3
* **Tempo:** 1.48 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 2 | 1.0 | 0.500 | 2.002 |
| c2 | 2 | 1.0 | 0.500 | 2.002 |
| c3 | 4 | 3.0 | 0.750 | 1.812 |
| c4 | 2 | 1.0 | 0.500 | 2.002 |

#### ROLLOUT: random | C: 1.4 | ITERAÇÕES: 50

* **Jogada recomendada:** c2
* **Tempo:** 9.23 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 14 | 10.0 | 0.714 | 1.454 |
| c2 | 17 | 13.0 | 0.765 | 1.436 |
| c3 | 6 | 2.0 | 0.333 | 1.464 |
| c4 | 13 | 8.5 | 0.654 | 1.422 |

#### ROLLOUT: random | C: 1.4 | ITERAÇÕES: 200

* **Jogada recomendada:** c2
* **Tempo:** 41.78 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 44 | 27.0 | 0.614 | 1.099 |
| c2 | 80 | 59.5 | 0.744 | 1.104 |
| c3 | 27 | 13.0 | 0.481 | 1.102 |
| c4 | 49 | 31.0 | 0.633 | 1.093 |

#### ROLLOUT: random | C: 3.0 | ITERAÇÕES: 10

* **Jogada recomendada:** c1
* **Tempo:** 3.70 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 3 | 1.5 | 0.500 | 3.128 |
| c2 | 3 | 3.0 | 1.000 | 3.628 |
| c3 | 2 | 1.0 | 0.500 | 3.719 |
| c4 | 2 | 1.0 | 0.500 | 3.719 |

#### ROLLOUT: random | C: 3.0 | ITERAÇÕES: 50

* **Jogada recomendada:** c1
* **Tempo:** 7.57 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 14 | 10.0 | 0.714 | 2.300 |
| c2 | 11 | 6.0 | 0.545 | 2.335 |
| c3 | 13 | 8.5 | 0.654 | 2.300 |
| c4 | 12 | 7.5 | 0.625 | 2.338 |

#### ROLLOUT: random | C: 3.0 | ITERAÇÕES: 200

* **Jogada recomendada:** c2
* **Tempo:** 44.82 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 48 | 27.5 | 0.573 | 1.570 |
| c2 | 57 | 37.0 | 0.649 | 1.564 |
| c3 | 45 | 24.0 | 0.533 | 1.563 |
| c4 | 50 | 29.5 | 0.590 | 1.567 |

#### ROLLOUT: greedy | C: 0.1 | ITERAÇÕES: 10

* **Jogada recomendada:** c2
* **Tempo:** 11.49 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 1 | 0.5 | 0.500 | 0.652 |
| c2 | 7 | 4.5 | 0.643 | 0.700 |
| c3 | 1 | 0.5 | 0.500 | 0.652 |
| c4 | 1 | 0.5 | 0.500 | 0.652 |

#### ROLLOUT: greedy | C: 0.1 | ITERAÇÕES: 50

* **Jogada recomendada:** c2
* **Tempo:** 47.11 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 14 | 9.0 | 0.643 | 0.696 |
| c2 | 18 | 10.0 | 0.556 | 0.602 |
| c3 | 15 | 8.5 | 0.567 | 0.618 |
| c4 | 3 | 1.5 | 0.500 | 0.614 |

#### ROLLOUT: greedy | C: 0.1 | ITERAÇÕES: 200

* **Jogada recomendada:** c2
* **Tempo:** 112.88 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 72 | 37.5 | 0.521 | 0.548 |
| c2 | 99 | 52.0 | 0.525 | 0.548 |
| c3 | 25 | 12.5 | 0.500 | 0.546 |
| c4 | 4 | 1.5 | 0.375 | 0.490 |

#### ROLLOUT: greedy | C: 1.4 | ITERAÇÕES: 10

* **Jogada recomendada:** c1
* **Tempo:** 7.95 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 3 | 2.0 | 0.667 | 1.893 |
| c2 | 3 | 2.5 | 0.833 | 2.060 |
| c3 | 2 | 1.0 | 0.500 | 2.002 |
| c4 | 2 | 1.5 | 0.750 | 2.252 |

#### ROLLOUT: greedy | C: 1.4 | ITERAÇÕES: 50

* **Jogada recomendada:** c2
* **Tempo:** 53.01 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 12 | 7.5 | 0.625 | 1.424 |
| c2 | 15 | 10.5 | 0.700 | 1.415 |
| c3 | 11 | 6.5 | 0.591 | 1.426 |
| c4 | 12 | 7.5 | 0.625 | 1.424 |

#### ROLLOUT: greedy | C: 1.4 | ITERAÇÕES: 200

* **Jogada recomendada:** c2
* **Tempo:** 130.42 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 56 | 34.5 | 0.616 | 1.047 |
| c2 | 65 | 42.0 | 0.646 | 1.046 |
| c3 | 39 | 20.5 | 0.526 | 1.042 |
| c4 | 40 | 21.5 | 0.537 | 1.047 |

#### ROLLOUT: greedy | C: 3.0 | ITERAÇÕES: 10

* **Jogada recomendada:** c1
* **Tempo:** 8.02 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 3 | 2.0 | 0.667 | 3.295 |
| c2 | 3 | 2.5 | 0.833 | 3.462 |
| c3 | 2 | 0.5 | 0.250 | 3.469 |
| c4 | 2 | 1.0 | 0.500 | 3.719 |

#### ROLLOUT: greedy | C: 3.0 | ITERAÇÕES: 50

* **Jogada recomendada:** c2
* **Tempo:** 52.46 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 12 | 7.0 | 0.583 | 2.296 |
| c2 | 14 | 9.5 | 0.679 | 2.264 |
| c3 | 11 | 5.0 | 0.455 | 2.244 |
| c4 | 13 | 8.0 | 0.615 | 2.261 |

#### ROLLOUT: greedy | C: 3.0 | ITERAÇÕES: 200

* **Jogada recomendada:** c2
* **Tempo:** 142.20 ms

| Ação | N | W | W/N | UCT final |
| --- | --- | --- | --- | --- |
| c1 | 53 | 32.0 | 0.604 | 1.552 |
| c2 | 63 | 43.0 | 0.683 | 1.553 |
| c3 | 42 | 20.5 | 0.488 | 1.554 |
| c4 | 42 | 20.5 | 0.488 | 1.554 |

| Rollout | C | Iterações | Jogada | Tempo (ms) |
| --- | --- | --- | --- | --- |
| random | 0.1 | 10 | c4 | 2.97 |
| random | 0.1 | 50 | c1 | 10.90 |
| random | 0.1 | 200 | c3 | 44.11 |
| random | 1.4 | 10 | c3 | 1.48 |
| random | 1.4 | 50 | c2 | 9.23 |
| random | 1.4 | 200 | c2 | 41.78 |
| random | 3.0 | 10 | c1 | 3.70 |
| random | 3.0 | 50 | c1 | 7.57 |
| random | 3.0 | 200 | c2 | 44.82 |
| greedy | 0.1 | 10 | c2 | 11.49 |
| greedy | 0.1 | 50 | c2 | 47.11 |
| greedy | 0.1 | 200 | c2 | 112.88 |
| greedy | 1.4 | 10 | c1 | 7.95 |
| greedy | 1.4 | 50 | c2 | 53.01 |
| greedy | 1.4 | 200 | c2 | 130.42 |
| greedy | 3.0 | 10 | c1 | 8.02 |
| greedy | 3.0 | 50 | c2 | 52.46 |
| greedy | 3.0 | 200 | c2 | 142.20 |

---

### 6.5 Comparação Final


**a) Qualidade das decisões:** A jogada recomendada difere drasticamente em baixas iterações. O rollout semi-guloso encontra a jogada ótima (`c2`) muito mais cedo e a mantém, enquanto o aleatório é errático nas primeiras fases (sugerindo `c4`, `c1` e `c3`) e só converge para a resposta correta (`c2`) a partir de 200 iterações (com C=1.4 e C=3.0).

**b) Velocidade de convergência:** O rollout semi-guloso estabiliza a jogada recomendada (`c2`) já com 50 iterações (para C=1.4 e C=3.0) e até mesmo com 10 iterações (para C=0.1). O rollout aleatório requer o teto máximo de 200 iterações para finalmente estabilizar em `c2`.

**c) Número de simulações necessárias:** O semi-guloso precisa de apenas cerca de 50 simulações para obter um W/N confiável que indique a vitória clara, custando cerca de 53 ms por ser mais pesado computacionalmente. O aleatório compensa sua "burrice" tática com volume bruto, exigindo 200 simulações para superar o ruído (custando ~41 a 44 ms), provando que inteligência embutida no rollout poupa exploração na árvore.

### IMPACTO DO VALOR DE C

**a) Distribuição de visitas:** Com C=0.1, a distribuição é extremamente concentrada e viciada (ex: Aleatório/200 tem 123 visitas em `c3` e apenas 1 em `c1`). Com C=3.0, a distribuição é forçadamente uniforme e dispersa (ex: Aleatório/200 distribui as visitas quase igualmente: 48, 57, 45, 50). O valor C=1.4 apresenta a melhor proporção de direcionamento seletivo focado em `c2` (80 visitas contra 27 a 49 das demais).

**b) Estabilidade da jogada:** C=0.1 gera instabilidade severa no rollout aleatório, trocando de recomendação a cada salto (`c4` $\to$ `c1` $\to$ `c3`). C=1.4 e C=3.0 mostram forte estabilidade de longo prazo, ambos corrigindo erros iniciais nas 10 iterações para convergir solidamente em `c2` nas 200 iterações.

**c) Melhor jogada com poucas iterações:** O valor C=0.1 acoplado ao rollout semi-guloso foi o único a "cravar" a jogada ótima (`c2`) com apenas 10 iterações. Ao ignorar a exploração prematuramente, ele capitalizou rapidamente em cima do determinismo forte fornecido pela heurística do rollout guloso.

### COMPARAÇÃO GERAL

| Eixo de Análise | Variante 1 | Variante 2 | Variante 3 |
| --- | --- | --- | --- |
| **a) Rollout** | Aleatório | Semi-guloso | - |
| **b) Valor de C** | C = 0.1 | C = 1.4 | C = 3.0 |
| **c) Iterações** | 10 | 50 | 200 |
| **d) Estabilidade** | Baixa | Média | Alta |

**Justificativas:**

* **a) Rollout:** O aleatório é quase 3x mais rápido processualmente (~41ms vs ~130ms em 200 iters), mas o semi-guloso compensa ao introduzir conhecimento do domínio, convergindo para a decisão correta com ¼ das simulações.
* **b) Valores de C:** C=0.1 provoca convergência prematura em máximos locais errados se a heurística for cega, enquanto C=3.0 atrasa o refinamento estatístico ao explorar opções inúteis; C=1.4 entrega o equilíbrio matemático ideal de convergência progressiva.
* **c) Número de Iterações:** 10 iterações sofrem de ruído estatístico agudo e geram recomendações quase aleatórias, 50 iterações iniciam a estabilização real do MCTS, e 200 iterações garantem a prova matemática da decisão.
* **d) Estabilidade das decisões:** A pior estabilidade reside na combinação de baixas iterações com parâmetros extremos (C=0.1 e random), enquanto a estabilidade plena emerge do uso do fator heurístico (semi-guloso) pareado com a calibragem clássica de C=1.4 em alto volume.

A configuração recomendada para este problema é o **Rollout Semi-guloso com C=1.4 e 50 iterações**. Esta combinação atinge o ponto de eficiência ideal, garantindo a identificação cravada e estável da jogada ótima (`c2`) com um custo computacional extremamente viável (~53 ms), dispensando o processamento desnecessário de 200 iterações. O uso de C=1.4 previne tanto a cegueira gananciosa de C=0.1 quanto a dispersão difusa de C=3.0, extraindo o máximo do conhecimento tático embutido no rollout guloso.

---
