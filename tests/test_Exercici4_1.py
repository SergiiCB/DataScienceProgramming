# coding=utf-8

import pytest
from src import Exercici4_1
@pytest.fixture
def dataset():
    return [{"text": f"test {i}"} for i in range(30)]
@pytest.fixture
def frequencies():
    return [{"a": 10, "b": i} for i in range(30)]
def test_append_frequencies(dataset, frequencies):
    dataset = Exercici4_1.append_frequencies(dataset, frequencies)
    assert dataset[0]["frequency"] == {"a": 10, "b": 0}
    assert dataset[29]["frequency"] == {"a": 10, "b": 29}
