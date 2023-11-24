# coding=utf-8

"""
Mètode utilitzat per resoldre l'exercici
"""

import csv

def save_process_dataset(dataset, file_path):
    """Guarda el dataset processat en un arxiu CSV"""
    with open(file_path, 'w', newline='', encoding='utf-8') as arxiu:
        noms_columnes = ['sentiment', 'id', 'date', 'query', 'user', 'text', 'frequency']
        arxiu_csv = csv.DictWriter(arxiu, fieldnames=noms_columnes)
        arxiu_csv.writeheader()
        arxiu_csv.writerows(dataset)

    print(f"L'arxiu '{file_path}' s'ha guardat correctament.")