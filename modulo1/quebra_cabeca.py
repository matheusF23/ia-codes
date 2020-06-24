
def heuristica(estado):
    manhattan = 0
    for i, linha in enumerate(estado):
        for col, valor in enumerate(linha):
            for n in range(9):
                if(valor == n):
                    linhaAtual = i
                    colunaAtual = col
                    linhaCorreta = int(valor / 3)
                    colunaCorreta = valor % 3
                    manhattan += abs(linhaAtual - linhaCorreta) + \
                        abs(colunaAtual - colunaCorreta)
    return manhattan


def testa_borda(filho, borda):
    """Verifica se o nó está na borda"""
    existeNaBorda = False
    for i in range(len(borda)):
        if filho == borda[i][0][-1]:
            existeNaBorda = True
            break
    return existeNaBorda


def teste_objetivo(estado, estadoObjetivo):
    """Verifica se o objetivo foi alcançado"""
    return estado == estadoObjetivo


def cria_borda_ordenada(borda, novoCaminho):
    """ordena a borda em ordem crescente de custo"""
    for indice, caminho in enumerate(borda):
        if (novoCaminho[1] <= caminho[1]):
            # É preciso adicionar o novo caminho no indice ao qual ele tem um
            # custo menor, para isso separamos a borda em duas e colocamos o
            # novo caminho no meio
            ladoEsquerdoDaBorda = borda[:indice]
            ladoDireitoDaBorda = borda[indice:]
            novaBorda = ladoEsquerdoDaBorda + \
                [novoCaminho] + ladoDireitoDaBorda
            return novaBorda
    novaBorda = borda[:] + [novoCaminho]
    return novaBorda


def acoes(estado):
    """Recebe um estado e retorna as ações possiveis"""
    linha1 = estado[0]
    linha2 = estado[1]
    linha3 = estado[2]
    if (0 in linha1):
        for indice, valor in enumerate(linha1):
            if(valor == 0):
                if(indice == 0):
                    return ['baixo', 'direita']
                elif(indice == 1):
                    return ['baixo', 'esquerda', 'direita']
                else:
                    return ['baixo', 'esquerda']
    elif (0 in linha2):
        for indice, valor in enumerate(linha2):
            if(valor == 0):
                if(indice == 0):
                    return ['baixo', 'direita', 'cima']
                elif(indice == 1):
                    return ['baixo', 'esquerda', 'direita', 'cima']
                else:
                    return ['baixo', 'esquerda', 'cima']
    elif (0 in linha3):
        for indice, valor in enumerate(linha3):
            if(valor == 0):
                if(indice == 0):
                    return ['cima', 'direita']
                elif(indice == 1):
                    return ['cima', 'esquerda', 'direita']
                else:
                    return ['cima', 'esquerda']


def no_filho(estado, acao):
    """Recebe um estado e uma ação e retorna o estado resultante dessa ação"""
    linha1 = estado[0].copy()
    linha2 = estado[1].copy()
    linha3 = estado[2].copy()
    filho = [linha1, linha2, linha3]
    if (0 in linha1):
        for indice, valor in enumerate(linha1):
            if(valor == 0):
                if(acao == 'baixo'):
                    linha1[indice], linha2[indice] = linha2[indice], linha1[indice]
                    return filho
                elif(acao == 'esquerda'):
                    linha1[indice], linha1[indice -
                                           1] = linha1[indice - 1], linha1[indice]
                    return filho
                elif(acao == 'direita'):
                    linha1[indice], linha1[indice +
                                           1] = linha1[indice + 1], linha1[indice]
                    return filho
    elif (0 in linha2):
        for indice, valor in enumerate(linha2):
            if(valor == 0):
                if(acao == 'baixo'):
                    linha3[indice], linha2[indice] = linha2[indice], linha3[indice]
                    return filho
                elif(acao == 'cima'):
                    linha1[indice], linha2[indice] = linha2[indice], linha1[indice]
                    return filho
                elif(acao == 'esquerda'):
                    linha2[indice], linha2[indice -
                                           1] = linha2[indice - 1], linha2[indice]
                    return filho
                elif(acao == 'direita'):
                    linha2[indice], linha2[indice +
                                           1] = linha2[indice + 1], linha2[indice]
                    return filho
    elif (0 in linha3):
        for indice, valor in enumerate(linha3):
            if(valor == 0):
                if(acao == 'cima'):
                    linha3[indice], linha2[indice] = linha2[indice], linha3[indice]
                    return filho
                elif(acao == 'esquerda'):
                    linha3[indice], linha3[indice -
                                           1] = linha3[indice - 1], linha3[indice]
                    return filho
                elif(acao == 'direita'):
                    linha3[indice], linha3[indice +
                                           1] = linha3[indice + 1], linha3[indice]
                    return filho


def testa_custo(filho, borda, novoCaminho):
    """Verifica se o estado do filho tem um custo menor que um possivel
    mesmo estado presente na borda"""
    for i in range(len(borda)):
        if filho == borda[i][0][-1] and novoCaminho[1] < borda[i][1]:
            borda[i] = novoCaminho
            break


def quebra_cabeca(estadoInicial, estadoObjetivo):
    """Resolve o problema do quebra-cabeças usando o algorítmo de busca A*"""
    no = estadoInicial
    borda = [no]
    explorado = []

    while True:
        if (len(borda) == 0):
            break

        no = borda.pop(0)   # Escolhe o nó com menor custo

        if (teste_objetivo(no[0][-1], estadoObjetivo)):
            return no

        explorado.append(no[0][-1])

        for acao in acoes(no[0][-1]):
            filho = no_filho(no[0][-1], acao)
            custo = len(no[0]) + heuristica(filho)
            novoCaminho = [no[0] + [filho], custo]
            if (not testa_borda(filho, borda) or filho not in explorado):
                borda = cria_borda_ordenada(borda, novoCaminho)
            else:
                testa_custo(filho, borda, novoCaminho)


estadoInicial = [[
    [
        [7, 2, 4],
        [5, 0, 6],
        [8, 3, 1]
    ]
], 0]

estadoObjetivo = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

resultado = quebra_cabeca(estadoInicial, estadoObjetivo)

if (resultado):
    print(f'Custo do caminho: {resultado[1]}')
    for estado in resultado[0]:
        for linha in estado:
            print(linha)
        print()
else:
    print('Não consegui achar solução')
