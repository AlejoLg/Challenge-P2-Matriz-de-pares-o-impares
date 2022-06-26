""" Función que recibe una lista de listas y devuelve una del mismo tamaño pero con Booleanos,
True si el número es par y False si es impar
"""


def matriz_pares(lista_de_listas):
    """ Recibo una lista de listas, itero cada lista y luego cada numero dentro de esas listas.
    si el número es divisible por dos (tiene resto 0) le asigno un True en una nueva lista, sinó False.

    Args:
        lista_de_listas (str): Lista de listas de números entrantes.

    Returns:
        string: Lista nueva de números representados como True si son par o False si son Impar
    """
    # Defino una lista en la que se agregarán las listas nuevas
    lista_nueva = []

    # Itero por cada lista dentro de la lista de listas
    for l in lista_de_listas:

        # Defino una lista vacía para agregar los booleanos
        lista = []

        # Itero por cada número de la lista de números
        for n in l:

            # Chequeo si el número es par (divisible por 2 con resto 0)
            if n%2==0:
                lista.append(True)
            
            # Si es impar
            else:
                lista.append(False)

        # Agrego la nueva lista de booleanos a la lista de listas creada previamente
        lista_nueva.append(lista)

    # Devuelvo la nueva lista de listas
    return lista_nueva

# Invoco a la función matriz_pares enviando como argumento una lista de listas de ejemplo
lista_nueva = matriz_pares(lista_de_listas=[[1,2,3],[2,3,4],[4,5,6]])

# Muestro por pantalla el resultado devuelto por la función matriz_pares
print(lista_nueva)

