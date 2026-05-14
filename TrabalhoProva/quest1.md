## Questão 01 -- Busca em amplitude/largura, Busca em profundidade e Busca iterativa em profundidade

Um agente deve se deslocar entre salas de um prédio. Cada sala é representada por uma letra. As conexões representam movimentos permitidos entre salas. Todas as ações possuem custo unitário. A tabela abaixo apresenta o grafo do problema.

| **Sala** | **Salas vizinhas (ordem obrigatória)** |
| :---: | :--- |
| A | B, C, D |
| B | E, F |
| C | G, H |
| D | I |
| E | J |
| F | K, L |
| G | M |
| H | N, O |
| I | P |
| J | - |
| K | Q |
| L | - |
| M | R |
| N | - |
| O | S |
| P | - |
| Q | - |
| R | - |
| S | - |

**Estado inicial:** $A$  
**Estado objetivo:** $S$

Formular o problema acima como **um problema de busca em espaços de estados**. A resposta deve conter:
a) definição formal do estado;
b) estado inicial;
c) teste de objetivo;
d) função sucessora;
e) função de custo;
f) representação escolhida em Python.

Em seguida, resolva o problema utilizando os seguintes algoritmos:
1. Busca em amplitude/largura (Breadth-First Search);
2. Busca em profundidade (Depth-First Search);
3. Busca iterativa em profundidade (Iterative Deepening Search).

Para cada algoritmo, apresentar:
a) ordem completa de expansão dos nós;
b) conteúdo da fronteira após cada expansão;
c) árvore parcial de busca;
d) caminho solução encontrado;
e) profundidade da solução;
f) custo da solução;
g) quantidade de nós gerados;
h) quantidade de nós expandidos.

Preencher uma tabela semelhante ao modelo abaixo.

| **Passo** | **Nó expandido** | **Conteúdo da fronteira** |
| :---: | :---: | :---: |
| 1 | A | [B, C, D] |
| 2 | B | [...] |
| 3 | ... | ... |

Implementar os três algoritmos em Python respeitando os seguintes critérios: NÃO utilizar bibliotecas externas, bibliotecas prontas de grafos e implementações encontradas na internet. Todo o código deve ser autoral.

Experimento adicional: modificar a ordem dos sucessores de exatamente **dois nós** do grafo. Exemplo:
- alterar: $C: G, H$ &nbsp;&nbsp;&nbsp; para: $C: H, G$

Após a modificação, 1) executar novamente os três algoritmos; 2) comparar os resultados obtidos; e 3) analisar o impacto da ordem dos sucessores.

Responder as seguintes questões:
a) O caminho solução mudou?
b) A quantidade de nós expandidos mudou?
c) Algum algoritmo foi mais sensível à ordem dos sucessores?
d) Qual algoritmo apresentou maior consumo de memória?
e) Qual algoritmo encontrou a solução mais rapidamente?

Por fim, comparar os algoritmos considerando: a) completude; b) otimalidade; c) complexidade de tempo; d) complexidade de espaço; e) dependência da ordem dos sucessores; f) comportamento em árvores profundas; g) adequação para problemas grandes.

---