#### 1. BACKTRACKING SIMPLES

* **Solução:** {'T1': 'A', 'T2': 'B', 'T3': 'C', 'T4': 'A', 'T5': 'B', 'T6': 'A'}
* **Estados explorados:** 10
* **Retrocessos:** 0
* **Tempo:** 0.6154 ms

#### 2. BACKTRACKING + MRV

* **Solução:** {'T3': 'B', 'T2': 'A', 'T1': 'B', 'T4': 'A', 'T5': 'B', 'T6': 'A'}
* **Estados explorados:** 9
* **Retrocessos:** 0
* **Tempo:** 0.1442 ms

#### 3. BACKTRACKING + DEGREE

* **Solução:** {'T2': 'A', 'T4': 'A', 'T5': 'B', 'T1': 'B', 'T3': 'B', 'T6': 'A'}
* **Estados explorados:** 9
* **Retrocessos:** 0
* **Tempo:** 0.1023 ms

#### 4. FORWARD CHECKING

* **Solução:** {'T1': 'A', 'T2': 'B', 'T3': 'C', 'T4': 'A', 'T5': 'B', 'T6': 'A'}
* **Estados explorados:** 6
* **Retrocessos:** 0
* **Tempo:** 0.0820 ms

#### 5. BACKJUMPING

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