def heuristica(estado):
    linha1 = estado[0]
    linha2 = estado[1]
    linha3 = estado[2]
    contador = 0
    for i, valor in enumerate(linha1):
        if (i == 0):
            if(valor == 1):
                contador += 1
                continue
            if(valor == 2):
                contador += 2
                continue
            if(valor == 3):
                contador += 1
                continue
            if(valor == 4):
                contador += 2
                continue
            if(valor == 5):
                contador += 3
                continue
            if(valor == 6):
                contador += 2
                continue
            if(valor == 7):
                contador += 3
                continue
            if(valor == 8):
                contador += 4
                continue
        if (i == 1):
            if(valor == 0):
                contador += 1
                continue
            if(valor == 2):
                contador += 1
                continue
            if(valor == 3):
                contador += 2
                continue
            if(valor == 4):
                contador += 1
                continue
            if(valor == 5):
                contador += 2
                continue
            if(valor == 6):
                contador += 3
                continue
            if(valor == 7):
                contador += 2
                continue
            if(valor == 8):
                contador += 3
                continue
        if (i == 2):
            if(valor == 0):
                contador += 2
                continue
            if(valor == 1):
                contador += 1
                continue
            if(valor == 3):
                contador += 3
                continue
            if(valor == 4):
                contador += 2
                continue
            if(valor == 5):
                contador += 1
                continue
            if(valor == 6):
                contador += 4
                continue
            if(valor == 7):
                contador += 3
                continue
            if(valor == 8):
                contador += 2
                continue

    for i, valor in enumerate(linha2):
        if (i == 0):
            if(valor == 0):
                contador += 1
                continue
            if(valor == 1):
                contador += 2
                continue
            if(valor == 2):
                contador += 3
                continue
            if(valor == 4):
                contador += 1
                continue
            if(valor == 5):
                contador += 2
                continue
            if(valor == 6):
                contador += 1
                continue
            if(valor == 7):
                contador += 2
                continue
            if(valor == 8):
                contador += 3
                continue
        if (i == 1):
            if(valor == 0):
                contador += 2
                continue
            if(valor == 1):
                contador += 1
                continue
            if(valor == 2):
                contador += 2
                continue
            if(valor == 3):
                contador += 1
                continue
            if(valor == 5):
                contador += 1
                continue
            if(valor == 6):
                contador += 2
                continue
            if(valor == 7):
                contador += 1
                continue
            if(valor == 8):
                contador += 2
                continue
        if (i == 2):
            if(valor == 0):
                contador += 3
                continue
            if(valor == 1):
                contador += 2
                continue
            if(valor == 2):
                contador += 1
                continue
            if(valor == 3):
                contador += 2
                continue
            if(valor == 4):
                contador += 1
                continue
            if(valor == 6):
                contador += 3
                continue
            if(valor == 7):
                contador += 2
                continue
            if(valor == 8):
                contador += 1
                continue
    for i, valor in enumerate(linha3):
        if (i == 0):
            if(valor == 0):
                contador += 2
                continue
            if(valor == 1):
                contador += 3
                continue
            if(valor == 2):
                contador += 4
                continue
            if(valor == 3):
                contador += 1
                continue
            if(valor == 4):
                contador += 2
                continue
            if(valor == 5):
                contador += 3
                continue
            if(valor == 7):
                contador += 1
                continue
            if(valor == 8):
                contador += 2
                continue
        if (i == 1):
            if(valor == 0):
                contador += 3
                continue
            if(valor == 1):
                contador += 2
                continue
            if(valor == 2):
                contador += 3
                continue
            if(valor == 3):
                contador += 2
                continue
            if(valor == 4):
                contador += 1
                continue
            if(valor == 5):
                contador += 2
                continue
            if(valor == 6):
                contador += 1
                continue
            if(valor == 8):
                contador += 1
                continue
        if (i == 2):
            if(valor == 0):
                contador += 4
                continue
            if(valor == 1):
                contador += 3
                continue
            if(valor == 2):
                contador += 2
                continue
            if(valor == 3):
                contador += 3
                continue
            if(valor == 4):
                contador += 2
                continue
            if(valor == 5):
                contador += 1
                continue
            if(valor == 6):
                contador += 2
                continue
            if(valor == 7):
                contador += 1
                continue
    return contador
