# importar el modulo de otro directorio
from src.string_ends_with import solution
import pytest


@pytest.mark.string_ends_with
def test_string_ends_with():
    assert solution('abcde', 'cde') == True
    assert solution('abcde', 'abc') == False
    assert solution('abcde', '') == True