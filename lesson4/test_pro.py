from lesson4.home_work import F, sample_names
from functools import reduce


def test_one():
    assert 'Anna' in F(sample_names, 10)

def test_two():
    assert reduce(lambda x, y: len(x) + len(y) if type(x) == str else x + len(y), F(sample_names, 15)) > 100
