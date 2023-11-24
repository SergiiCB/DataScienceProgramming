# coding=utf-8

"""
Mètode utilitzat per resoldre l'exercici
"""

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def get_wordcloud():
    # Carregar el dataset processament
    PROCESSED_FILE_PATH = './data/twitter_processed.csv'
    dataset = pd.read_csv(PROCESSED_FILE_PATH)

    # Pregunta 1: Quants clústers tenim en el nostre dataset?

    get_clusters(dataset['sentiment'])

    # Pregunta 2: Tenim elements buits en les columnes text? Si és així, quin és el percentatge?

    dataset = remove_null_text(dataset)

    # Pregunta 3: Generar word cloud per a cada clúster
    print(f"Pregunta 3: Generar word cloud per a cada clúster")

    clusters = dataset['sentiment'].unique()
    for cluster in clusters:
        # Filtrar tuits per clúster
        tweets_cluster = dataset[dataset['sentiment'] == cluster]['text']

        # Unir els tuits en un sol text
        text_cluster = ' '.join(tweets_cluster)

        # Generar la word cloud
        wordcloud = WordCloud(background_color='white').generate(text_cluster)

        # Mostrar la word cloud
        plt.figure(figsize=(8, 8))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.title(f"Word Cloud - Cluster: {cluster}")
        plt.axis('off')
        plt.show()


def remove_null_text(dataset):
    percentatge_elements_buits = dataset['text'].isnull().sum() / len(dataset['text']) * 100
    print(f"Pregunta 2: Tenim elements buits en les columnes text? Si és així, quin és el percentatge?")
    print(f"Percentatge d'elements buits en la columna 'text': {percentatge_elements_buits:.2f}%")
    # Eliminar elements nuls en la columna 'text'
    dataset = dataset.dropna(subset=['text'])
    return dataset


def get_clusters(column):
    num_clusters = column.nunique()
    print(f"Pregunta 1: Quants clústers tenim en el nostre dataset?")
    print(f"Nombre de clústers en el dataset: {num_clusters}")
    return num_clusters
