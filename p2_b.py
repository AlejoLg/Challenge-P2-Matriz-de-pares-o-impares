


def matriz_pares(lista_de_listas):    

    # Itero y enumero por cada lista en la lista de listas
    for posl, l in enumerate(lista_de_listas):

        # Itero y enumero por cada numero en la lista de numeros 
        for posn, n in enumerate(l):

            # Chequeo si el número es par (divisible por 2 con resto 0)
            if n%2==0:

                # Si es, reemplazo en la posición de la lista y en la posición del número por True
                lista_de_listas[posl][posn] = True
   
            else:
            
                # Si no es, reemplazo en la posición de la lista y en la posición del número por False 
                lista_de_listas[posl][posn] = True

    #Devuelvo la lista_de_listas sobreescrita 
    return lista_de_listas

# Le asigno un valor a la variable lista_de_listas
lista_de_listas=[ [ 1,2,3], [2,3,4],[4,5,6] ]

# Invoco a la función matriz_pares enviando como argumento una lista de listas de ejemplo
lista_nueva = matriz_pares(lista_de_listas)

# Muestro por pantalla el resultado devuelto por la función matriz_pares
print(lista_nueva)
