def test_add(): assert 1 + 1 == 2
def test_zero_division():
    try:
        _ = 1 / 0
    except ZeroDivisionError:
        assert True
    else:
        assert False, "Expected ZeroDivisionError"