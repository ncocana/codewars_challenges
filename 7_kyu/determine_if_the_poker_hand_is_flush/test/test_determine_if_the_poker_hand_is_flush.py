# importar el modulo de otro directorio
from src.determine_if_the_poker_hand_is_flush import is_flush
import pytest


@pytest.mark.is_flush
def test_is_flush():
    assert is_flush(["AS", "3S", "9S", "KS", "4S"]) == True
    assert is_flush(["AD", "4S", "7H", "KC", "5S"]) == False
    assert is_flush(["AD", "4S", "10H", "KC", "5S"]) == False
    assert is_flush(["QD", "4D", "10D", "KD", "5D"]) == True
