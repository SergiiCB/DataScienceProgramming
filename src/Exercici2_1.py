# coding=utf-8

"""
Mètode utilitzat per resoldre l'exercici
"""

import re


def preprocess_dataframe(dataframe):
    """Realitza un preprocessament fent ús d'expressions regulars"""
    for data in dataframe:
        data['text'] = preprocess_text(data['text'])
    return dataframe


def preprocess_text(text):
    # Elimina URLs
    text = re.sub(r'http\S+|https\S+', '', text)
    text = re.sub(r'(?<!\S)www(?!\\.)\S+', '', text)

    # Elimina caràcters especials no ASCII
    text = re.sub(r'[^\x00-\x7F]+', '', text)

    # Elimina símbols
    text = re.sub(r'[^\w\s]', '', text)

    # Converteix a minúscules
    text = text.lower()
    return text