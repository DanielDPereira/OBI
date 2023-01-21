# Cubo e quadrado
O número 729 tem uma particularidade interessante: é ao mesmo tempo o cubo e o quadrado de um
número inteiro (729 = 27<sup>2</sup> e 729 = 9<sup>3</sup>). Outro número com essa particularidade é 4096 (4096 = 64<sup>2</sup>
e 4096 = 16<sup>3</sup>).

Sua tarefa é, dados dois números inteiros *A* e *B*, determinar quantos números no intervalo entre *A*
e *B* são ao mesmo tempo cubo e quadrado de um número inteiro.
## Entrada
A primeira da entrada contém um inteiro *A*, o limite inferior do intervalo de interesse, a segunda
linha contém um inteiro *B*, o limite superior do intervalo de interesse (*A* e *B* fazem parte do intervalo
de interesse).
## Saída
Seu programa deve produzir uma única linha na saída, contendo um único inteiro, a quantidade de
números que são ao mesmo tempo cubo e quadrado de um número inteiro, para todos os números
do intervalo de interesse.
## Restrições
- 1 ≤ *A* < *B* ≤ 100 000 000
## Informações sobre a pontuação
- Para um conjunto de casos de testes valendo 30 pontos, *B* ≤ 100 000.
- Para um conjunto de casos de testes valendo outros 70 pontos, nenhuma restrição adicional.

| Exemplo de entrada 1 | Exemplo de saída 1 |
| -------------------- | ------------------ |
| 64                   | 2                  |
| 729                  |                    |

*Explicação do exemplo 1:* os números que são cubo e quadrado de um outro número no intervalo
entre 64 e 729 são somente 64 e 729, portanto a resposta é 2.

| Exemplo de entrada 2 | Exemplo de saída 1 |
| -------------------- | ------------------ |
| 3000                 | 1                  |
| 5000                 |                    |

*Explicação do exemplo 2:* 4096 é o único número no intervalo entre 3000 e 5000 que é cubo e
quadrado de um outro número, portanto a resposta é 1.
