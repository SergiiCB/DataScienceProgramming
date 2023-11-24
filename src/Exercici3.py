# coding=utf-8

"""
Mètode utilitzat per resoldre l'exercici
"""

def process_words(dataframe):
    frequencies = []
    vocabulary = set()
    for register in dataframe:
        words = register['text'].split()
        frequency = {}
        for word in words:
            frequency[word] = update_frequency(word, frequency)
            vocabulary.add(word)
        frequencies.append(frequency)
    # Mostra els 5 primers elements de la llista de freqüències
    print("Primers 5 elements de la llista de freqüències:")
    for frequency in frequencies[:5]:
        print(frequency)

    # Ordenar alfabèticament el vocabulari i mostrar les 10 primeres paraules
    sorted_vocabulary = sorted(list(vocabulary))
    print("Primeres 10 paraules del vocabulari:")
    for word in sorted_vocabulary[:10]:
        print(word)
    return frequencies

def update_frequency(word, frequency):
    return frequency.get(word, 0) + 1

