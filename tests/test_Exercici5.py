# coding=utf-8

import pytest
import pandas as pd
from src import Exercici5
from pandas.testing import assert_frame_equal

@pytest.fixture
def get_dataframe():
    dataframe = pd.DataFrame({
        'text': ['test1', None, 'test2', 'test3'],
        'sentiment': [0, 1, 1, 4]
    })
    return dataframe

def test_remove_null_text(get_dataframe):
    expected = pd.DataFrame({
        'text': ['test1', 'test2', 'test3'],
        'sentiment': [0, 1, 4]
    })
    result = Exercici5.remove_null_text(get_dataframe)
    assert_frame_equal(
        result.reset_index(drop=True),
        expected.reset_index(drop=True)
    )

def test_get_clusters(get_dataframe):
    expected = pd.DataFrame({
        'sentiment': [0, 1, 4]
    })
    result = Exercici5.get_clusters(get_dataframe['sentiment'])
    print(f"result {result}")

    assert result == len(expected['sentiment'])