# coding=utf-8

"""
Mètode utilitzat per resoldre l'exercici
"""

def append_frequencies(dataset, frequencies):
    """Mostra l'element 20 del dataset amb el seu diccionari de freqüències"""
    for i, data in enumerate(dataset):
        data["frequency"] = frequencies[i]
    print(dataset[20])
    return dataset