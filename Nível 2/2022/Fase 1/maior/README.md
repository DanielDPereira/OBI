# Maior Valor

Nesta tarefa, dados três números inteiros *N* , *M* e *S* você deve escrever um programa para determinar
o maior número inteiro *I* tal que

- *I* está dentro do intervalo [*N*, *M* ] (ou seja, *I* ≥ *N* e *I* ≤ *M* ).
- A soma dos dígitos de *I* é igual a *S*.

## Entrada

A primeira linha contém um inteiro *N* , o menor valor do intervalo. A segunda linha contém um
inteiro *M* , o maior valor do intervalo. A terceira linha contém um inteiro *S*, o valor da soma dos
dígitos, conforme descrito.

## Saída

Seu programa deve produzir uma única linha, contendo um único inteiro, que deve ser o valor de *I*
obedecendo às restrições acima, ou −1 se não existir.

## Restrições

- 1 ≤ *N* ≤ *M* ≤ 10 000
- 1 ≤ *S* ≤ 36

## Informações sobre a pontuação
- Para um conjunto de casos de testes valendo 10 pontos, *M* ≤ 100.

| Exemplo de entrada 1 | Exemplo de saída 1 |
| -------------------- | ------------------ |
| 1                    | 60                 |
| 100                  |                    |
| 6                    |                    |

*Explicação do exemplo 1:* 60 é o maior inteiro no intervalo [1, 100] cuja soma dos dígitos é igual
a 6.

| Exemplo de entrada 2 | Exemplo de saída 2 |
| -------------------- | ------------------ |
| 1000                 | -1                 |
| 1001                 |                    |
| 3                    |                    |

*Explicação do exemplo 2:* Não há número inteiro no intervalo [1000, 1001] cuja soma dos dígitos
é igual a 3.

| Exemplo de entrada 3 | Exemplo de saída 3 |
| -------------------- | ------------------ |
| 80                   | 480                |
| 500                  |                    |
| 12                   |                    |

*Explicação do exemplo 3:* 480 é o maior inteiro no intervalo [80, 500] cuja soma dos dígitos é
igual a 12.
