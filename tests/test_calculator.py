import pytest
from calculator import Calculator


@pytest.mark.parametrize('a,b,expected', [(2,3,5), (-2,-3,-5), (-2,3,1), (0,0,0), (0.1,0.2,0.3)])
def test_add(a,b,expected):
    assert Calculator.add(a,b) == pytest.approx(expected)


@pytest.mark.parametrize('a,b,expected', [(10,2,5), (-10,2,-5), (0,4,0), (1,4,0.25)])
def test_divide(a,b,expected):
    assert Calculator.divide(a,b) == pytest.approx(expected)


@pytest.mark.parametrize('a,b', [(1,0), (0,0), (-1,0.0)])
def test_divide_by_zero(a,b):
    with pytest.raises(ZeroDivisionError, match='Деление на ноль'):
        Calculator.divide(a,b)


@pytest.mark.parametrize('number,expected', [(-7,False),(0,False),(1,False),(2,True),(3,True),(4,False),(17,True),(25,False),(97,True)])
def test_is_prime(number,expected):
    assert Calculator.is_prime_number(number) is expected


@pytest.mark.parametrize('invalid', [1.5, '7', True])
def test_prime_rejects_non_integer(invalid):
    with pytest.raises(TypeError, match='целое число'):
        Calculator.is_prime_number(invalid)
