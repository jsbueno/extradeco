import pytest

import extradeco

# not using a fixture for the decorator due to the use of the non-local mechanism
# to check the decorator actuation.

def test_works_with_no_parameters():
    f_args = None
    @extradeco.parametrized
    def logger(func, *args, **kw):
        nonlocal f_args
        f_args = args
        return func(*args, **kw)

    @logger()
    def s(a,b):
        return a + b

    s(2, 3)
    assert f_args == (2, 3)

def test_works_with_optional_parameters_not_passed():
    f_args = None
    @extradeco.parametrized
    def logger(func, d, e=1, f=2, *args, **kw):
        nonlocal f_args
        f_args = d, e, f
        return func(*args, **kw)

    @logger(0)
    def s(a,b): return a + b

    s(10, 20)
    assert f_args == (0, 1, 2)

def test_works_with_optional_parameters_partially_passed():
    f_args = None
    @extradeco.parametrized
    def logger(func, d, e=1, f=2, *args, **kw):
        nonlocal f_args
        f_args = d, e, f
        return func(*args, **kw)

    @logger(5, 10)
    def s(a,b): return a + b

    s(10, 20)
    assert f_args == (5, 10, 2)

def test_works_with_optional_parameters_fully_passed():

    f_args = None
    @extradeco.parametrized
    def logger(func, d, e=1, f=2, *args, **kw):
        nonlocal f_args
        f_args = d, e, f
        return func(*args, **kw)


    @logger(5, 10, 15)
    def s(a,b): return a + b

    s(10, 20)
    assert f_args == (5, 10, 15)

def test_raises_with_mandatory_parameter_missing():

    f_args = None
    @extradeco.parametrized
    def logger(func, d, e=1, f=2, *args, **kw):
        nonlocal f_args
        f_args = d, e, f
        return func(*args, **kw)

    with pytest.raises(TypeError):
        @logger()
        def s(a,b): return a + b

def test_raises_with_more_parameters_than_acceptable():
    f_args = None
    @extradeco.parametrized
    def logger(func, d, e=1, f=2, *args, **kw):
        nonlocal f_args
        f_args = d, e, f
        return func(*args, **kw)

    with pytest.raises(TypeError):
        @logger(1,2,3,4)
        def s(a,b): return a + b
