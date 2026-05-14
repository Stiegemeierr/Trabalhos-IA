
## Questão 06 -- Monte Carlo Tree Search (MCTS)

Considerar o jogo Connect-4 simplificado abaixo. O jogador vermelho deve decidir qual coluna jogar. O estado atual é:

| | | | |
| :---: | :---: | :---: | :---: |
| &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| **A** | **V** | &nbsp; | &nbsp; |
| **V** | **A** | &nbsp; | &nbsp; |

**Legenda:** V: vermelho e A: amarelo. As ações possíveis são: $c_1, c_2, c_3, c_4$

Para MCTS, explicar detalhadamente:
a) seleção;
b) expansão;
c) simulação (rollout);
d) retropropagação;
e) papel do número de visitas;
f) papel do número de vitórias;
g) diferença entre exploração e explotação.

Executar 10 iterações do algoritmo MCTS. Em cada iteração apresentar:
a) caminhos selecionados;
b) nó expandido;
c) resultado do rollout;
d) atualização de: $N(s), W(s)$
e) árvore parcial construída.

Utilizar:
$$UCT(j) = \frac{w_j}{n_j} + C \sqrt{\frac{\ln N}{n_j}}$$
com $C = 1.4$  
e calcular:
a) valor de UCT para cada filho;
b) nó selecionado;
c) influência do termo de exploração;
d) influência do termo de explotação.

Apresentar a seguinte tabela:

| **Jogada** | **Visitas** | **Vitórias** | **UCT** |
| :---: | :---: | :---: | :---: |
| c1 | 3 | 2 | ... |
| c2 | 5 | 4 | ... |
| c3 | 1 | 1 | ... |

Executar novamente o algoritmo utilizando $C = 0.1$ e depois $C = 3.0$ e comparar:
a) quantidade de exploração;
b) diversidade de jogadas;
c) estabilidade das decisões;
d) qualidade das jogadas encontradas.

Implementar dois tipos de rollout:
1. rollout totalmente aleatório;
2. rollout semi-guloso:
   - priorizar jogadas centrais;
   - bloquear vitória imediata do adversário.

e comparar:
a) qualidade das decisões;
b) velocidade de convergência;
c) número de simulações necessárias.

Implementar *seleção, expansão, rollout, retropropagação e cálculo de UCT* em Python respeitando os seguintes critérios: NÃO utilizar bibliotecas externas, bibliotecas prontas de jogos e implementações encontradas na internet. Todo o código deve ser autoral.

Por fim, comparar: a) rollout aleatório vs semi-guloso; b) diferentes valores de $C$; c) número de iterações; d) estabilidade das decisões.