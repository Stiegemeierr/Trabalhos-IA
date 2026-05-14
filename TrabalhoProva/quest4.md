
## Questão 04 -- CSP e Otimizações de Busca

Um hospital precisa montar automaticamente a escala de plantões de um pequeno grupo de médicos. Os turnos são:
$$T_1, T_2, T_3, T_4, T_5, T_6$$
Os médicos disponíveis são:
$$\{A, B, C, D\}$$
Cada turno deve possuir exatamente um médico.

Restrições que devem ser consideradas:
1. O mesmo médico NÃO pode trabalhar em turnos consecutivos.
2. O médico $A$ não pode trabalhar em: $T_3$
3. O médico $B$ deve trabalhar em pelo menos um turno entre: $T_1, T_2$
4. O médico $C$ não pode trabalhar simultaneamente em: $T_2 \text{ e } T_3$ (Nota: em um mesmo turno só há 1 médico, assume-se que não pode fazer os dois).
5. O médico $D$ pode trabalhar no máximo dois turnos.

Modelar o problema como um **Constraint Satisfaction Problem (CSP)**. Apresentar: a) conjunto de variáveis; b) domínio de cada variável; c) restrições unárias; d) restrições binárias; e) restrições globais; f) representação do grafo de restrições. 

Em seguida, resolver o problema manualmente utilizando **Backtracking** e apresentar:
a) árvore parcial da busca;
b) ordem de atribuição das variáveis;
c) conflitos encontrados;
d) estados descartados;
e) retrocessos realizados;
f) solução final encontrada.

Apresentar a tabela:

| **Passo** | **Variável atribuída** | **Estado parcial** |
| :---: | :---: | :---: |
| 1 | T1=A | {T1=A} |
| 2 | T2=A  | conflito |
| 3 | T2=B | {T1=A, T2=B} |

Resolver o problema utilizando **MRV (Minimum Remaining Values)** e **Degree Heuristic** e explicar:
a) qual variável foi escolhida em cada passo;
b) por que ela foi escolhida;
c) como MRV reduziu o espaço de busca;
d) como Degree influenciou a busca.

Implementar **Forward Checking** e apresentar:
a) redução dos domínios após cada atribuição;
b) domínios eliminados;
c) momento em que inconsistências foram detectadas;
d) comparação com Backtracking simples.

Implementar **Backjumping** e apresentar:
a) variáveis responsáveis pelos conflitos;
b) saltos realizados;
c) diferenças para backtracking tradicional;
d) redução observada na árvore de busca.

Implementar os algoritmos *Backtracking*, *Backtracking + MRV*, *Backtracking + Degree*, *Forward Checking* e *Backjumping* em Python respeitando os seguintes critérios: NÃO utilizar bibliotecas externas, bibliotecas prontas de CSP, OR-Tools e implementações encontradas na internet. Todo o código deve ser autoral.

Por fim, comparar os algoritmos considerando: a) número de estados explorados; b) número de retrocessos; c) velocidade de execução; d) consumo de memória; e) facilidade de implementação; f) eficiência prática.

---