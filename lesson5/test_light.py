import lesson5.divisor_master as dm
import pytest

n = 100

@pytest.fixture()
def number():
    return n

@pytest.fixture()
def simple_numbers():
    return dm.simple_numbers_list(n)

def test_simple_numbers_list(simple_numbers):
    assert 13 in simple_numbers

def test_is_simple_number(simple_numbers):
    assert dm.is_simple_number(simple_numbers.pop())

def test_dividers(number, simple_numbers):
    assert len(dm.dividers(number, simple_numbers)) > 2

def test_simple_multipliers(number, simple_numbers):
    assert type(dm.simple_multipliers(number, simple_numbers)) == str

def test_max_simple_divider(number, simple_numbers):
    divs = dm.dividers(number, simple_numbers)
    assert dm.max_simple_divider(simple_numbers, divs) != number
