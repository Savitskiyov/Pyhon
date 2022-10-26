#import pytest
import pytest

from utils import division

# def test_division_good():
#     assert division(10, 2) == 4

# Декораторы
@pytest.mark.parametrize('a, b, expected_result', [(10, 2, 5),
                                                   (10, 5, 2),
                                                   (12, 3, 4),
                                                   (10, 10, 1),
                                                   (10, -5, -2),
                                                   (5, 2, 2.5)])

 

def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)

