import random
import pytest
# from pytest_mock import mocker

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

def test_fail():
    assert pytest.fail('testing pytest.fail', True)

# def test_shuffle_spy():
#     spy = mocker.spy(random, 'shuffle')
#     assert random.shuffle([1,2,3,4,5]) != [1,2,3,4,5], 'list not shuffled'

#     spy.assert_called_once_with([1,2,3,4,5])
#     spy.spy_return != [1,2,3,4,5]

if __name__ == '__main__':
    
    pytest.main()
