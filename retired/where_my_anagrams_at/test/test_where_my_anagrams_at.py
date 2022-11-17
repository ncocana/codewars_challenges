# importar el modulo de otro directorio
from src.where_my_anagrams_at import anagrams
import pytest


@pytest.mark.anagrams
def test_anagrams():
    cases = [
            ('abba', ['aabb', 'abcd', 'bbaa', 'dada', 'abbb', 'aaab'], ['aabb', 'bbaa']),
            ('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'], ['carer', 'racer']),
            ('laser', ['lazing', 'lazy', 'lacer'], []),
            ('a', ['a', 'b', 'c', 'd'], ['a']),
            ('big', ['gig', 'dib', 'bid', 'biig'], []),
            ('ab', ['cc', 'ac', 'bc', 'cd', 'ab', 'ba', 'racar', 'caers', 'racer'], ['ab', 'ba']),
            ('abba', ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa', 'babaa'], ['aabb', 'bbaa', 'abab', 'baba', 'baab']),
    ]
    for word, words, expected in cases:
        assert anagrams(word, words) == expected
