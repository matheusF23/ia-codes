'''
1 = graos
2 = raposa
3 = galinha
'''


def testa_borda(filho, borda):
    """Verifica se o nó está na borda"""
    existeNaBorda = False
    for i in range(len(borda)):
        if filho == borda[i][0][-1]:
            existeNaBorda = True
            break
    return existeNaBorda


def teste_objetivo(estado):
    """Verifica se o objetivo foi alcançado"""
    return estado == [1, 1, 2, 3, 0, 0, 0, 0]


def acoes(estado):
    """Recebe um estado e retorna as ações possiveis"""
    # [1,0,0,3,0,1,2,0]
    margemDireita = estado[5:]
    margemEsquerda = estado[1:4]
    estadosImpossiveis = [[1, 2, 3], [1, 0, 3], [0, 2, 3]]

    if (margemDireita in estadosImpossiveis and estado[4] == 1):
        return ['escolheItem', 'atravessa']
    elif(margemEsquerda in estadosImpossiveis and estado[0] == 1):
        return ['escolheItem', 'atravessa']
    elif (margemDireita not in estadosImpossiveis and estado[4] == 1):
        return ['escolheItem', 'atravessa']
    elif(margemEsquerda not in estadosImpossiveis and estado[0] == 1):
        return ['atravessa']


def atravessa(estado, inicioItem, destinoItem):
    novoEstado = estado.copy()
    novoEstado[0], novoEstado[4] = novoEstado[4], novoEstado[0]
    novoEstado[destinoItem], novoEstado[inicioItem] = novoEstado[inicioItem], novoEstado[destinoItem]

    return novoEstado


def no_filho(no, item, explorado):
    estadosImpossiveis = [[1, 2, 3], [1, 0, 3], [0, 2, 3]]

    estado = no[0][-1].copy()
    if (item == 0):
        estado[0], estado[4] = estado[4], estado[0]
        return estado
    if (estado[4] == 1):
        for i in range(3):
            posicaoItem = i + 5
            if (estado[posicaoItem] == i + 1):
                novoEstado = atravessa(estado, posicaoItem, i + 1)
                if (novoEstado[5:] not in estadosImpossiveis and novoEstado not in explorado):
                    return novoEstado
    if (estado[0] == 1):
        for i in range(3):
            posicaoItem = i + 1
            if (estado[posicaoItem] == i + 1):
                novoEstado = atravessa(estado, posicaoItem, i + 5)
                if (novoEstado[1:4] not in estadosImpossiveis and novoEstado not in explorado):
                    return novoEstado


def ajuda_fazendeiro(estadoInicial):
    """Executa o algoritmo de busca em largura"""
    no = estadoInicial

    if(teste_objetivo(no[0])):
        return no

    borda = [no]
    explorado = []
    acheiSolucao = False

    while not acheiSolucao:
        if (len(borda) == 0):
            break
        no = borda.pop(0)
        explorado.append(no[0][-1])

        item = 0    # Para decidir se e qual item escolher
        for acao in acoes(no[0][-1]):
            if (acao == 'escolheItem'):
                item = 1
            elif (acao == 'atravessa'):
                filho = no_filho(no, item, explorado)
                if (not filho in explorado and not testa_borda(filho, borda)):
                    if teste_objetivo(filho):
                        no[0].append(filho)
                        no[1] += 1
                        acheiSolucao = True
                        break
                    borda.append([no[0] + [filho], no[1] + 1])

    if (acheiSolucao is True):
        return no
    return False


# estadoInicial = [['0000 1123'], 0]  # Estado inicial com custo do caminho
estadoInicial = [[[0, 0, 0, 0, 1, 1, 2, 3]], 0]

resposta = ajuda_fazendeiro(estadoInicial)
if resposta:
    print(f'Quantidade de passos: {resposta[1]}')
    for i, v in enumerate(resposta[0]):
        for indice, valor in enumerate(v):
            if (indice != 0 and indice != 4):
                if(valor == 1):
                    v[indice] = 'grão'
                if(valor == 2):
                    v[indice] = 'raposa'
                if(valor == 3):
                    v[indice] = 'galinha'
            else:
                if (valor == 1):
                    v[indice] = 'fazendeiro'
        print(
            f'etapa: {i}\n',
            f'\tmargem esquerda: {v[:4]}\n',
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n',
            f'\tmargem direita: {v[4:]}\n'
        )
