# Inteligência artificial
## 1. O problema do fazendeiro

Considere o seguinte cenário: "um fazendeiro está levando uma raposa, uma galinha e um saco de grãos para casa. Para chegar lá, ele precisa atravessar um rio de barco. Só que ele pode levar consigo apenas um item de cada vez. Se a raposa for deixada sozinha com a galinha, ela comerá a galinha. Se a galinha for deixada sozinha com os grãos, ela comerá os grãos. Como o fazendeiro poderá atravessar o rio mantendo todo seu suprimento intacto?". Esta situação pode ser modelada como um problema de busca. Pede-se:

* **Formulação do problema:**

  A primeira consideração que fizemos foi delegar que margemEsquerda será a margem objetivo e margemDireita será a margem inicial.
  Então, atribuimos uma numeração para cada item (saco de grãos, raposa e galinha), para que o código fique mais limpo.

      grãos -> 1
      raposa -> 2
      galinha -> 3

  No caso do fazendeiro, vamos considerá-lo como um bit de sinal (0 ou 1), para indicar em qual margem do rio ele está.  
  Para representar um estado vamos usar uma lista, na qual cada posição será um item. Por exemplo, para o estado inicial:

  estadoInicial = [0,0,0,0,1,1,2,3]

  - Os quatro primeiros elementos da lista (estadoInicial[:4]) referenciam a margem esquerda e, os quatro últimos (estadoInicial[4:]), a margem direita. 
  - O primeiro item de cada margem (estadoInicial[0] e estadoInicial[4]) simboliza o fazendeiro Quando ele é 0, significa que o fazendeiro não se encontra nessa margem.
  - As outras posições da lista só podem receber um valor cada uma, ou seja, os itens não podem mudar de lugar na margem. Sendo assim, estadoInicial[1] e estadoInicial[5] só podem receber o valor específico de grão (1), estadoInicial[2] e estadoInicial[6] só podem receber o valor específico de raposa (2), estadoInicial[3] e estadoInicial[7] só podem receber o valor específico de galinha (3).
  - O 0 siginifica que nenhum item se encontra naquela margem.

  Como exemplo, o estado em que o fazendeiro atravessou a galinha para a margem esquerda:

  estado = [1,0,0,3,0,1,2,0]

  Feitas as considerações, temos:

  - **Estado inicial**: [0, 0, 0, 0, 1, 1, 2, 3] (Todos na margem direita do rio);
  - **Ações possíveis**: Escolher item, atravessar o rio;
  - **Modelo de transição**: Ao executar a ação de atravessar o rio, devolver quais itens estão em cada margem;
  - **Teste de objetivo:** verificar se todos os itens estão na margem esquerda do rio (margem da casa);
  - **Custo do caminho:** 1 para cada ação de atravessar o rio;

  Colocamos a ação de escolher item, para os casos em que o fazendeiro precisa atravessar o rio sem levar nenhum item. Ele precisa decidir se vai levar um item ou não.

  O algorítmo do fazendeiro encontra-se no arquivo [algoritmo_do_fazendeiro.py](algoritmo_do_fazendeiro.py)
