# coding=utf-8

import pytest
from src import Exercici4_2
import tempfile
import os

@pytest.fixture
def sample_dataset():
    return [
        {'sentiment': 'positive', 'id': 1, 'date': '2023-06-18', 'query': 'example', 'user': 'user1', 'text': 'Hello', 'frequency': 5},
        {'sentiment': 'negative', 'id': 2, 'date': '2023-06-19', 'query': 'example', 'user': 'user2', 'text': 'World', 'frequency': 3}
    ]

@pytest.fixture
def create_temp_dir():
    # Crea un directori temporal
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir

def test_save_process_dataset(sample_dataset, create_temp_dir):
    temp_csv = f"{create_temp_dir}/test.csv"
    Exercici4_2.save_process_dataset(sample_dataset, temp_csv)
    assert os.path.exists(temp_csv)

    with open(temp_csv, 'r', encoding='utf-8') as file:
        content = file.read()
    expected = "sentiment,id,date,query,user,text,frequency\npositive,1,2023-06-18,example,user1,Hello,5\nnegative,2,2023-06-19,example,user2,World,3\n"
    assert expected == content




