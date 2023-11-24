# coding=utf-8

"""
Mètode utilitzat per resoldre l'exercici
"""

import matplotlib.pyplot as plt
import pandas as pd
import heapq


def get_top_20(dictionary):
    # Obté el top 20
    top_items = heapq.nlargest(20, dictionary, key=dictionary.get)
    return {key: dictionary[key] for key in top_items}


def flatten_dictionary(dataframe):
    flatten_dict = {}
    print(dataframe)
    for frequency in dataframe['frequency']:
        for key, value in frequency.items():
            flatten_dict[key] = value if key not in flatten_dict else value + flatten_dict[key]
    return flatten_dict


def generate_histogram(dataframe):
    """Genera un histograma amb els valors obtinguts en l'exercici 3"""
    dataframe = pd.DataFrame(dataframe)
    for cluster in dataframe['sentiment'].unique():
        flatten_dict = {}
        filtered_dataframe = dataframe[dataframe['sentiment'] == cluster]
        for frequency in filtered_dataframe['frequency']:
            for key, value in frequency.items():
                flatten_dict[key] = value if key not in flatten_dict else value + flatten_dict[key]

        flatten_dict = flatten_dictionary(filtered_dataframe)
        filtered_results = get_top_20(flatten_dict)

        plt.bar(list(filtered_results.keys()), filtered_results.values(), color='g')
        plt.bar(
            list(filtered_results.keys()),
            filtered_results.values(),
            color='g'
        )
        plt.show()