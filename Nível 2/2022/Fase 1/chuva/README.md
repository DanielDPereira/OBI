# Chuva

Eventos climáticos extremos como chuvas descomunais estão cada vez mais frequentes e intensos
em todo o mundo.

O Centro Nacional de Monitoramento da Nlogônia tem medidores de quantidade de chuva dia-a-dia
espalhados por todo o reino. Cada medição é um número inteiro, indicando a quantidade de chuva,
em milímetros, que caiu na Nlogônia num determinado dia. Como o sistema existe há vários anos,
a lista de medições é muito grande.

Preocupado com o assunto, o rei da Nlogônia mandou que o Ministro da Ciência crie um programa
de computador para calcular quantos intervalos de dias existem na lista de medições tal que a soma
das medições nesse intervalo é igual a um certo valor.

Mais precisamente, considere uma lista com *N* medições, indicando a quantidade de chuva do dia 1
ao dia *N* . Considere ainda todos os possíveis intervalos de dias entre 1 e *N* , cada intervalo definido
pelo dia inicial e dia final do intervalo. O rei deseja saber quantos intervalos têm a soma das
medições exatamente igual a um certo valor *S*.

O Ministro da Ciência é um físico brilhante, mas não sabe resolver essa tarefa. Você poderia
ajudá-lo?

## Entrada

A primeira linha contém um inteiro *N* , o número de medições na lista. A segunda linha contém um
inteiro *S*, o valor da soma desejada. A terceira linha contém *N* inteiros *X<sub>i</sub>*, os valores das medições.

## Saída

Seu programa deve produzir uma única linha, contendo um único inteiro, que deve ser o número de
intervalos que têm a soma das medições igual a S.

## Restrições

- 1 ≤ *N* ≤ 100 000
- 0 ≤ *S* ≤ 1 000 000
- 0 ≤ *X<sub>i</sub>* ≤ 10, para 1 ≤ *i* ≤ N

## Informações sobre a pontuação

- Para um conjunto de casos de testes valendo 20 pontos, *N* ≤ 300.
- Para um outro conjunto de casos de testes valendo 30 pontos, *N* ≤ 1000.

| Exemplo de entrada 1 | Exemplo de saída 1 |
| -------------------- | ------------------ |
| 6                    | 6                  |
| 2                    |                    |
| 0 2 0 1 0 1          |                    |

*Explicação do exemplo 1:* São 6 os intervalos com soma igual a 2: [2], [0,2], [2,0], [0,2,0], [1,0,1]
e [0,1,0,1]

| Exemplo de entrada 2 | Exemplo de saída 2 |
| -------------------- | ------------------ |
| 8                    | 0                  |
| 13                   |                    |
| 10 1 0 0 9 10 1 5    |                    |

*Explicação do exemplo 2:* Não há intervalo com soma igual a 13.

| Exemplo de entrada 3 | Exemplo de saída 3 |
| -------------------- | ------------------ |
| 5                    | 1                  |
| 6                    |                    |
| 1 0 3 0 2            |                    |

*Explicação do exemplo 3:* Há apenas um intervalo com soma igual a 6: [1, 0, 3, 0, 2].
