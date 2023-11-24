# coding=utf-8

from src import Exercici6
import pandas as pd

def test_get_top_20():
    data = {f"test_{i}": i for i in range(10, 30)}
    expected = {f"test_{i}": i for i in range(29, 9, -1)}
    assert Exercici6.get_top_20(data) == expected


def test_flatten_dictonary():
    data = pd.DataFrame()
    data['frequency'] = [
        {'test1': 1, 'test2': 2, 'test3': 3},
        {'a': 1, 'b': 2, 'c': 3},
        {'a': 1, 'b': 2, 'c': 3}
    ]

    expected = {'test1': 1, 'test2': 2, 'test3': 3, 'a': 2, 'b': 4, 'c': 6}
    assert Exercici6.flatten_dictionary(data) == expected