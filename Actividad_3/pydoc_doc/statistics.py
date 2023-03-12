import numpy as np

def media(lista):
    """
    Calcula la media aritmética de una lista de números.

    Args:
        lista: Una lista de números
    Returns:
        La media aritmética de la lista
    """
    media = float(sum(lista))/len(lista)
    return media

def moda(lista):
    """
    Calcula la moda aritmética de una lista de números.

    Args:
        lista: Una lista de números
    Returns:
        La moda aritmética de la lista
    """
    contador = {}
    for x in lista:
        if x in contador.keys():
            contador[x] += 1
        else:
            contador[x] = 1
    moda = max(contador, key=contador.get)

    return moda

def mediana(lista):
    """
    Calcula la mediana de una lista de números.

    Args:
        lista: Una lista de números
    Returns:
        La mediana de la lista
    """
    lista = sorted(lista)

    if len(lista)%2 == 0:
        mediana = 0.5*(lista[int(len(lista)/2) - 1] + lista[int(len(lista)/2)])
    else:
        mediana = lista[int(len(lista)/2)]
    return mediana

def varianza(lista):
    """
    Calcula la varianza de la distribución compuesta por una lista de números.

    Args:
        lista: Una lista de números
    Returns:
        La varianza estadística de la lista
    """
    varianza = 0
    avg = media(lista)
    for x in lista:
        varianza += (x - avg)**2.
    varianza = varianza/len(lista)
    return varianza

def desviacion_tipica(lista):
    """
    Calcula la desviación típica de la distribución de una lista de números.

    Args:
        lista: Una lista de números
    Returns:
        La desviación típica de la lista
    """
    var = varianza(lista)
    desviacion_tipica = np.sqrt(var)
    return desviacion_tipica