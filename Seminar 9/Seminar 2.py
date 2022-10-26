import pytest
from my_sequence import num_sequence

list_example = [(5, 11.55), (6, 14.07)]


@pytest.mark.parametrize('a, expected_result', list_example)
def test_num_sequence_good(a, expected_result):
    assert num_sequence(a) == expected_result


@pytest.mark.parametrize('expected_exception, x', [(TypeError, '2')])
def test_num_sequence_good(expected_exception, x):
    with pytest.raises(expected_exception):
        num_sequence(x)
