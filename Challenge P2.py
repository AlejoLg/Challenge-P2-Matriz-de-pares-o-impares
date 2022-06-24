


def matriz_pares(lista_de_listas):    
    matriz_nueva = []
    for l in lista_de_listas:
        matriz_chica = []
        for n in l:
            if n%2==0:
                matriz_chica.append(True)
            else:
                matriz_chica.append(False)
        matriz_nueva.append(matriz_chica)

    return matriz_nueva
    
    
matriz_nueva = matriz_pares(lista_de_listas=[ [1,2,3],[2,3,4],[4,5,6],[1,2,3],[2,3,4],[4,5,6]])
print(matriz_nueva)

