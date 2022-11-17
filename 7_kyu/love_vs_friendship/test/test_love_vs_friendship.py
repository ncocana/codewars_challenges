# importar el modulo de otro directorio
from src.love_vs_friendship import words_to_marks
import pytest


@pytest.mark.words_to_marks
def test_words_to_marks():
    assert words_to_marks('attitude') == 100
    assert words_to_marks('friends') == 75
    assert words_to_marks('family') == 66
    assert words_to_marks('selfness') == 99
    assert words_to_marks('knowledge') == 96
