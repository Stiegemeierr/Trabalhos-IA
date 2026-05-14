


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

<!-- Tabelas e resultados do código - grafo original -->

#### 1.2.2 Grafo Modificado

<!-- Tabelas e resultados do código - grafo modificado -->
<!-- Incluir nota sobre quais dois nós foram alterados e por quê -->

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

<!-- Tabelas e resultados do código - heurística original -->

#### 2.2.2 Heurística Modificada

<!-- Tabelas e resultados do código - heurística modificada -->
<!-- Incluir nota sobre quais três nós foram alterados, valores antigos/novos e qual tornou h(n) inadmissível -->

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

<!-- Tabela passo a passo gerada pelo código -->

#### 3.3.2 Random Restart Hill-Climbing (20 execuções)

<!-- Tabela de execuções gerada pelo código -->

#### 3.3.3 Simulated Annealing

<!-- Tabela resumida por passo e tabela de movimentos piores aceitos -->

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

<!-- Saída do Prompt 4 da Q4 -->

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

<!-- Saída do Prompt 1 da Q5 -->

---

### 5.2 Execução Manual: Minimax e Alpha-Beta

<!-- Saída do Prompt 2 da Q5 -->

---

### 5.3 Reordenação e Minimax com Profundidade Limitada

<!-- Saída do Prompt 3 da Q5 -->

---

### 5.4 Execução dos Algoritmos

#### 5.4.1 Árvore Original

<!-- Tabela comparativa gerada pelo código - árvore original -->

#### 5.4.2 Árvore com Folhas Modificadas

<!-- Tabela comparativa gerada pelo código - árvore modificada -->
<!-- Incluir nota sobre quais 3 folhas foram alteradas e justificativa -->

---

### 5.5 Análise do Experimento e Comparação Final

<!-- Saída do Prompt 5 da Q5 -->

---
---

## Questão 06 - Monte Carlo Tree Search (MCTS)

### 6.1 Conceitos Teóricos

<!-- Saída do Prompt 1 da Q6 -->

---

### 6.2 Execução Manual: 10 Iterações com C = 1.4

<!-- Saída do Prompt 2 da Q6 -->

---

### 6.3 Análise do Parâmetro C (0.1, 1.4 e 3.0)

<!-- Saída do Prompt 3 da Q6 -->

---

### 6.4 Execução dos Algoritmos

<!-- Tabela comparativa gerada pelo código (18 combinações) -->

---

### 6.5 Comparação Final

<!-- Saída do Prompt 5 da Q6 -->

---
