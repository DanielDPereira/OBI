# Camisetas da Olimpíada
A Olimpíada Municipal de Programação vai distribuir camisetas para os melhores colocados, e por
isso solicitou que os premiados informassem o tamanho preferido da camiseta, entre os tamanhos
pequeno e médio.  

A empresa que confeccionou as camisetas, por uma falha, pode ter se enganado na quantidade de
camisetas para cada tamanho. Foram produzidas camisetas em número suficiente para todos os
premiados, mas talvez não do tamanho preferido.  

Dadas a lista com os tamanhos preferidos pelos premiados e a quantidade de camisetas de cada
tamanho produzidas pela empresa, escreva um programa para determinar se todos os premiados
receberão camisetas do tamanho escolhido.
## Entrada
A primeira linha contém um inteiro *N* , o número de premiados. A segunda linha contém *N* inteiros
*T<sub>i</sub>*, indicando os tamanhos solicitados pelos premiados, sendo que *T<sub>i</sub>* = 1 representa o tamanho
pequeno e *T<sub>i</sub>* = 2 representa o tamanho médio. A terceira linha contém um inteiro *P* , o número de
camisetas de tamanho pequeno produzidas. A quarta e última contém um inteiro *M* , o número de
camisetas de tamanho médio produzidas.
## Saída
Seu programa deve produzir uma única linha, contendo um único caractere, que deve ser a letra
maiúscula ‘S’ se todos os premiados serão atendidos com a camiseta do tamanho que escolheram,
ou a letra maiúscula ‘N’ caso contrário.
## Restrições
- 1 ≤ *N* ≤ 1000
- 0 ≤ *P* ≤ 1000
- 0 ≤ *M* ≤ 1000
- *N* ≤ *P* + *M*
- 1 ≤ *X<sub>i</sub>* ≤ 2 para 1 ≤ *i* ≤ *N*
## Informações sobre a pontuação
- Para um conjunto de casos de testes valendo 20 pontos, 1 ≤ *N* ≤ 10.

| Exemplo de entrada 1 | Exemplo de saída 1 |
| -------------------- | ------------------ |
| 5                    | S                  |
| 1 1 2 1 2            |                    |
| 3                    |                    |
| 2                    |                    |

| Exemplo de entrada 2 | Exemplo de saída 2 |
| -------------------- | ------------------ |
| 4                    | N                  |
| 2 2 2 2              |                    |
| 1                    |                    |
| 3                    |                    |

| Exemplo de entrada 3 | Exemplo de saída 3 |
| -------------------- | ------------------ |
| 6                    | N                  |
| 1 1 1 2 1 1          |                    |
| 4                    |                    |
| 4                    |                    |
