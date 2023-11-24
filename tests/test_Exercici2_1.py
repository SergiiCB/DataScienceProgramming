# coding=utf-8

import pytest
from src import Exercici2_1

def test_preprocess_dataframe():
    dataframe = [{
        'text': "@switchfoot http://twitpic.com/2y1zl - Awww, that's a bummer.  You shoulda got David Carr of Third Day to do it. ;D"
    }, {
        'text': "is upset that he can't update his Facebook by texting it... and might cry as a result  School today also. Blah!"}]

    expected = [{
        'text': "switchfoot   awww thats a bummer  you shoulda got david carr of third day to do it d"
    }, {
        'text': "is upset that he cant update his facebook by texting it and might cry as a result  school today also blah"}]
    assert Exercici2_1.preprocess_dataframe(dataframe) == expected


def test_preprocess_text():
    text = "-!234 Hello 123 AHDJEW https://google.com ?¿ 中國 ^^"
    expected = "234 hello 123 ahdjew    "

    assert Exercici2_1.preprocess_text(text) == expected

def test_preprocess_text_mayus():
    text = "AHDJEW"
    expected = "ahdjew"

    assert Exercici2_1.preprocess_text(text) == expected

def test_preprocess_text_ascii():
    text = "中國"
    expected = ""
    assert Exercici2_1.preprocess_text(text) == expected

def test_preprocess_text_symbols():
    text = "a-! ?¿ ^^"
    expected = "a  "

    assert Exercici2_1.preprocess_text(text) == expected