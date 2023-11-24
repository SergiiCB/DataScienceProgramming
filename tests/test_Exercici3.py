# coding=utf-8

import pytest
from src import Exercici3


def test_process_words():
    dataframe = [{
        'text': "programació la llengua universal de les màquines"
    }, {
        'text': "codi que transforma i transforma amb cada línia i cada línia crea i crea noves possibilitats"}]

    assert Exercici3.process_words(dataframe)


def test_update_frequency():
    word = "transforma"
    frequency = {"transforma": 2, "codi": 1, "universal": 1}
    assert Exercici3.update_frequency(word, frequency) == 3


def test_update_frequency_not_existing():
    word = "test"
    frequency = {"transforma": 2, "codi": 1, "universal": 1}
    assert Exercici3.update_frequency(word, frequency) == 1

