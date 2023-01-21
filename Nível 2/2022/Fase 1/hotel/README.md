# Hotel
O hotel da Colônia de Férias dos Professores está com uma promoção para as férias de julho. A
promoção é válida para quem chegar a partir do dia 1 de julho e sair no dia 1 de agosto.

O preço da diária do hotel é menor para quem chegar mais cedo, e vai aumentando a cada dia. Mais
precisamente, a promoção funciona assim:
- A diária do hotel para cada quem chegar no dia 1 é D Reais. Assim, quem chegar no dia 1
vai pagar um total de 31 × D Reais.
- A diária do hotel aumenta A reais por dia. Ou seja, a diária é D + A Reais para quem chegar
no dia 2; D + 2 × A Reais no dia 3; D + 3 × A Reais no dia 4 e assim por diante.
- A partir do dia 16 a diária não aumenta mais.

Note que quem chegar no dia 2 vai pagar um total de 30 × (D + A) reais; quem chegar no dia 3
vai pagar um total de 29 × (D + 2 × A) reais, e assim por diante.

Bruno gosta muito da professora Vilma, e para agradá-la quer ajudá-la a planejar suas férias, escre-
vendo um programa para calcular o total (em Reais) que a professora Vilma vai gastar, dependendo
do dia em que chegar no hotel.

## Entrada
A primeira linha contém um inteiro *D*, o valor da diária no dia 1. A segunda linha contém um
inteiro *A*, o aumento da diária a cada dia a partir do dia 2 até o dia 15 (inclusive). A terceira linha
contém um inteiro *N* , o dia de chegada no hotel.

## Saída
Seu programa deve produzir uma única linha, contendo um único inteiro, que deve ser o valor total
a ser pago ao hotel pela estadia.

## Restrições
- 1 ≤ *D* ≤ 1 000
- 1 ≤ *A* ≤ 1 000
- 1 ≤ *N* ≤ 31

## Informações sobre a pontuação
- Para um conjunto de casos de testes valendo 10 pontos, *N* = 1.

| Exemplo de entrada 1 | Exemplo de saída 1 |
| -------------------- | ------------------ |
| 100                  | 3100               |
| 10                   |                    |
| 1                    |                    |

*Explicação do exemplo 1:* Como a chegada é no dia 1, o valor da diária com a promoção é 100.
Do dia 1 ao dia 31 são 31 diárias. Assim, o total a pagar é 31 × 100.

| Exemplo de entrada 2 | Exemplo de saída 2 |
| -------------------- | ------------------ |
| 100                  | 6460               |
| 20                   |                    |
| 15                   |                    |

*Explicação do exemplo 2:* Como a chegada é no dia 15, o valor da diária com a promoção é
100 + 14 × 20 = 380. Do dia 15 ao dia 31 são 17 diárias. Assim, o total a pagar é 17 × 380
= 6460.

| Exemplo de entrada 3 | Exemplo de saída 3 |
| -------------------- | ------------------ |
| 100                  | 2720               |
| 5                    |                    |
| 16                   |                    |

*Explicação do exemplo 3:* Como a chegada é no dia 16, o valor da diária com a promoção é
100 + 14 × 5 = 170. Do dia 16 ao dia 31 são 16 diárias. Assim, o total a pagar é 16 × 170 =
2720.
