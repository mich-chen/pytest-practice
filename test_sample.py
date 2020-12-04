import random
import pytest
# from pytest_mock import mocker

# *************** Pytest Assertions ***************
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4


# *************** Pytest Failure Tests ***************

def test_fail_true():
    """Failure includes traceback."""
    assert pytest.fail('testing pytest.fail', True)

def test_fail_false():
    """No traceback, only lists test name in failure summary."""
    assert pytest.fail('testing pytest.fail', False)


# *************** Pytest.raises: expected exceptions and errors ***************

def test_raise_pass():
    """Pass == correctly raises exception/error."""

    with pytest.raises(ZeroDivisionError):
        1/0 # pass

def test_raise_fail():
    """Fail == expression does not raise exception/error."""

    with pytest.raises(ZeroDivisionError):
        1/1 # fail


# *************** Pytest Mocker Spy ***************

# def test_shuffle_spy():
#     spy = mocker.spy(random, 'shuffle')
#     assert random.shuffle([1,2,3,4,5]) != [1,2,3,4,5], 'list not shuffled'

#     spy.assert_called_once_with([1,2,3,4,5])
#     spy.spy_return != [1,2,3,4,5]


if __name__ == '__main__':
    
    pytest.main()
