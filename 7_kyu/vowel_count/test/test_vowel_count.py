# importar el modulo de otro directorio
from src.vowel_count import get_count
import pytest


@pytest.mark.all_vowels
def test_all_vowels():
    assert get_count("aeiou") == 5
    assert get_count("abracadabra") == 5
        
@pytest.mark.only_y
def test_only_y():
    assert get_count("y") == 0    
        
@pytest.mark.no_vowels
def test_no_vowels():
    assert get_count("bcdfghjklmnpqrstvwxz y") == 0
    assert get_count("") == 0