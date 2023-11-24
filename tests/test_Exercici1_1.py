# coding=utf-8

import tempfile
import os
import zipfile
import pytest
from src import Exercici1_1

@pytest.fixture
def csv_zip_file():
    # Crea un directori temporal
    with tempfile.TemporaryDirectory() as temp_dir:
        # Defineix el contingut del fitxer CSV
        csv_data = [
            "sentiment,id,text\n",
            "000,1,test_text\n",
            "004,2,test_text_2\n",
        ]

        # Crea el fitxer CSV dins del directori temporal
        csv_file_path = os.path.join(temp_dir, "data.csv")
        with open(csv_file_path, "w") as csv_file:
            csv_file.writelines(csv_data)

        # Crea el fitxer ZIP i afegeix el fitxer CSV
        zip_file_path = os.path.join(temp_dir, "data.zip")
        with zipfile.ZipFile(zip_file_path, "w") as zip_file:
            zip_file.write(csv_file_path, "data.csv")

        # Retorna el path del fitxer ZIP i el path del directori temporal
        yield zip_file_path, temp_dir


def test_import_csv_from_zip(csv_zip_file):
    zip_path, folder = csv_zip_file
    Exercici1_1.import_csv_from_zip(zip_path, folder)

    extracted_file_path = os.path.join(folder, "data.csv")
    assert os.path.exists(extracted_file_path)

    with open(extracted_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    expected = "sentiment,id,text\n000,1,test_text\n004,2,test_text_2\n"

    assert content == expected
