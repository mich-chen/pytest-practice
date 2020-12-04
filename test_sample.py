import random
import pytest
from pytest_mock import mocker

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

def test_execinfo():
    """excinfo == ExceptionInfo instance.

    attributes include:
        .type
        .value
        .traceback

    can have access to actual exception. See example below."""

    with pytest.raises(RuntimeError) as excinfo:

        def func():
            func()
        func()

    assert 'maximum recursion' in str(excinfo.value) # fail
    # assert 'min recursion' in str(excinfo.value) # pass

def valueError():
    """Define ValueError exception with specific string representation"""
    raise ValueError('Testing ValueError raised')

def test_valueError():
    """Test matching: test regex matches string representation of exception"""

    with pytest.raises(ValueError, match=r".* ValueError .*"):
        valueError()


# *************** Defining own explanation for failed assertions via hooks in conftest.py ***************

def test_assertrepr_compare():
    l = 1
    r = 2
    assert l == r


# *************** Pytest Mocker Spy ***************

def test_shuffle_patch(mocker):
    mocker.patch('random.shuffle', side_effect=lambda x: x.reverse())
    lst = [1,2,3,4,5]
    random.shuffle(lst)

    random.shuffle.assert_called_once_with(lst)
    assert lst == [5,4,3,2,1], 'shuffle did not shuffle in place'


if __name__ == '__main__':
    
    pytest.main()
