# Plano de Internet
João conseguiu contratar um ótimo plano de Internet para o seu telefone celular. O plano permite que João utilize uma quota de até X megabytes de dados por mês para navegar na Internet. Se João não usa toda a sua quota no mês, os megabytes que ele não usou são adicionados à quota do mês seguinte. Pelo contrato, João nunca pode usar mais megabytes do que a sua quota corrente. Por exemplo, se X=200 megabytes e João usou 150 no primeiro mês e 220 megabytes no segundo mês, então no terceiro mês João tem uma quota de 230 megabytes para usar (50 megabytes são transferidos do primeiro para o segundo mês, 30 megabytes são transferidos do segundo para o terceiro mês). Nesta tarefa são dados o valor da quota mensal X e quantos megabytes João usou em cada um dos primeiros N meses do plano. Você deve determinar quantos megabytes João tem para usar no mês N+1.

## Entrada
A primeira linha da entrada contém um número inteiro X, o valor da quota mensal em megabytes. A segunda linha contém um inteiro N, o número de meses. Cada uma das linhas seguintes contém um número inteiro M_i, indicando a quantidade de megabytes que João usou em cada mês, do mês 1 até o mês N.

## Saída
Seu programa deve produzir uma única linha, contendo um único número inteiro, a quantidade de megabytes que João tem para usar no mês N+1.

## Restrições
- 1 ≤ X ≤ 100
- 1 ≤ N ≤ 100
- 0 ≤ M_i ≤ 10000 para 1 ≤ i ≤ N
- M_i nunca é maior do que a quantidade de megabytes que João tem para usar no mês.

## Informações sobre a pontuação
- Para um conjunto de casos de testes valendo 10 pontos, 1 ≤ N ≤ 3.
- Para um conjunto de casos de testes valendo 90 pontos, nenhuma restrição adicional.

| Exemplo de entrada 1 | Exemplo de saída 1 |
| -------------------- | ------------------ |
| 100                  | 130                |
| 2                    |                    |
| 50                   |                    |
| 120                  |                    |


| Exemplo de entrada 2 | Exemplo de saída 2 |
| -------------------- | ------------------ |
| 10                   | 28                 |
| 3                    |                    |
| 4                    |                    |
| 6                    |                    |
| 2                    |                    |



| Exemplo de entrada 3 | Exemplo de saída 3 |
| -------------------- | ------------------ |
| 100                  | 100                |
| 2                    |                    |
| 100                  |                    |
|100                   |                    |

