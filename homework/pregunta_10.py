"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        data = []
        for line in file:
            parts = line.strip().split("\t")
            col1 = parts[0]
            col4 = parts[3].split(",") if parts[3] else []
            col5 = parts[4].split(",") if parts[4] else []
            count_col4 = len(col4)
            count_col5 = len(col5)
            data.append((col1, count_col4, count_col5))
    return data