
## Questão 03 -- Busca Local em Problema das N-Rainhas

Considerar o problema das 8-Rainhas. O objetivo é posicionar 8 rainhas em um tabuleiro $8 \times 8$ de forma que nenhuma rainha ataque outra. Duas rainhas entram em conflito quando estão i) na mesma linha, ii) na mesma coluna e iii) na mesma diagonal. Nesta atividade, cada estado será representado por um vetor:
$$[s_1, s_2, s_3, s_4, s_5, s_6, s_7, s_8]$$
onde: $s_i = \text{linha da rainha na coluna } i$

Exemplo: $[4, 2, 7, 3, 6, 8, 5, 1]$ significa:
- coluna 1 $\rightarrow$ linha 4;
- coluna 2 $\rightarrow$ linha 2;
- ...
- coluna 8 $\rightarrow$ linha 1.

Iniciar a busca a partir do estado:
$$[1, 1, 1, 1, 1, 1, 1, 1]$$
Considerar a seguinte função heurística:
$h(s) = \text{número total de pares de rainhas em conflito}$

Objetivo: $\min h(s)$  
Um estado solução ocorre quando: $h(s) = 0$

Modelar o problema como um **problema de busca local**. Apresentar: a) representação do estado; b) definição de vizinho; c) função de avaliação; d) critério de parada; e) interpretação da superfície de busca.

Em seguida, resolver o problema manualmente utilizando o **algoritmo Hill-Climbing**, onde um vizinho é obtido movendo exatamente UMA rainha para outra linha da MESMA coluna. A solução deve apresentar:
a) estado atual;
b) todos os vizinhos avaliados em cada iteração;
c) valor de $h(s)$ para cada vizinho;
d) estado escolhido;
e) explicação da escolha realizada;
f) número total de iterações;
g) estado final encontrado.

A resposta deve conter tabelas semelhantes ao modelo:

| **Iteração** | **Estado** | **h(s)** |
| :---: | :---: | :---: |
| 0 | [1,1,1,1,1,1,1,1] | 28 |
| 1 | [...] | ... |
| 2 | [...] | ... |

Além disso, para cada iteração, mostrar pelo menos os 5 melhores vizinhos gerados.

Durante a execução do Hill-Climbing, identificar se ocorreu máximo local, platô, pico estreito ou solução global. Caso algum desses itens ocorra, explicar:
a) por que ocorreu;
b) como isso afetou a busca;
c) como poderia ser evitado.

Implementar uma versão com **Random Restart Hill-Climbing**:
- Executar o algoritmo 20 vezes;
- Cada execução deve iniciar em um estado aleatório;
- Registrar: número de passos, valor final de $h(s)$, se encontrou solução ou não.

Apresentar a seguinte tabela:

| **Execução** | **Estado inicial** | **Passos** | **h(s) final** |
| :---: | :---: | :---: | :---: |
| 1 | [...] | ... | ... |
| 2 | [...] | ... | ... |

Implementar o algoritmo **Simulated Annealing** usando a seguinte função de aceitação:
$$P = e^{-\Delta E / T}$$
onde: $\Delta E$: aumento do número de conflitos; $T$: temperatura atual.

Apresentar:
a) valor inicial da temperatura;
b) política de resfriamento utilizada;
c) exemplos de movimentos piores aceitos;
d) comparação com Hill-Climbing simples;
e) quantidade de soluções válidas encontradas.

Implementar os algoritmos *Hill-Climbing*, *Random Restart Hill-Climbing* e *Simulated Annealing* em Python respeitando os seguintes critérios: NÃO utilizar bibliotecas externas, bibliotecas prontas de otimização e implementações encontradas na internet. Todo o código deve ser autoral.

Por fim, comparar os algoritmos considerando: a) qualidade das soluções; b) velocidade de convergência; c) sensibilidade ao estado inicial; d) capacidade de escapar de máximos locais; e) custo computacional; f) estabilidade dos resultados.

---