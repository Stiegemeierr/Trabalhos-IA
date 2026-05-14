
## Questão 05 -- Minimax e Poda Alpha-Beta

Considerar a seguinte árvore de jogo para um jogo determinístico de dois jogadores. O jogador MAX realiza a primeira jogada na raiz da árvore. Os valores nas folhas representam a utilidade final do jogo.

**Estrutura da Árvore:**
- **MAX** (Raiz)
  - **MIN** (Filho 1)
    - **MAX** (Neto 1) $\rightarrow$ Folhas: `3`, `5`
    - **MAX** (Neto 2) $\rightarrow$ Folhas: `6`, `9`
  - **MIN** (Filho 2)
    - **MAX** (Neto 3) $\rightarrow$ Folhas: `1`, `2`
    - **MAX** (Neto 4) $\rightarrow$ Folhas: `0`, `-1`
  - **MIN** (Filho 3)
    - **MAX** (Neto 5) $\rightarrow$ Folhas: `7`, `4`
    - **MAX** (Neto 6) $\rightarrow$ Folhas: `5`, `6`

Os valores terminais são apresentados abaixo, da esquerda para a direita:
$$[3, 5, 6, 9, 1, 2, 0, -1, 7, 4, 5, 6]$$

A ordem de expansão dos filhos deve seguir obrigatoriamente da esquerda para a direita. Explicar:
a) objetivo do algoritmo Minimax;
b) diferença entre nós MAX e MIN;
c) conceito de utilidade;
d) propagação de valores na árvore;
e) hipótese de adversário perfeito;
f) objetivo da poda Alpha-Beta.

Executar passo a passo o algoritmo Minimax na árvore apresentada e apresentar: a) valores calculados em cada nó; b) ordem de expansão; c) propagação dos valores; d) decisão tomada por MAX; e) caminho escolhido pelo algoritmo; f) árvore parcialmente preenchida.

Apresentar a tabela:

| **Nó** | **Tipo** | **Valor Minimax** |
| :---: | :---: | :---: |
| A | MAX | ... |
| B | MIN | ... |
| C | MAX | ... |

Executar a **Poda Alpha-Beta** utilizando a MESMA ordem de expansão. Apresentar:
a) valores de $\alpha$ e $\beta$ em cada passo;
b) momento em que ocorreram podas;
c) quais ramos foram podados;
d) motivo matemático da poda;
e) quantidade de nós NÃO explorados.

Apresentar a tabela:

| **Passo** | **Nó** | **$\alpha$** | **$\beta$** | **Poda?** |
| :---: | :---: | :---: | :---: | :---: |
| 1 | A | ... | ... | não |
| 2 | B | ... | ... | sim |

Alterar a ordem de expansão dos filhos de forma a maximizar o número de podas. Em seguida, discutir:
a) Quantas podas ocorreram antes?
b) Quantas podas ocorreram depois?
c) Por que a nova ordem melhora a eficiência?
d) Qual a relação entre ordenação e desempenho?

Considerar agora que a árvore é muito grande e que a busca deve parar na profundidade 2. Os seguintes valores heurísticos devem ser usados nos nós não-terminais da profundidade limite:
$$[4, 7, 2, 5, 6, 1]$$
Responder:
a) executar Minimax limitado;
b) utilizar os valores heurísticos;
c) comparar a decisão com Minimax completo;
d) discutir possíveis erros causados pela heurística.

Implementar os algoritmos *Minimax*, *Alpha-Beta* e *Minimax com profundidade limitada*, em Python respeitando os seguintes critérios: NÃO utilizar bibliotecas externas, bibliotecas prontas de jogos, e implementações encontradas na internet. Todo o código deve ser autoral.

Comparar Minimax e Alpha-Beta considerando: a) número de nós explorados; b) quantidade de podas; c) custo computacional; d) consumo de memória; e) impacto da ordenação dos movimentos; f) qualidade das decisões.

Em um experimento adicional, modificar os valores de exatamente 3 folhas da árvore. Após isso:
1. executar novamente Minimax;
2. executar novamente Alpha-Beta;
3. verificar se a decisão final mudou;
4. analisar a sensibilidade do algoritmo às utilidades.

---