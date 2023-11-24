# coding=utf-8

import pytest
from src import Exercici2_2

def test_remove_stop_words():
    dataframe = [{
        "text": "is upset that he cant update his facebook by texting it and might cry as a result  school today also blah"
    }, {
        "text": "you shoulda got david carr of third day to do it"}]

    expected = [{
        "text": "upset cant update facebook texting might cry result school today also blah"
    }, {
        "text": "shoulda got david carr third day"}]

    assert Exercici2_2.remove_stop_words(dataframe) == expected

