""" Función que recibe un string de números separados por "," y los suma
"""

def sumar(numeros):
    """ Recibo x cantidad de números mediante un string, divido dicho str utilizando un split
    e itero por cada número recibido para sumarlo a un acumulador que dará el resultado final

    Args:
        numeros (str): String de números a sumarcd 

    Returns:
        float: Resultado de la suma de numeros provenientes del string
    """

    # Defino e inicializo en 0 un acumulador
    suma = 0

    # Splitteo el string de numeros, en una lista tomando como separador el caracter ","
    numeros = numeros.split (",")

    # Itero por cada número en la lista de números
    for element in numeros:

        # Acumulo en suma casteando a integer el numero que está en str
        suma = suma + float(element)

    # Devuelvo la suma realizada en el acumulador
    return suma

# Invoco la función sumar enviado como argumento str de numeros separados por ","
respuesta = sumar("51,2,43,7,23")

# Muestro en pantalla la respuesta utilizando un f-string
print(f"La respuesta es: {respuesta}")
