from calculator import is_even, multiply


def test_multiply_positive_numbers() -> None:
    assert multiply(3, 4) == 12


def test_multiply_negative_number() -> None:
    assert multiply(-2, 3) == -6


def test_is_even() -> None:
    assert is_even(8) is True
