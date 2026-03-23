## 1. Explicação e Formulação do Problema

O Problema dos Missionários e Canibais é um quebra-cabeça clássico na Inteligência Artificial, célebre por ter sido o foco do primeiro artigo que abordou a formulação de problemas de um ponto de vista puramente analítico, publicado por Amarel em 1968. O desafio consiste em transportar $N$ missionários e $N$ canibais de uma margem de um rio para a outra usando um barco com capacidade máxima para duas pessoas. A restrição fundamental, que confere complexidade ao problema, é que em nenhum momento o número de missionários pode ser estritamente menor que o número de canibais em qualquer uma das margens, sob pena de os missionários serem devorados.

Para que um agente inteligente possa encontrar a solução ótima, abstraímos os detalhes físicos irrelevantes e modelamos o cenário sob o paradigma de resolução de problemas por meio de busca. O problema fica matematicamente formalizado por cinco componentes:

**Estado:** Adotamos uma representação atômica onde cada estado é uma "caixa-preta" indivisível para o algoritmo. Representamos um estado matematicamente pela tupla $(M_{esq}, C_{esq}, B_{esq})$, que indica a quantidade de missionários, canibais e barcos presentes na margem esquerda do rio.
* **Estado Inicial:** O problema começa com todas as entidades na margem de origem. Para o caso genérico de $N$ indivíduos, define-se como a tupla $(N, N, 1)$.
* **Teste de Objetivo:** Verifica se todos os indivíduos e o barco atravessaram o rio com sucesso, ou seja, alcançaram o estado $(0, 0, 0)$.
* **Ações e Filtro de Restrição:** A função `AÇÕES(s)` retorna as viagens válidas do barco $(m, c)$ obedecendo à capacidade da embarcação ($1 \le m + c \le 2$). Crucialmente, esta função atua como um filtro: ela só retorna ações que resultem em estados onde os missionários não estejam em desvantagem numérica em nenhuma das margens.
* **Modelo de Transição e Custo de Caminho:** A função `RESULTADO(s, a)` calcula a transição, subtraindo a tupla da ação da margem esquerda se o barco estiver indo, ou somando se estiver voltando. Cada travessia possui um custo de caminho unitário ($c = 1$).
