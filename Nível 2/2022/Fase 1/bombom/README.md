# Bombom

Bombom é um jogo de cartas para duas pessoas, jogado com apenas dezesseis cartas: Ás, Valete,
Dama e Rei, nos quatro naipes (Copas, Espadas, Ouros e Paus). Cada carta tem um valor, que
depende da figura e do naipe.

A cada partida, as cartas são embaralhadas e colocadas em um monte. Inicialmente uma carta do
monte é virada e mostrada aos dois jogadores: o naipe dessa carta é chamado de *naipe dominante*
da partida.

Então cada jogador recebe três cartas do monte. Ganha a partida o jogador que tem as cartas cuja
soma dos valores é maior.

O valor das cartas é dado na tabela abaixo:

| Figura | Naipe não dominante | Naipe Dominante |
| ------ | ------------------- | --------------- |
| Ás     | 10                  | 14              |
| Valete | 11                  | 15              |
| Dama   | 12                  | 16              |
| Rei    | 13                  | 17              |

Luana e Edu estão jogando Bombom e querem sua ajuda para determinar o vencedor da partida,
ou se há empate.

## Entrada

A entrada contém sete linhas, cada linha contendo a descrição de uma carta. Cada carta é descrita
por duas letras. A primeira letra de uma carta indica a figura e pode ser `A`, `J`, `Q` ou `K`, representando
respectivamente as figuras Ás, Valete, Dama e Rei. A segunda letra de uma carta indica o naipe e
pode ser `C`, `E`, `O` ou `P`, representando respectivamente os naipes Copas, Espadas, Ouros e Paus. O
naipe da primeira carta da entrada é o naipe dominante da partida. A segunda, terceira e quarta
cartas da entrada são as cartas de Luana. A quinta, sexta e sétima cartas da entrada são as cartas
de Edu.

## Saída

Seu programa deve produzir uma única linha, contendo somente o nome do jogador que ganha a
partida, ou `empate` caso não haja um ganhador.

## Restrições

- As cartas na entrada obedecem ao formato descrito no enunciado.
- Não há cartas repetidas na entrada.

| Exemplo de entrada 1 | Exemplo de saída 1 |
| -------------------- | ------------------ |
| AC                   | Edu                |
| JC                   |                    |
| JE                   |                    |
| JP                   |                    |
| KO                   |                    |
| KP                   |                    |
| QE                   |                    |

*Explicação do exemplo 1:* O naipe dominante é Copas. As cartas de Luana valem 15 + 11 +
11 = 37; as cartas de Edu valem 13 + 13 + 12 = 38. Assim, Edu é o vencedor.

| Exemplo de entrada 2 | Exemplo de saída 2 |
| -------------------- | ------------------ |
| QP                   | empate             |
| QC                   |                    |
| AC                   |                    |
| KP                   |                    |
| KO                   |                    |
| KE                   |                    |
| KC                   |                    |

*Explicação do exemplo 2:* O naipe dominante é Paus. As cartas de Luana valem 12 + 10 + 17
= 39; as cartas de Edu valem 13 + 13 + 13 = 39. Assim, há empate.

| Exemplo de entrada 3 | Exemplo de saída 3 |
| -------------------- | ------------------ |
| KE                   | Luana              |
| QE                   |                    |
| AC                   |                    |
| AE                   |                    |
| AP                   |                    |
| KO                   |                    |
| JE                   |                    |

*Explicação do exemplo 3:* O naipe dominante é Espadas. As cartas de Luana valem 16 + 10 + 14 = 40; as cartas de Edu valem 10 + 13 + 15 = 38. Assim, Luana é a vencedora.
