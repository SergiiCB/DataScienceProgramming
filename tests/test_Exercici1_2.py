# coding=utf-8

import tempfile
from src import Exercici1_2
import pytest
import os

def create_temp_csv(data):
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    temp_file.writelines(data)
    temp_file.close()
    return temp_file.name

@pytest.fixture
def create_csv():
    csv_data = [
        "sentiment,id,text\n",
        "000,1,test_text\n",
        "004,2,test_text_2\n",
    ]
    csv_path = create_temp_csv(csv_data)
    yield csv_path
    os.remove(csv_path)


def test_convert_csv_to_dataframe(create_csv):
    expected = [{
        "sentiment": "000",
        "id": "1",
        "text": "test_text"
    }, {
        "sentiment": "004",
        "id": "2",
        "text": "test_text_2"
    }]

    assert Exercici1_2.read_csv_to_dataframe(create_csv) == expected


def test_convert_invalid_path(create_csv):
    invalid_path = "invalid_path"
    assert invalid_path != create_csv
    with pytest.raises(Exception):
        Exercici1_2.read_csv_to_dataframe("invalid_path")