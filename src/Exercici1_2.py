# coding=utf-8

"""
Mètode utilitzat per resoldre l'exercici
"""

import csv

def read_csv_to_dataframe(csv_path):
    """Llegeix el fitxer i carrega el dataset com una llista de diccionaris"""
    dataframe = []
    # Cada fila del fitxer original correspon amb un diccionari
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dataframe.append(row)
    # Mostra els 5 primers registres del dataset
    print(dataframe[:5])
    return dataframe