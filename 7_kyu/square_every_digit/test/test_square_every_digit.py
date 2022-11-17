# importar el modulo de otro directorio
from src.square_every_digit import square_digits
import pytest


@pytest.mark.square_digits
def test_square_digits():
    assert square_digits(9119) == 811181
    assert square_digits(0) == 0