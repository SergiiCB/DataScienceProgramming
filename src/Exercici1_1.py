# coding=utf-8

"""
Mètode utilitzat per resoldre l'exercici
"""

import zipfile

def import_csv_from_zip(zip_file_path, extract_folder):
    """Descomprimeix el fitxer i guarda el seu contingut en la carpeta data del projecte"""
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
        print(f"Fitxer extret a '{extract_folder}'.")